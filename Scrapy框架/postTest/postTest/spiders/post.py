import scrapy


class PostSpider(scrapy.Spider):
    name = "post"
    allowed_domains = ["fanyi.baidu.com"]
    #如果是post请求，且没有参数，那么这个start_urls将没有意义
    # start_urls = ["https://fanyi.baidu.com/?aldtype=16047#en/zh/final"]

    # def parse(self, response):
        
#因此我们要重新定义一下
def start_requests(self):
    url = "https://fanyi.baidu.com/sug"

    data = {
        # "query":"final"
        # "from": "en",
        # "to": "zh",
        # "query": "final",
        # "simple_means_flag": "3",
        # "sign": "269003.63994",
        # "token": "67c26fd59098ade1dd552e591573739c",
        # "domain": "common",
        # "ts": "1701235090318",
        # "kw":"final"
        "kw": "final"
    }

    yield scrapy.FormRequest(url = url,formdata = data,callback = parse_second)
import json
def parse_second(self,response):
    print("+++++++++++++++++++++++++++++")
    content = response.text
    obj = json.loads(content,enconding = "utf-8")
    print(obj) 