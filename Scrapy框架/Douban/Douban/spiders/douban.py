import scrapy


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com"]

    def parse(self, response):
        print("访问成功")
        # content = response.text
        # with open("douban.html","w",encoding = "utf-8") as f:
        #     f.write(content)
