# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SfItem(scrapy.Item):
    chaper_name = scrapy.Field()
    chaper_text = scrapy.Field()
    book_Name = scrapy.Field()
