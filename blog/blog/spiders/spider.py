import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from blog.items import BlogItem

class BlogSpider(CrawlSpider):
    name='Blog'
    item_count = 0
    allowed_domain= ['https://www.sise.edu.pe/']
    start_urls= ['https://www.sise.edu.pe/blogs']
    rules = {
       Rule(LinkExtractor(allow=(),restrict_xpaths=('//ul[@class="pager__items js-pager__items"]/li/a'))),
       Rule(LinkExtractor(allow=(),restrict_xpaths=('//div[@class="title-left"]//h3//a')),
                            callback='parse_item',follow=False)
    }

    def parse_item(self,response):
        bl_item = BlogItem()

        #titulo
        bl_item['titulo'] = response.xpath('//div[@class="title-top hidden-xs"]/h3/span[@property="schema:name"]/text()').extract()
        bl_item['imagen'] =  response.xpath('//div[@class="img-top"]/img/@src').extract()
        bl_item['texto'] = ", ".join(response.xpath('//div[@property="schema:text"]/p').extract())
        bl_item['hipervinculo'] = ", ".join(response.xpath('//div[@property="schema:text"]/p/a/@href').extract())
        self.item_count +=1
        if self.item_count >200:
            raise CloseSpider('item_exceeded')
        yield bl_item


        