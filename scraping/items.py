# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapingItem(scrapy.Item):
    article_url = scrapy.Field()
    article_link = scrapy.Field()
    article_uuid = scrapy.Field()
    article_id = scrapy.Field()
    article_text = scrapy.Field()
    article_title = scrapy.Field()
