import scrapy


class TongchengSpider(scrapy.Spider):
    name = "Tongcheng"
    allowed_domains = ["bj.58.com"]
    start_urls = ["https://bj.58.com/huangyezonghe/?key=unity"]

    def parse(self, response):
        
        # with open("tongcheng.html","w",encoding = 'utf-8') as f:
        #     f.write(response.text)
        
        res_List = response.xpath("//div[@class='sousuo']//dt/a")

        print("————————————————————————————————————")
        print(res_List.extract())
