from email import header
from wsgiref import headers
import requests
from bs4 import BeautifulSoup
import json
import os
import sys

file_path = "C:/Users/USER/Desktop/캡스톤/크롤링결과/국제1link.json"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print('캡스톤 2조 뉴스 크롤러 시작')

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/98.0.4758.102" }

url_1 = 'https://news.daum.net/breakingnews/foreign?page='

news = []
url = []

for i in range(1,3):
    url_full=url_1+str(i)
    print(url_full)
    req = requests.get(url_full)
    req.encoding= None
    html = req.content
    soup = BeautifulSoup(html, 'html.parser')
    for capstone in soup.find('div', attrs={'class':'box_etc'}).find_all("li"):  
        url.append(capstone.find("a")["href"])
        news.append({
        'title': capstone.find('a', attrs={'class':'link_txt'}).text,
        'url': capstone.find("a")["href"]
    })
  
        

print(url)
#사회
#정치 : https://news.daum.net/breakingnews/politics
#경제 : https://news.daum.net/breakingnews/economic
#국제 : https://news.daum.net/breakingnews/foreign
#문화 : https://news.daum.net/breakingnews/culture
#IT : https://news.daum.net/breakingnews/digital
#스포츠 : https://news.daum.net/breakingnews/sports
#연예 : https://news.daum.net/breakingnews/entertain





    


with open(file_path, 'w', encoding='UTF-8') as outfile:
    json.dump(url, outfile, indent=4, ensure_ascii=False)