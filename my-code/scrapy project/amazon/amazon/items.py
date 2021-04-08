# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    prod_name = scrapy.Field()
    price = scrapy.Field()
    old_price = scrapy.Field()
    price_ml = scrapy.Field()
    stars = scrapy.Field()
    reviews = scrapy.Field()
    delivery_date = scrapy.Field()
