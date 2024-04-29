from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import json
from datetime import datetime

# 현재 날짜 가져오기
current_date = datetime.now().strftime("%Y-%m-%d")
filename = f"chart_flo100_{current_date}.json"
# 웹드라이브 설치
options = ChromeOptions()
service = ChromeService(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)
browser.get("http://www.ttobongee.com/skin3/menu.php")

# 페이지가 완전히 로드될 때까지 대기
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "data-wrap"))
)

# # "더보기" 버튼을 찾아 클릭
# try:
#     more_button = WebDriverWait(browser, 10).until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn_list_more"))
#     )
#     if more_button:
#         browser.execute_script("arguments[0].click();", more_button)
#         print("Clicked '더보기' button.")
#         time.sleep(3)
# except Exception as e:
#     print("Error clicking '더보기':", e)

# time.sleep(3)

# 업데이트된 페이지 소스를 변수에 저장
html_source_updated = browser.page_source
soup = BeautifulSoup(html_source_updated, 'html.parser')

# print(soup)

# 데이터 추출
menu_data = []
menu = soup.select(".data_wrap .menuList")
for main in menu:
    mainmenu = main.select_one(".name").text.strip()

    print(mainmenu)
    title = main.select_one(".tit__text").text.strip()
    artist = main.select_one(".artist__link").text.strip()
    album = main.select_one(".album").text.strip()
    image_url = main.select_one(".thumb img").get('data-src')

    menu_data.append({
        "rank": mainmenu,
        "title": title,
        "artist": artist,
        "imageURL": image_url,
        "album": album
    })

# 데이터를 JSON 파일로 저장
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(music_data, f, ensure_ascii=False, indent=4)

# 브라우저 종료
browser.quit()

# title = browser.find_elements(By.CSS_SELECTOR, ".tit__text")
# artist = browser.find_elements(By.CSS_SELECTOR, "span.artist__link.last")
# ranking = browser.find_elements(By.CSS_SELECTOR, "td.num")
# # print(len(ranking))

# titleList = [title.text for title in title]
# artistList = [art.text for art in artist]
# rankList = [rank.text for rank in ranking]

