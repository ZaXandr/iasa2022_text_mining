import scrapy
from ..items import ScrapingItem


class VzgladSpider(scrapy.Spider):
    name = 'vzglad'
    allowed_domains = ['m.vz.ru']
    start_urls = ['https://m.vz.ru/']

    def parse(self, response):
        item = ScrapingItem()
        content = response.xpath('//div[@class = "othnews"]/h4')
        for article_link in content.xpath('./a'):
            item['article_url'] = article_link.xpath('.//@href').extract_first()
            if item['article_url'].startswith("http"):
                continue
            item['article_url'] = "https://m.vz.ru/" + item['article_url']
            print(item['article_url'])
            yield (item)

