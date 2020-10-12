# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy import signals
from scrapy.exporters import CsvItemExporter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
import csv
import json

class BlogPipeline(object):
    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        self.file = open('scraped_items.json', 'w')
        # Your scraped items will be saved in the file 'scraped_items.json'.
        # You can change the filename to whatever you want.
        self.file.write("[")

    def spider_closed(self, spider):
        self.file.write("]")
        self.file.close()
        file.close()

    def process_item(self, item, spider):
        line = json.dumps(
            dict(item),
            indent = 4,
            sort_keys = True,
            separators = (',', ': ')
        ) + ",\n"
        self.file.write(line)
        return item