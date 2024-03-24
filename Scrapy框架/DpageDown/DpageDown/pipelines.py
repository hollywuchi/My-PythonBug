# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


#如果想使用管道，那么就要在setting中打开pipelines
class DpagedownPipeline:
    #在爬虫文件开始之前就执行的一个方法
    def open_spider(self,spider):
        print("————————————————————————————————————————")
        self.f = open("book.json","w",encoding = "utf-8")


    def process_item(self, item, spider):
        
        self.f.write(str(item))
        return item
    
    #在爬虫文件执行完成之后执行的一个方法
    def close_spider(self,spider):
        print("————————————————————————————————————————")
        self.f.close()

import urllib.request

class IpageDownPipeline:
    #在新建管道的时候，一定要把方法名都改为”process_item“，否则不会被判定为一个管道
    def process_item(self,item,spider):
        url = "http:" + item.get("img")[0]    #这里因为返回的是一个列表，所以要取第一个值
        fileName = "./img/" +item.get("name")[0] + ".jpg"
        urllib.request.urlretrieve(url = url,filename = fileName)
        return item