import scrapy
from scrapyproject.items import ProductItem

class ScraperSpider(scrapy.Spider):
    name = "scraper"
    allowed_domains = ["www.scrapingcourse.com"]
    start_urls = ["https://www.scrapingcourse.com/ecommerce/"]

    def parse(self, response):
        # Get all HTML product elements
        products = response.css("li.product")

        for product in products:
            item = ProductItem()
            item['name'] = product.css("h2::text").get()
            item['image_url'] = response.urljoin(product.css("img::attr(src)").get())
            item['price'] = "".join(product.css(".price *::text").getall())
            item['url'] = response.urljoin(product.css("a::attr(href)").get())
            yield item
