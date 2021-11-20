import scrapy
from scrapy.loader.processors import TakeFirst


class QuotesSpiderItem(scrapy.Item):
    title = scrapy.Field(output_processor=TakeFirst())
    movie_name = scrapy.Field(output_processor=TakeFirst())
    actress = scrapy.Field(output_processor=TakeFirst())
    mosaic = scrapy.Field(output_processor=TakeFirst())
    size = scrapy.Field(output_processor=TakeFirst())
    torrents = scrapy.Field(output_processor=TakeFirst())
    magnets = scrapy.Field(output_processor=TakeFirst())
    link = scrapy.Field(output_processor=TakeFirst())
