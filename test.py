# -*- coding: utf-8 -*-

import sys
import io
from flask import Flask, request, Response
from bs4 import BeautifulSoup, CData
import urllib.request
import urllib.parse
import time
import re

keyword = 'hello'
data = None
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"}
#1 http://www.xiami.com/search?pos=1&key={keyword} html
req1 = urllib.request.Request('http://www.xiami.com/search?pos=1&key=' + urllib.parse.quote(keyword), data, headers)
response1 = urllib.request.urlopen(req1)
xiami_soup1 = BeautifulSoup(response1.read().decode('gbk', 'ignore').encode('utf-8'), 'html.parser')
td_songs = xiami_soup1.find_all('td', class_='song_name')
for td in td_songs:
    a = td.find('a')
    if str(a['href'])[:4] != 'http':
        a = a.next_sibling.next_sibling
    req2 = urllib.request.Request(a['href'], data, headers)
    response2 = urllib.request.urlopen(req2)
    xiami_soup2 = BeautifulSoup(response2.read(), 'html.parser')
    lrc_main = xiami_soup2.find('div', class_='lrc_main')
    if lrc_main != None:
        info = xiami_soup2.find(id='albums_info').get_text().replace('：\n', '：').replace('\n\n\n', '\n')
        geci = info + lrc_main.get_text().strip()
        print(geci)
print("未查到歌词")