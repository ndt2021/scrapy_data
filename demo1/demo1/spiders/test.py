import scrapy

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.vietnamplus.vn']
    start_urls = ['https://www.vietnamplus.vn/cho-doi-gi-o-hai-tran-thuc-chien-dau-tien-cua-huan-luyen-vien-troussier-post907883.vnp']

    def parse(self, response):
        # Trích xuất tiêu đề bài viết
        title = response.xpath('/html/body/div[2]/div/div[3]/h1/text()').get()

        # Trích xuất tác giả
        author = response.css('body > div.site-body > div > div.article > div.article__meta > span::text').get()

        # Trích xuất nội dung từ tất cả các thẻ <p>
        paragraphs = response.xpath('//p/text()').getall()

        # Kết hợp các đoạn văn thành một chuỗi
        content = '\n'.join(paragraphs)

        # In ra thông tin để kiểm tra
        self.log(f'Title: {title}, Author: {author}')
        self.log(f'Content: {content}')

        # Ghi dữ liệu vào file văn bản (txt)
        with open('output.txt', 'w', encoding='utf-8') as file:
            file.write(f'Title: {title}\nAuthor: {author}\n\nContent:\n{content}')