import scrapy
from demo1.items import BaomoiItem

class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["baomoi.com"]
    start_urls = ["https://baomoi.com/rut-ngan-thoi-gian-dieu-hanh-gia-xang-dau-xuong-7-ngay/c/47560544.epi"]

    def parse(self, response):
        item = BaomoiItem()

        # Trích xuất thông tin cần thiết từ trang bài viết chi tiết
        item['title'] = response.xpath('//h1/text()').get()
        item['author'] = response.xpath('//*[@id="__next"]/div[3]/div/div/div[2]/div[1]/div[1]/div[1]/div[4]/p[24]/strong').get()
        item['link'] = response.url

        yield item

        # In ra thông tin để kiểm tra
        self.log(f'Title: {item["title"]}, Author: {item["author"]}, Link: {item["link"]}')
