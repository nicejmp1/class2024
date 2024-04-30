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

# 현재 날짜 가져오기 및 기본 URL 정의
current_date = datetime.now().strftime("%Y-%m-%d")
base_url = "http://www.ttobongee.com/skin3/"
filename = f"ttobongee_chicken{current_date}.json"

# 웹드라이버 설정
options = ChromeOptions()
service = ChromeService(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)

# 메뉴 데이터 추출 함수
def get_menu_data(browser, base_url):
    # 페이지 소스 가져오기
    html_source = browser.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    menu_data = []
    menu_items = soup.select(".menuList")
    for item in menu_items:
        # 제목 추출
        title = item.find('p', class_='name').text.strip() if item.find('p', class_='name') else 'No Title'
        # 이미지 URL 추출 (클래스 이름은 확인 필요)
        image = item.find('img')['src'] if item.find('img') else 'No Image URL'
        if image.startswith('/'):
            image = base_url + image
        # 추출된 데이터를 리스트에 추가
        menu_data.append({
            "title": title,
            "imageURL": image,
            # 여기에 description을 추가하세요
        })
    return menu_data

# 전체 메뉴 데이터를 모을 리스트
all_menu_data = []

# 페이지 접속
browser.get("http://www.ttobongee.com/skin3/menu.php")
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "content_bg")))

# 탭 전환 및 데이터 추출
tabs = browser.find_elements(By.CLASS_NAME, "a")
for tab in tabs:
    # 탭을 클릭합니다.
    tab.click()
    time.sleep(2)  # 데이터 로드를 기다립니다.

    # 탭 전환 후 데이터 추출
    all_menu_data.extend(get_menu_data(browser, base_url))

# 데이터를 JSON 파일로 저장
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(all_menu_data, f, ensure_ascii=False, indent=4)

# 브라우저 종료
browser.quit()
