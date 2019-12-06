# -*- coding:utf-8 -*-
import scrapy
import re

class stockspider(scrapy.Spider):
    name = 'stocks'
    start_urls = ['http://quote.eastmoney.com/stocklist.html']

    def parse(self,response):
        for href in response.css('a::attr(href)').extract():
            try:
                stock = re.findall(r'[s][zh]\d{6}',href)[0]
                url = 'https://gupiao.baidu.com/stock/' + stock + '.html'
                yield scrapy.Request(url,callback = self.parse_stock)
            except:
                continue

    def parse_stock(self,response):
        infoDict = {}
        stockInfo = response.css('.stock-bets')
        name = stockInfo.css('.bets-name').estract()[0]
        keylist = stockInfo.css('dt').extract()
        valuelist = stockInfo.css('dd').extract()
        for i in range(len(keylist)):
            key = re.findall(r'>.*</dt>',keylist[i])[0][1:-5]
            try:
                val = re.findall(r'\d+\.?.*<dd>',valuelist[i])[0][0:-5]
            except:
                val = '--'
            infoDict[key] = val

        infoDict.update(
                {'股票名称':re.findall('\s.*\(',name)[0].split()[0] + \
                        re.findall('\>.*\<',name)[0][1:-1]})
        yield infoDict
