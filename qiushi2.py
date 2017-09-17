#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL='https://www.qiushibaike.com/text/'

headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'}

parse_html=requests.get(DOWNLOAD_URL,headers=headers)

Soup=BeautifulSoup(parse_html.text,'lxml')

joke_list=Soup.find('div',class_='col1')

with open('jokes', 'w+', encoding='utf-8') as f:
    for joke in Soup.find_all('div',class_='content'):
        joke_content=joke.find('span').getText()
        #print(joke_content)
        f.write(joke_content)
        f.write('\n')













