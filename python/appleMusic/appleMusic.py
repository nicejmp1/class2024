# import json
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from webdriver_manager.chrome import ChromeDriverManager

# filename = 'appleMusic100.json'
# # Chrome 옵션 설정
# options = ChromeOptions()
# options.add_argument("window-size=1920x1080")
# options.add_argument("disable-gpu")
# options.add_argument("lang=ko_KR")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
# service = ChromeService(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)

# driver.get("https://music.apple.com/kr/playlist/%EC%98%A4%EB%8A%98%EC%9D%98-top-100-%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/pl.d3d10c32fbc540b38e266367dc8cb00c")

# time.sleep(10) 

# # 웹 페이지에서 데이터 추출
# playicon_elements = driver.find_elements(By.CSS_SELECTOR, '[data-testid="artwork"] .svelte-1vcdnyq > source[type="image/jpeg"]')
# rankings_elements = driver.find_elements(By.CSS_SELECTOR, '[data-testid="track-ranking"]')
# titles_elements = driver.find_elements(By.CSS_SELECTOR, '[data-testid="track-title"]')
# artists_elements = driver.find_elements(By.CSS_SELECTOR, '.svelte-154tqzm [data-testid="click-action"]')

# # 추출한 데이터를 리스트로 저장
# ranking_list = [rank.text for rank in rankings_elements]
# title_list = [title.text for title in titles_elements]
# artist_list = [artist.text for artist in artists_elements if artist.text.strip() != '']
# playicon_list = [img.get_attribute('srcset').split(',')[0].split(' ')[0].replace('\\', '') for img in playicon_elements]

# # 데이터의 길이를 동일하게 맞춤
# min_length = min(len(ranking_list), len(title_list), len(artist_list), len(playicon_list))

# # JSON 형식으로 변환할 리스트
# music_data = []
# for i in range(min_length):
#     music_data.append({
#         "Rank": ranking_list[i],
#         "Title": title_list[i],
#         "Artist": artist_list[i],
#         "PlayIcon": playicon_list[i]
#     })

# # 데이터를 JSON 파일로 저장
# with open(filename, 'w', encoding='utf-8') as f:
#     json.dump(music_data, f, ensure_ascii=False, indent=4)

# # 브라우저 종료
# driver.quit()

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
filename = f"chart_apple100_{current_date}.json"
# 웹드라이브 설치
options = ChromeOptions()
service = ChromeService(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)
browser.get("https://music.apple.com/kr/playlist/%EC%98%A4%EB%8A%98%EC%9D%98-top-100-%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/pl.d3d10c32fbc540b38e266367dc8cb00c")

# 페이지가 완전히 로드될 때까지 대기
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "songs-list"))
)

# 업데이트된 페이지 소스를 변수에 저장
html_source_updated = browser.page_source
soup = BeautifulSoup(html_source_updated, 'html.parser')

print(soup)

time.sleep(10)

# 노래 정보를 추출
song_data = []
songs_list = soup.find_all('div', class_='songs-list-row', role='row')

for song in songs_list:
    ranking = song.find('div', class_='songs-list-row__rank').text.strip()
    title = song.find('div', class_='songs-list-row__song-name').text.strip()
    artist = song.find('a', {'data-testid': 'click-action'}).text.strip()
    album = song.find_all('a', {'data-testid': 'click-action'})[1].text.strip()
    img_tag = song.find('picture').find('source', type="image/webp")  # More specific targeting to webp images
    if img_tag:
        image_sources = img_tag['srcset']
        # Extracting the desired 80x80 webp image URL from srcset
        image_url = next((src.split(' ')[0] for src in image_sources.split(',') if '80x80bb.webp' in src), "No image available")
    else:
        image_url = "No image available"

    song_data.append({
        'ranking': ranking,
        'title': title,
        'artist': artist,
        'album': album,
        'image_url': image_url
    })

# 추출된 데이터를 JSON 파일로 저장
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(song_data, f, ensure_ascii=False, indent=4)

# 브라우저 종료
browser.quit() 