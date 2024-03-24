import scrapy


class BaiduSpider(scrapy.Spider):
    #爬虫的名字 用于运行爬虫的时候 使用的值
    name = "Baidu"
    #允许访问的域名：也就是说，这个程序只能访问百度的网站，其他网站并不能被打开
    allowed_domains = ["www.baidu.com"]
    #起始的url地址，指的是第一次要访问的域名
    #下面的start_urls 是在没有添加http的allowed_domains前面添加一个http
                    # 在allowed_domains的后面添加一个/（旧版，现在已经更新，之后不会添加/）
    start_urls = ["http://www.baidu.com"]

    def parse(self, response):
        print("Hello world")
