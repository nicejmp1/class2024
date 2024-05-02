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
    "http://www.hoolala.co.kr/menu/default.aspx?menu=%uC804%uCCB4%uBA54%uB274"
]

# 현재 날짜 가져오기
current_date = datetime.now().strftime("%Y-%m-%d")
filename = f"hoolala_chicken{current_date}.json"
base_url = "http://www.hoolala.co.kr"

# 웹드라이버 설정
options = ChromeOptions()
service = ChromeService(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)

def get_menu_data(browser, base_url):
    # 페이지 소스 가져오기
    html_source = browser.page_source
    soup = BeautifulSoup(html_source, 'html.parser')

    menu_data = []
    menu_items = soup.select(".m_menu_big_box")
    for item in menu_items:
        title = item.find('li', class_='m_menu_text').text.strip() 
        money = item.find('li', class_='menu_price').text.strip() 
        image = item.find('img', class_='thumbMenu')['src'] 
        if image.startswith('/'):
            image = base_url + image    

        menu_data.append({
            "title": title,
            "money": money,
            "imageURL": image
        })
    return menu_data

all_menu_data = []

for url in urls:
    browser.get(url)
    # 페이지가 완전히 로드될 때까지 대기
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "menu_spa_box"))
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
