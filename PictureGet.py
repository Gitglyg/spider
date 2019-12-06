#!/usr/bin/env python3
import requests
import os

url = 'https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign=f46180464a34970a4373172da5cbd1c0/d50735fae6cd7b89c2e372ea042442a7d8330ecf.jpg'
root = '/Pictures/'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url,timeout = 30)
        print(r.status_code)
        with open(path,'wb') as f:	# ‘wb’可二进制写入文件
            f.write(r.content)
            print('文件保存成功')
    else:
        print('文件已存在')
except:
    print('爬取失败')
