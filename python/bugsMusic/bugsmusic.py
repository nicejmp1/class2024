import requests as req
from bs4 import BeautifulSoup as bs
import json

res = req.get("https://music.bugs.co.kr/chart")

soup = bs(res.text, "lxml")

# 데이터 선택
ranking_elements = soup.select(".ranking > strong")
title_elements = soup.select(".title > a")
artist_elements = soup.select(".artist > a:nth-child(1)")
image_elements = soup.select(".trackList > tbody .thumbnail img ")

# 데이터 저장
chart_data = []
for rank, title, artist, image in zip(ranking_elements, title_elements, artist_elements, image_elements):
    chart_data.append({
        'Ranking': rank.text.strip(),
        'Title': title.text.strip(),
        'Artist': artist.text.strip(),
        'Image': image['src'].strip()
    })

# JSON 파일로 저장
with open("bugsChart100.json", "w", encoding='utf-8') as json_file:
    json.dump(chart_data, json_file, ensure_ascii=False, indent=4)
