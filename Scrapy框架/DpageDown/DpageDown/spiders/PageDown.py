import scrapy

#想要将那三个变量传回item里，要先将那个item导入
from DpageDown.items import DpagedownItem


class PagedownSpider(scrapy.Spider):
    name = "PageDown"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["http://category.dangdang.com/cp01.45.55.14.00.00.html"]

# http://category.dangdang.com/pg2-cp01.45.55.14.00.00.html
    base_url = "http://category.dangdang.com/pg"
    page = 1
    def parse(self, response):
        # print("——————————————————————————————————————————————————————————————————————")
        li_list = response.xpath("//ul[@id='component_59']/li")
        
        for li in li_list:
            name = li.xpath('.//img/@alt').extract()
            img = li.xpath('.//img/@data-original').extract()
            price = li.xpath('.//span[@class="search_now_price"]/text()').extract()
            if img:
                img = img
            else:
                img = li.xpath('.//img/@src').extract()
            
            book  = DpagedownItem(img = img,name = name,price = price)
            yield book
        
        #一个递归：可以重复的调用这个方法，一直到满足条件
        if self.page < 10:  #下载前十页的数据
            self.page = self.page + 1   #如果页数不满，就加页数
            url = self.base_url + str(self.page) + "-cp01.45.55.14.00.00.html"  

            #scrapy.request是scrapy的get请求部分（之后还有post部分）
            yield scrapy.Request(url = url,callback = self.parse)   #下一个要打开的网页
            #callback = 可以让你选择一个要重复执行的方法，但是不能有（）
        # print("——————————————————————————————————————————————————————————————————————")