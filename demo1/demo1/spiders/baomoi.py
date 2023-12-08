import scrapy
from demo1.items import BaomoiItem

class BaomoiSpider(scrapy.Spider):
    name = "baomoi"
    allowed_domains = ["baomoi.com"]
    start_urls = ["https://baomoi.com/"]

    def parse(self, response):
        # Trích xuất tất cả các liên kết trên trang
        all_links = response.css('a::attr(href)').getall()
        # Mở hoặc tạo file để lưu các liên kết bài viết
        with open('article_links.txt', 'a', encoding='utf-8') as file:
            # Lưu từng liên kết vào file
            for link in all_links:
                file.write(link + '\n')