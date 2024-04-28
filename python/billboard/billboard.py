import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

res = req.get("https://www.billboard.com/charts/hot-100/")


soup = bs(res.text, "lxml")
# print(soup)

# 데이터 선택
ranking = soup.select(r".u-letter-spacing-0080\@tablet")
title = soup.select(".o-chart-results-list-row-container .lrv-u-width-100p  #title-of-a-story ")
artist = soup.select(".a-truncate-ellipsis-2line")
img = soup.select(".o-chart-results-list__item > .c-lazy-image > .lrv-a-crop-1x1 > img.c-lazy-image__img")
print(img)

rankingList = [r.text.strip() for r in ranking]
titleList = [t.text.strip() for t in title]
artistList = [a.text.strip() for a in artist]
imgList = [img['data-lazy-src'].strip() for img in img]

# 데이터 프레임 생성
chart_df = pd.DataFrame({
    'Ranking' : rankingList,
    'Title': titleList,
    'Artist' : artistList,
    'Imglist' : imgList
})


# JSON 파일로 저장
chart_df.to_json("billboard100.json", force_ascii=False, orient="records")
