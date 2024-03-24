# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#需要获取的变量类型
class DpagedownItem(scrapy.Item):
    
    img = scrapy.Field()

    name = scrapy.Field()

    price = scrapy.Field()