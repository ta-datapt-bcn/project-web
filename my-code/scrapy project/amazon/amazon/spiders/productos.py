import scrapy


class ProductosSpider(scrapy.Spider):
    name = 'productos'
    allowed_domains = ['amazon.es']
    # Url of the HairCare Products section of Amazon Spain, with "professional" typed into the search box
    start_urls = ['https://www.amazon.es/s?k=profesional&rh=n%3A4347699031&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss']

    def parse(self, response):
        # Obtaining a list of products by selecting them by class with xpath
        products = response.xpath("//div[@class='sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20']")
        # Iterating over the list to create a dictionary for every product
        for product in products:
            yield {
                'prod_name':product.xpath(".//span[@class='a-size-base-plus a-color-base a-text-normal']/text()").get(default=None),
                'price_whole':product.xpath(".//span[@class='a-price-whole']/text()").get(default=None),
                'price_bulk':product.xpath(".//span[@class='a-size-base a-color-secondary']/text()").get(default=None),
                'price_old':product.xpath(".//span[@class='a-price a-text-price']/span/text()").get(default=None),
                'stars':product.xpath(".//span[@class='a-icon-alt']/text()").get(default=None),
                'reviews':product.xpath(".//span[@class='a-size-base']/text()").get(default=None),
                'delivery_date':product.xpath(".//span[@class='a-text-bold']/text()").get(default=None)
            }

        # Changing to the next page when there are no more products to scrape
        next_page = response.xpath("//li[@class='a-last']/a/@href").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)