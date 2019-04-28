# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BosszhipinItem(scrapy.Item):
    pass
    skill = scrapy.Field()
    nature = scrapy.Field()
    company = scrapy.Field()
    salary = scrapy.Field()
    job = scrapy.Field()
    exp = scrapy.Field()

