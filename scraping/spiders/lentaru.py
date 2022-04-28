import scrapy
from ..items import ScrapingItem


class LentaruSpider(scrapy.Spider):
    name = 'lentaru'
    allowed_domains = ['m.lenta.ru']
    start_urls = ['https://m.lenta.ru/rubrics/russia']

    def parse(self, response):
        item = ScrapingItem()
        content = response.xpath('//li[@class="tabloid__item _mini"]')
        for article_link in content.xpath('./a'):
            item['article_url'] = article_link.xpath('.//@href').extract_first()
            if item['article_url'].startswith("http"):
                continue
            item['article_url'] = "https://m.lenta.ru"+item['article_url']
            print(item['article_url'])
            yield (item)

