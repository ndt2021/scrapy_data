import scrapy
import re

class VietnamplusSpider(scrapy.Spider):
    name = "vietnamplus"
    allowed_domains = ["www.vietnamplus.vn"]
    start_urls = ["https://www.vietnamplus.vn/"]

    def parse(self, response):
        # Trích xuất tất cả các liên kết trên trang
        all_links = response.css('a::attr(href)').getall()

        # Lọc chỉ các liên kết HTTP và thuộc về bài báo bên trong trang Vietnamplus
        article_links = [link for link in all_links if re.match(r'^https://www\.vietnamplus\.vn/', link)]

        # In giá trị của article_links để kiểm tra
        self.log(f'Article Links: {article_links}')

        # Mở hoặc tạo file để lưu các liên kết bài viết
        with open('article_links.txt', 'w', encoding='utf-8') as file:
            # Lưu từng liên kết vào file
            for article_link in article_links:
                file.write(article_link + '\n')

        # Duyệt qua từng liên kết bài viết và gửi yêu cầu đến đó để quét
        for article_link in article_links:
            if isinstance(article_link, str):
                yield scrapy.Request(article_link, callback=self.parse_article)

     # def parse_article(self, response):
     #    # Tương tự như parse, bạn có thể trích xuất thông tin từ trang bài viết chi tiết ở đây
     #    title = response.xpath('/html/body/div[2]/div/div[3]/h1/text()').get()
     #    author = response.css('body > div.site-body > div > div.article > div.article__meta > span::text').get()
     #    paragraphs = response.xpath('//p/text()').getall()
     #    content = '\n'.join(paragraphs)
     #
     #    # In ra thông tin để kiểm tra
     #    self.log(f'Title: {title}, Author: {author}')
     #    self.log(f'Content: {content}')

        # Ghi dữ liệu vào file văn bản (txt)
        # with open('output.txt', 'a', encoding='utf-8') as file:
        #     file.write(f'Title: {title}\nAuthor: {author}\n\nContent:\n{content}\n\n')
    #     pass