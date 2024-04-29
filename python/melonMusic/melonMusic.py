import requests as req
from bs4 import BeautifulSoup as bs
import json

# 요청 헤더 설정
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}

# 멜론 차트 페이지 요청
res = req.get("https://www.melon.com/chart/index.htm", headers=head)
soup = bs(res.text, "lxml")

# 데이터 선택
ranking_elements = soup.select("tbody .wrap.t_center > .rank")
title_elements = soup.select("tbody .wrap_song_info .ellipsis.rank01 span > a")
artist_elements = soup.select("tbody .wrap_song_info .ellipsis.rank02 span > a:nth-child(1)")
icon_elements = soup.select(".wrap > a > img")

# 데이터 추출 및 저장
chart_data = []
for rank, title, artist, icon in zip(ranking_elements, title_elements, artist_elements, icon_elements):
    chart_data.append({
        'Ranking': rank.text.strip(),
        'Title': title.text.strip(),
        'Artist': artist.text.strip(),
        'PlayIcon': icon['src'].strip()
    })

# JSON 파일로 저장
with open("MelonChart100.json", "w", encoding='utf-8') as json_file:
    json.dump(chart_data, json_file, ensure_ascii=False, indent=4)
