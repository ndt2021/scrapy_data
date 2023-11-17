# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BaomoiItem(scrapy.Item):
    title = scrapy.Field()
    sapo = scrapy.Field()
    body = scrapy.Field()
    author = scrapy.Field()
    category = scrapy.Field()
    publish_date = scrapy.Field()
    avatar = scrapy.Field()
    tag = scrapy.Field()
    news_relation = scrapy.Field()
