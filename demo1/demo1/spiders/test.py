import datetime

import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.vietnamplus.vn']

    start_urls = ['https: // www.vietnamplus.vn /']

    def start_requests(self):
        # Trong phương thức này, self là một tham chiếu đến đối tượng Spider hiện tại (được tạo từ lớp MySpider)
        # self.start_urls là danh sách các URL khởi đầu được đặt trong thuộc tính start_urls của đối tượng Spider
        link =[
        'https://www.vietnamplus.vn/giuong-cao-ngon-co-dai-doan-ket-toan-dan-toc-xay-dung-dat-nuoc-giau-manh-post908585.vnp',
        'https://www.vietnamplus.vn/cho-doi-gi-o-hai-tran-thuc-chien-dau-tien-cua-huan-luyen-vien-troussier-post907883.vnp',
        'https://www.vietnamplus.vn/kinhte/batdongsan/',
        'https://www.vietnamplus.vn/kinhte/thong-cao-bao-chi/'
    ]
        for url in link:
            yield scrapy.Request(url, callback=self.parse)
    def parse(self, response):
        # Trích xuất tiêu đề bài viết
        title = response.xpath('/html/body/div[2]/div/div[3]/h1/text()').get()

        # Trích xuất tác giả
        author = response.css('body > div.site-body > div > div.article > div.article__meta > span::text').get()

        # Publish Date: Ngày và giờ mà tin tức được công bố hoặc đăng tải lên trang web.
        publish_date = response.css(
            'body > div.site-body > div > div.article > div.article__meta > time::text').extract_first()

        # sapo
        # sapo = response.xpath('/html/body/div[2]/div/div[3]/div[1]/p').get()
        sapo = response.css('body > div.site-body > div > div.article > div.article__sapo.cms-desc> p::text').get()

        #category
        category = response.css('body > div.site-body > div > div.breadcrumb.breadcrumb-detail > h2:nth-child(1) > a::text').get()

        # avatar
        # avatar = response.css('body > div.site-body > div > div.article > div.col > div.main-col.content-col > figure > img::attr(src)::text').get()

        # Tag
        tags = response.css('div.article__tag a::text').getall()

        allTag = '\n'.join(tags)

        # Trích xuất nội dung từ tất cả các thẻ <p>
        paragraphs = response.xpath('//p/text()').getall()

        # Kết hợp các đoạn văn thành một chuỗi
        content = '\n'.join(paragraphs)

        # In ra thông tin để kiểm tra
        self.log(f'Title: {title}, Author: {author}')
        self.log(f'Publish date: {publish_date}')
        self.log(f'Sapo: {sapo}')
        self.log(f'Category: {category}')
        # self.log(f'avatar {avatar}')
        self.log(f'Tag: {allTag}')

        self.log(f'Content: {content}')
        # Ghi dữ liệu vào file văn bản (txt)
        with open('output.txt', 'a', encoding='utf-8') as file:
            file.write(f'Title: {title}\n'
                       f'Author: {author}\n\n'
                       f'Date: {publish_date}\n\n'
                       f'Sapo: {sapo}\n\n\n'
                       f'Category: {category}\n\n\n'
                       # f'url_avatar: {avatar}\n\n\n'
                       f'Tag: {allTag}\n\n\n\n'
                       f'Content:\n{content}\n\n')
