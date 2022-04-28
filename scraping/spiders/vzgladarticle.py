import hashlib
import json

import scrapy
from scrapy.http import Request

from ..items import ScrapingItem


class VzgladarticleSpider(scrapy.Spider):
    name = 'vzgladarticle'

    def start_requests(self):
        data = []
        with open('vzglad.json') as json_file:
            data = json.load(json_file)
        for link_url in data:
            request = Request(link_url['article_url'], callback=self.parse)
            yield request

    def parse(self, response):
        item = ScrapingItem()
        news_body = ""
        item['article_link'] = response.url
        item['article_uuid'] = hashlib.sha256(str(response.url).encode('utf-8')).hexdigest()
        item['article_id'] = response.url.split("/")[-1]
        item['article_text'] = "\n".join(response.xpath('//div[@class="text newtext"]/p/text()').extract())
        item['article_title'] = response.xpath('//div[@class="text newtext"]/p/b/text()').extract()
        yield (item)

