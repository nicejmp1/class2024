import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

res = req.get("https://music.apple.com/kr/playlist/%EC%98%A4%EB%8A%98%EC%9D%98-top-100-%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/pl.d3d10c32fbc540b38e266367dc8cb00c")

# print(res.text)
# print(res.status_code)

soup = bs(res.text, "lxml")
print(soup)


