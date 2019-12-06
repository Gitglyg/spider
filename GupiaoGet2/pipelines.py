


class BaidustocksInfoPipeline(object):
    def open_spider(self,spider):
        self.f = open('BaidustockInfo.txt','w')

    def close_spider(self,spider):
        self.f.close()

    def process_item(self,item,spider):
        try:
            line = str(dict(item)) + '\n'
            slef.f.write(line)
        except:
            pass
        return item
