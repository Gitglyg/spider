#!/usr/bin/env python3
import requests
import re

def getHTMLText(url):
    headerskey = {'user-agent':'chrome/5.0',"cookie": "t=c1e8231792f007e72593175d60586f3a; cna=HthOFWZZfEoCAZkiYyMw5eUw; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; tracknick=tb313659628; lgc=tb313659628; tg=0; enc=C%2B2%2F0QsEwiUFmf00owySlc7hJiEsY4t4EIGdIzzH6ih9ajzhcMJCs7wzlX4%2B4gJrv2IlLviuxk0B1VAXlVwD8Q%3D%3D; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; miid=1314040285196636905; uc3=vt3=F8dBy3vI3wKCeS4bgiY%3D&id2=VyyWskFTTiu0DA%3D%3D&nk2=F5RGNwsJzCC9CC4%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D; _cc_=VFC%2FuZ9ajQ%3D%3D; _m_h5_tk=ec90707af142ccf8ce83ead2feda4969_1560657185501; _m_h5_tk_enc=2bc06ae5460366b0574ed70da887384e; mt=ci=-1_0; cookie2=14c413b3748cc81714471780a70976ec; v=0; _tb_token_=e33ef3765ebe5; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; swfstore=97544; JSESSIONID=80EAAE22FC218875CFF8AC3162273ABF; uc1=cookie14=UoTaGdxLydcugw%3D%3D; l=bBjUTZ8cvDlwwyKtBOCNCuI8Li7OsIRAguPRwC4Xi_5Z86L6Zg7OkX_2fFp6Vj5RsX8B41jxjk99-etki; isg=BP__g37OnjviDJvk_MB_0lRbjtNJTFLqmxNfMJHMlK71oB8imbTI1uey5jD7-Cv-"}
    #s = requests.session()
    #post_data = {'TPL_username':'一堂课v','TPL_password':'napux@6737430'}
    #rs = s.post(login_url,post_data)

    #c =requests.cookies.RequestsCookieJar()
    #c.set('cookie-name','cookie-value')
    #s.cookies.update(c)
    #print(s.cookies.get_dict())

    r = requests.get(url,headers = headerskey)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def parsePage(ilt,html):
    tlt = re.findall(r'"raw_title":".*?"',html)
    plt = re.findall(r'"view_price":"[\d.]*"',html)
    for i in range(len(plt)):
        price = eval(plt[i].split(':')[1])
        title = eval(tlt[i].split(':')[1])
        ilt.append([price,title])

def printGoodList(ilt,file):
    tplt = '{:4}\t{:8}\t{:20}'
    print(tplt.format('序号','价格','名称'))
    count = 0
    for g in ilt:
        count += 1
        print(tplt.format(count,g[0],g[1]))
        file.write(tplt.format(count,g[0],g[1])+'\n')

def main():
    key = '书包'
    start_url = 'https://s.taobao.com/search?q='+key
    depth = 3
    infoList = []
    for i in range(depth):
        url = start_url + '&s=' + str(i*44)
        html = getHTMLText(url)
        parsePage(infoList,html)
    with open('tb.txt','w') as f:
        printGoodList(infoList,f)

if __name__ == '__main__':
    main()


