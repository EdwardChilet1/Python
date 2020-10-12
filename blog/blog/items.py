# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BlogItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #Info de blog
    titulo = scrapy.Field()
    tipo = scrapy.Field()

    #Info especial de cada blog
    imagen = scrapy.Field()
    hipervinculo = scrapy.Field() 
    texto = scrapy.Field()

    pass
