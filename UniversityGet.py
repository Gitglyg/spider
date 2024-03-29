#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string,
                tds[3].string])

def printUnivList(ulist,num):
    tplt = '{0:^5}\t{1:{4}^15}\t{2:{4}^10}\t{3:<5}'
    print(tplt.format('排名','学校','省份','总分',chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],u[3],chr(12288)))

def main():
    unifo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(unifo,html)
    printUnivList(unifo,30) # 30 univs

main()    
