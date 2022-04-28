import scrapy
from ..items import ScrapingItem


class TvzvezdaSpider(scrapy.Spider):
    name = 'tvzvezda'
    allowed_domains = ['m.tvzvezda.ru']
    start_urls = ['https://m.tvzvezda.ru/']

    def parse(self, response):
        item = ScrapingItem()
        content = response.xpath('//article[@class="images_news"]')
        for article_link in content.xpath('./a'):
            item['article_url'] = article_link.xpath('.//@href').extract_first()
            if item['article_url'].startswith("http"):
                continue
            item['article_url'] = "https://m.tvzvezda.ru" + item['article_url']
            print(item['article_url'])
            yield (item)
