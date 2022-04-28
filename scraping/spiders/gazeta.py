import scrapy
from ..items import ScrapingItem


class GazetaSpider(scrapy.Spider):
    name = 'gazeta'
    allowed_domains = ['m.gazeta.ru']
    start_urls = ['http://m.gazeta.ru/']

    def parse(self, response):
        item = ScrapingItem()
        content = response.xpath('//div[@class="b_ear-title"]')
        for article_link in content.xpath('./a'):
            item['article_url'] = article_link.xpath('.//@href').extract_first()
            if item['article_url'].startswith("http"):
                continue
            item['article_url'] = "https://m.gazeta.ru/" + item['article_url']
            print(item['article_url'])
            yield (item)
