#!/usr/bin/env python3
import requests

url = 'http://www.ip138.com/ips138.asp?ip='
kv = {'user-agent':'chrmod/5.0'}
try:
    r = requests.get(url+'202.204.80.112',headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-2700:-2200])
except:
    print('爬取失败')
