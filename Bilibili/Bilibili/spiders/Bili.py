import scrapy


class BiliSpider(scrapy.Spider):
    name = "Bili"
    allowed_domains = ["www.bilibili.com"]
    start_urls = ["https://www.bilibili.com/v/popular/all/"]

    #爬取B站热门在榜视频封面、标题、up名字、播放量
    def parse(self, response):
        print("——————————————————————————————————————————————————————————————")
        with open("b.html","w",encoding = "utf-8") as f:
            f.write(response.body.decode("utf-8"))
        
        # print(response.status)

        # b = response.body.decode("utf-8")
        # print(b)
        video_list = response.xpath("//ul[@class='card-list']/div[@class='video-card']")
        print(video_list)

        print("——————————————————————————————————————————————————————————————")

    