import scrapy
from demo1.items import BaomoiItem

class BaomoiSpider(scrapy.Spider):
    name = "baomoi"
    allowed_domains = ["baomoi.com"]
    start_urls = ["https://baomoi.com/"]

    def parse(self, response):
        # Lấy danh sách các bài viết từ trang chủ
        article_links = response.xpath('//h4/a/@href').extract()
        # Duyệt qua từng bài viết để lấy thông tin chi tiết
        for link in article_links:
            yield scrapy.Request(link, callback=self.parse_article)

    def parse_article(self, response):
        # Trích xuất thông tin từ trang bài viết chi tiết
        item = BaomoiItem()

        title = response.xpath('//*[@id="__next"]/div[3]/div/div/div[2]/div[1]/div[1]/div[1]/h1').get()
        self.log(f'Title: {title}')

        item['title'] = response.css('a::attr(title)').get()
        item['sapo'] = response.xpath('//p[@class="sapo"]/text()').get()
        item['body'] = response.xpath('//div[@class="body"]/text()').get()
        item['author'] = response.xpath('//span[@class="author"]/text()').get()
        item['category'] = response.xpath('//span[@class="category"]/text()').get()
        item['publish_date'] = response.xpath('//span[@class="publish-date"]/text()').get()
        item['avatar'] = response.xpath('//img/@src').get()
        item['tag'] = response.xpath('//div[@class="tags"]/a/text()').getall()
        item['news_relation'] = response.xpath('//div[@class="related-news"]/a/@href').getall()

        yield item


        # In ra thông tin để kiểm tra
        self.log(f'Title: {item["title"]}, Author: {item["author"]}, Category: {item["category"]}')