#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os

DOWNLOAD_URL = 'http://www.mzitu.com/all'
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'}

parse_html = requests.get(DOWNLOAD_URL, headers=headers)
Soup = BeautifulSoup(parse_html.text, 'lxml')
img_list = Soup.find('div',class_='all').find_all('a')  #注意class后面的下划线
for img in img_list:
    title=img.get_text()
    href=img['href']
    html=requests.get(href,headers=headers)
    html_soup=BeautifulSoup(html.text,'lxml')
    max_span=html_soup.find('div',class_='pagenavi').find_all('span')[-2].get_text()
    for page in range(1,int(max_span)+1):
        page_url=href+'/'+str(page)
        img_html=requests.get(page_url,headers=headers)
        img_soup=BeautifulSoup(img_html.text,'lxml')
        img_url=img_soup.find('div',class_='main-image').find('img')['src']
        name=img_url[-9:-4]
        img=requests.get(img_url,headers=headers)
        f=open(name+'.jpg','ab')
        f.write(img.content)
        f.close()
