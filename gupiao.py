#!/usr/bin/env python3

import requests
import re
from bs4 import BeautifulSoup
import traceback

def getHTML(url):
    head = {'user-agent':'Chrome/5.0'}
    r = requests.get(url,headers = head)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def getMassage(lit,Murl):
    return''

def getInfo(lit,Murl,info):
    for i in lit:
        nurl = Murl + 's=' + i[1]
        t = getHTML(nurl)
        info.write(t)
    return''

def main():
    list_url = 'http://quote.eastmoney.com/stocklist.html'
    info_url = 'http://gupiao.baidu.com/stock'
    slist = []
    getMassage(slist,list_url)
    with open('/Pictures/gupiao.txt','w') as f:
        getInfo(slist,info__url,f)

