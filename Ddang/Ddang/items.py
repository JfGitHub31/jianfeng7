# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DdangItem(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()
    publish = scrapy.Field()
    comment = scrapy.Field()
    price = scrapy.Field()
    pass
