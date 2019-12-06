#!/usr/bin/env python3

import requests
import re
from bs4 import BeautifulSoup
import traceback

def getHTML(url,code='utf-8'):
    head = {'user-agent':'Chrome/5.0'}
    r = requests.get(url,headers = head)
    r.raise_for_status()
    r.encoding = code
    return r.text

def getMassage(lst,Murl):
    html = getHTML(Murl,'GB2312')
    soup = BeautifulSoup(html,'html.parser')
    a = soup.find_all('a')
    for i in a:
        href = i.attrs['href']
        lst.append(re.findall(r"[s][zh]\d{6}",href)[0])

def getInfo(lit,Murl,fpath):
    count = 0 
    for i in lit:
        nurl = Murl + i + '.html'
        t = getHTML(nurl)
        try:
            if t == "":
               continue
            infoDict = {}
            soup = BeautifulSoup(t,'html.parser')
            Minfo = soup.find('div',attrs={'class':'stock-bets'})

            name = Minfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})

            keylist = Minfo.find('dt')
            valuelist = Minfo.find('dd')
            for i in range(lenkeylist):
                key = keylist[i].text
                value = valuelist[i].text
                infoDict[key] = value

            with open(fpath,'a',encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count = count + 1
                print('\r当前进度:{:.2f}'.format(count*100/len(lst)),end='')
        except:
            traceback.print_exc()
            continue

def main():
    list_url = 'http://quote.eastmoney.com/stocklist.html'
    info_url = 'http://gupiao.baidu.com/stock'
    slist = []
    getMassage(slist,list_url)
    fpath = '/Document/gupiao.txt'
    getInfo(slist,info_url,fpath)


main()
