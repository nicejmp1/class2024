import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import json

# Chrome 옵션 설정
options = ChromeOptions()
options.add_argument("window-size=1920x1080")
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 사이트 접속
driver.get('https://www.soribada.com/music/chart')
time.sleep(10) 

# 데이터 추출
search_box = driver.find_element(By.CLASS_NAME, 'music-list')
rankings = search_box.find_elements(By.CLASS_NAME , 'num')
titles = search_box.find_elements(By.CLASS_NAME , 'song-title')
artists = search_box.find_elements(By.CLASS_NAME ,  'link-type2-name')
playicons = driver.find_elements(By.CSS_SELECTOR, ".music-list .listen .img img")

chart_data = []
for rank, title, artist, playicon in zip(rankings, titles, artists, playicons):
    chart_data.append({
        "Ranking": rank.text,
        "Title": title.text,
        "Artist": artist.find_element(By.TAG_NAME, 'span').text,
        "Playicon": playicon.get_attribute('src')
    })

# JSON 파일로 저장
with open("soriBadaMusicChart.json", "w", encoding='utf-8') as file:
    json.dump(chart_data, file, ensure_ascii=False, indent=4)

# 드라이버 종료
driver.quit()
