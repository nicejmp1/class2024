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
    "http://www.kyedong.com/menu/default.aspx?menu=%uB9C8%uB298%uAC04%uC7A5%uBA54%uB274",
    "http://www.kyedong.com/menu/default.aspx?menu=%uD56B%uC18C%uC2A4%uBA54%uB274",
    "http://www.kyedong.com/menu/default.aspx?menu=%uD6C4%uB77C%uC774%uB4DC%uC591%uB150",
    "http://www.kyedong.com/menu/default.aspx?menu=%uCE58%uD0A8%uC0D0%uB7EC%uB4DC%uC640%uCE58%uD0A8%uAE4C%uC2A4",
    "http://www.kyedong.com/menu/default.aspx?menu=%uB625%uC9D1%uD280%uAE40",
    "http://www.kyedong.com/menu/default.aspx?menu=%uBD88%uB2ED%uBC1C"
]

# 현재 날짜 가져오기
current_date = datetime.now().strftime("%Y-%m-%d")
filename = f"kyedong_chicken{current_date}.json"
base_url = "http://www.kyedong.com"

# 웹드라이버 설정
options = ChromeOptions()
service = ChromeService(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)

def get_menu_data(browser, base_url):
    # 페이지 소스 가져오기
    html_source = browser.page_source
    soup = BeautifulSoup(html_source, 'html.parser')

    menu_data = []
    menu_items = soup.select(".mn1")
    for item in menu_items:
        title = item.find('p', class_='mn1_tit').text.strip() if item.find('p', class_='mn1_tit') else 'No Title'
        description = item.find('p', class_='mn1_con').text.strip() if item.find('p', class_='mn1_con') else 'No Description'
        image = item.find('img', class_='thumbMenu')['src'] if item.find('img', class_='thumbMenu') else 'No Image URL'
        if image.startswith('/'):
            image = base_url + image    

        menu_data.append({
            "title": title,
            "description": description,
            "imageURL": image
        })
    return menu_data

all_menu_data = []

for url in urls:
    browser.get(url)
    # 페이지가 완전히 로드될 때까지 대기
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sub_container"))
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
