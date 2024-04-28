# 파이썬 설치   
https://www.python.org/   

## 설치된 목록 보기   
````
pip3 list
````
## requests   

````
    pip3 install requests (Mac)
    pip3 install beautifulsoup4
    pip3 install lxml
    pip3 install pandas
    pip3 install selenium
```` 

각 라이브러리의 용도와 기능에 대한 설명
1. requests      
    requests 라이브러리는 Python에서 HTTP 요청을 보내는 기능을 제공합니다. 이를 통해 웹 페이지의 내용을 가져오거나 API를 사용할 수 있습니다. 웹 서버와의 간단한 상호작용을 위해 널리 사용됩니다.
2. beautifulsoup4
    beautifulsoup4는 HTML과 XML 파일로부터 데이터를 추출하기 위해 사용되는 라이브러리입니다. 복잡한 HTML 문서에서 데이터를 쉽게 파싱하고 조작할 수 있어 웹 스크래핑에 매우 유용합니다.
3. lxml
    lxml은 XML과 HTML을 처리하기 위한 라이브러리로, 매우 빠르고 기능이 풍부합니다. 주로 beautifulsoup4와 함께 사용되어 파싱 처리 속도를 향상시키는 파서로 사용됩니다.
4. pandas
    pandas는 데이터 분석과 조작을 위해 널리 사용되는 라이브러리입니다. 데이터를 효율적으로 처리하고 변형 및 분석할 수 있게 해주며, 다양한 형식의 데이터를 쉽게 다룰 수 있습니다.
5. selenium
    selenium은 웹 브라우저를 자동화하기 위해 사용되는 라이브러리입니다. 웹 애플리케이션의 테스트 자동화나 복잡한 웹 페이지와의 상호작용을 자동화하는데 사용됩니다.

## 파이썬 확인 방법
- cd python
- python3 들어갈 주소 .py
# 사이트 코드 갯수를 확인 하기 위해
    res.status_code를 사용

# 코드가 보이지 않을때 
    head = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML,   like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    head로 user-Agent를 이용해서 보여지게 한다

# 깔끔하게 소스를 보는 방법 (BeautifulSoup)
    from bs4 import BeautifulSoup as bs 를 설치 하게 한후
    soup = bs(res.text, "lxml")
    print(soup) 로 실행

# 해당 클래스 갯수 보는 방법
    ranking = soup.select(".ranking > strong")
    print(ranking)
(소스 안에있는 클래스 ranking의 갯수를 불러온다)

# 데이터 선택 방법
    ranking = soup.select(".ranking > strong")
    title = soup.select(".title > a")
    artist = soup.select(".artist >a")

# 원하는 클래스 내용 텍스트로 보이게 하는 방법
    # 데이터 저장
    rankingList = []
    titleList = []
    artistList = []
    
    for i in range(len(ranking)) : 
        rankingList.append(ranking[i].text)
        titleList.append(title[i].text)
        artistList.append(artist[i].text)
    
    print(rankingList)
    print(titleList)
    print(artistList)

# 저장된 데이터를 json 파일로 만드는 방법 (pandas)
    import pandas as pd

    data = {"rank" : rankingList, "title" : titleList, "artist" : artistList}
    print(pd.DataFrame(data))

# json 파일을 만드는 방법

- 데이터 저장 한문장으로
rankingList = [r.text.strip() for r in ranking]
titleList = [t.text.strip() for t in title]
artistList = [a.text.strip() for a in artist]

- 데이터 프레임 생성
chart_df = pd.DataFrame({
    'Ranking' : rankingList,
    'Title': titleList,
    'Artist' : artistList
})

- JSON 파일로 저장
chart_df.to_json("busChart100.json", force_ascii=False, orient="records")

## Vscode 확장프로그램 
- python
