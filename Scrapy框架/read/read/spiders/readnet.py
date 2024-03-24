import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from read.items import ReadItem

class ReadnetSpider(CrawlSpider):
    name = "readnet"
    allowed_domains = ["www.dushu.com"]
    start_urls = ["https://www.dushu.com/book/1005.html"]

    rules = (
        Rule(LinkExtractor(
                            allow=r"/book/1005_\d+.html"), 
                            callback="parse_item",
                             follow=True),)

    def parse_item(self, response):
        
        list_img = response.xpath("//div[@class='bookslist']/ul/li//img")

        # list_src = response.xpath("//div[@class = 'bookslist']/ul/li//i")

        for img in list_img:
            name = img.xpath("./@alt").extract_first()
            src = img.xpath("./@data-original").extract_first()

            book = ReadItem(name = name,src = src)
            yield book

        
