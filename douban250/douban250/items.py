# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Douban250Item(scrapy.Item):

    link = scrapy.Field()
    title = scrapy.Field()
    director = scrapy.Field()
    type = scrapy.Field()
    date = scrapy.Field()
    time_long = scrapy.Field()
    score = scrapy.Field()
    comment = scrapy.Field()
    # country = scrapy.Field()
    # actors = scrapy.Field()




