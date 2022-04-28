import scrapy
from ..items import ScrapingItem


class RosblatSpider(scrapy.Spider):
    name = 'rosbalt'
    allowed_domains = ['m.rosbalt.ru']
    start_urls = ['https://m.rosbalt.ru']

    def parse(self, response):
        item = ScrapingItem()
        content = response.xpath('//a[@class="hero"]')
        for article_link in content:
            item['article_url'] = article_link.xpath('.//@href').extract_first()
            if item['article_url'].startswith("http"):
                continue
            item['article_url'] = "https://m.rosbalt.ru" + item['article_url']
            print(item['article_url'])
            yield (item)
