import scrapy


class SportteryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    phone = scrapy.Field()
    city = scrapy.Field()
    province = scrapy.Field()
    address = scrapy.Field()
    lat = scrapy.Field()
    lng = scrapy.Field()
    mainname = scrapy.Field()
    topic = scrapy.Field()
    tag = scrapy.Field()
    name = scrapy.Field()
    officialurl = scrapy.Field()
    microblog = scrapy.Field()
    category = scrapy.Field()
    MapType = scrapy.Field()
