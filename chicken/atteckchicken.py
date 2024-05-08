import requests as req
from bs4 import BeautifulSoup as bs
import json
from datetime import datetime


# 현재 날짜 가져오기
current_date = datetime.now().strftime("%Y-%m-%d")
filename = f"atteckchicken__{current_date}.json"

def get_menu_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    res = req.get(url, headers=headers)
    soup = bs(res.text, "lxml")
    items = soup.select(".order_list_item")  # 메뉴 아이템을 포함하는 전체 컨테이너 선택

    chart_data = []
    for item in items:
        m = item.select_one(".tit")
        s = item.select_one(".detail_txt")
        p = item.select_one(".price")
        i = item.select_one(".img_box img")  # 이미지 태그 선택

        # 이미지 URL 추출, 없으면 빈 문자열 처리
        image_url = i['src'].strip() if i and i.has_attr('src') else ""
        chart_data.append({
            'Menu': m.text.strip() if m else 'No menu',
            'Sub': s.text.strip() if s else 'No sub',
            'Price': p.text.strip() if p else 'No price',
            'img': image_url
        })
    return chart_data

# URL 정의 및 데이터 추출
url = "https://m.booking.naver.com/order/bizes/777177/items/5209875?theme=place&entry=pll&area=pll"
chart_data = get_menu_data(url)

# 데이터를 JSON 파일로 저장
with open(filename, "w", encoding='utf-8') as json_file:
    json.dump(chart_data, json_file, ensure_ascii=False, indent=4)

