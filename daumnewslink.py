from email import header
from wsgiref import headers
import requests
from bs4 import BeautifulSoup
import json
import os
import sys

#file_path = "C:/Users/USER/Desktop/캡스톤/크롤링결과/국제1.json"
file_path = "C:/Users/USER/Desktop/캡스톤/DaumNewsCrawling/국제test.json"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print('캡스톤 2조 뉴스 크롤러 시작')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/98.0.4758.102"}

with open("C:/Users/USER/Desktop/캡스톤/크롤링결과/국제1link.json", "r") as f:
    data = json.load(f)

url_h = data

#ur_h는 테스트용 사용X
ur_h = ["https://v.daum.net/v/20220524111344387",
        "https://v.daum.net/v/20220524111342386",
        "https://v.daum.net/v/20220524111339384",
        "https://v.daum.net/v/20220524111337383",
        "https://v.daum.net/v/20220524111329378",
        "https://v.daum.net/v/20220524111326375",
        "https://v.daum.net/v/20220524111323373",
        "https://v.daum.net/v/20220524111308354",
        "https://v.daum.net/v/20220524111306352",
        "https://v.daum.net/v/20220524111303348",
        "https://v.daum.net/v/20220524111303347",
        "https://v.daum.net/v/20220524111258338",
        "https://v.daum.net/v/20220524111231319",
        "https://v.daum.net/v/20220524111215307",
        "https://v.daum.net/v/20220524111212303",
        "https://v.daum.net/v/20220524111210300",
        "https://v.daum.net/v/20220524111209296",
        "https://v.daum.net/v/20220524111207288",
        "https://v.daum.net/v/20220524111207287",
        "https://v.daum.net/v/20220524111205286",
        "https://v.daum.net/v/20220524111204281",
        "https://v.daum.net/v/20220524111201270",
        "https://v.daum.net/v/20220524111201271",
        "https://v.daum.net/v/20220524111200267",
        "https://v.daum.net/v/20220524111158264",
        "https://v.daum.net/v/20220524111147256",
        "https://v.daum.net/v/20220524111146254",
        "https://v.daum.net/v/20220524111146253",
        "https://v.daum.net/v/20220524111143250",
        "https://v.daum.net/v/20220524111116221"
        ]

news = []
hh = []
publisher = []

for url in url_h:
    req = requests.get(url)
    req.encoding = None
    html = req.content
    soup = BeautifulSoup(html, 'html.parser')
    # for a in soup.select('#harmonyContainer > section > figure > p'):
    # img.append({
    # 'img': a.find("img")["src"]})
    # for h in soup.select('#cSub > div > em'):
    # publisher.append({
    # 'publisher': h.find("img")["alt"]})
    
    p_tag = soup.find_all('p', attrs={'dmcf-ptype': 'general'})
    for context in p_tag:
        con = context.text
        #print(con)
        hh.append({
            'context': con
        })

    for a in soup.select('#harmonyContainer > section > figure > p'):
        for h in soup.select('#cSub > div > em'):
            news.append({
                'title': soup.find('h3', attrs={'class': 'tit_view'}).text,
                'url': url,
                'reporter': soup.find('span', attrs={'class': 'txt_info'}).text,
                'date': soup.find('span', attrs={'class': 'num_date'}).text,
                'img': a.find("img")["src"],
                'publisher': h.find("img")["alt"]
                #'context': p_tag.text
            })

#print(news)
with open(file_path, 'w', encoding='UTF-8') as outfile:
    json.dump(news, outfile, indent=4, ensure_ascii=False)
#cSub > div > em > img




#harmonyContainer > section > figure:nth-child(2) > p
#harmonyContainer > section > figure > p