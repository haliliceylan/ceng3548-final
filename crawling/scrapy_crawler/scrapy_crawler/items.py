# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BlogSiteData(scrapy.Item):
    url = scrapy.Field()
    is_blog = scrapy.Field(serializer=int)
