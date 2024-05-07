from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime

# URL 목록
urls = [
    "https://www.cheogajip.co.kr/bbs/board.php?bo_table=allmenu&page=1",
    "https://www.cheogajip.co.kr/bbs/board.php?bo_table=allmenu&page=2"
]

# 현재 날짜 가져오기
current_date = datetime.now().strftime("%Y-%m-%d")
filename = f"cheogajip_chicken{current_date}.json"
base_url = "https://www.cheogajip.co.kr"

# 웹드라이버 설정
options = ChromeOptions()
service = ChromeService(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)


def get_menu_data(browser, base_url):
    html_source = browser.page_source
    soup = BeautifulSoup(html_source, 'html.parser')

    menu_data = []
    menu_items = soup.select(".gall_li")
    for item in menu_items:
        title_element = item.select_one('.gall_text_href')
        if title_element:
            # 모든 공백과 개행을 제거하고 처음 나오는 개행 이전의 텍스트만 가져오기
            title_full_text = title_element.text.strip()
            # 개행 문자를 기준으로 분할하여 첫 부분만 선택
            title = title_full_text.split('\n')[0]
            # 추가적으로 공백과 탭을 제거하여 정리
            title = ' '.join(title.split())  # 여러 공백을 하나의 공백으로 축소
        else:
            title = 'No Title'

# Sub 정보 추출
        sub_element = item.select_one('p')  # <p> 태그 직접 선택
        sub = sub_element.text.strip() if sub_element else 'No Sub'

        money_element = item.select_one('.menuprice')
        money = money_element.get_text(strip=True) if money_element else 'No Price'

        image_element = item.select_one('.gall_href > img')
        image = image_element['src'] if image_element else 'No Image'
        if image.startswith('/'):
            image = base_url + image    

        menu_data.append({
            "title": title,
            "sub": sub,
            "money": money,
            "imageURL": image
        })
    return menu_data



all_menu_data = []

for url in urls:
    browser.get(url)
    # 페이지가 완전히 로드될 때까지 대기
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "bo_gall"))
    )
    # 데이터 추출
    menu_data = get_menu_data(browser, base_url)
    all_menu_data.extend(menu_data)
    time.sleep(3)  # 간단한 대기 시간 추가

# 데이터를 JSON 파일로 저장
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(all_menu_data, f, ensure_ascii=False, indent=4)

# 브라우저 종료
browser.quit()
