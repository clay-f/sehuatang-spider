# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SehuaItem(scrapy.Item):
    author = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()