import scrapy


class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["car.autohome.com.cn"]
    start_urls = ["https://car.autohome.com.cn/price/brand-15.html"]

    def parse(self, response):
        content =  response.xpath("//div[@class='list-cont-main']//a[@class='font-bold']/text()")
        print("————————————————————————————————————————————————————————————————")
        print(content.extract())
