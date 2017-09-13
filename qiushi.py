#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import codecs
import requests

DOWNLOAD_URL = 'https://www.qiushibaike.com/text/'


def download_page(url):
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'}).text


def parse_html(html):
    nextpage = ""
    content_list = []
    nextpage_reg = "<a href=\"([^\"]*?)\"[^<]*?<[^>]*?>\s下一页"
    content_reg = "<div class=\"content\">\s*?<span>([\w\W]*?)</span>"

    content_list = re.findall(content_reg, html)
    if re.findall(nextpage_reg, html):
        nextpage = re.findall(nextpage_reg, html)[0]
        nextpage = "{}{}".format(DOWNLOAD_URL, nextpage.replace("/text/", ""))

    return content_list, nextpage


def main():
    url = DOWNLOAD_URL
    with codecs.open('qiushis', 'wb', encoding='utf-8') as fp:
        while url:
            html = download_page(url)
            qiushis, url = parse_html(html)
            for item in qiushis:
                fp.write(item.strip().replace("<br/>", "\n") + '\n\n')


if __name__ == '__main__':
    main()


