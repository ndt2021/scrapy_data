import datetime

import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.vietnamplus.vn']

    start_urls = ['https: // www.vietnamplus.vn /']

    x=0

    def start_requests(self):
        # Trong phương thức này, self là một tham chiếu đến đối tượng Spider hiện tại (được tạo từ lớp MySpider)
        # self.start_urls là danh sách các URL khởi đầu được đặt trong thuộc tính start_urls của đối tượng Spider
        link =[
        'https://www.vietnamplus.vn/topic/75-nam-bac-ho-ra-loi-keu-goi-thi-dua-ai-quoc-1204.vnp',
'https://www.vietnamplus.vn/thu-tuong-chinh-phu-tao-moi-dieu-kien-thuan-loi-nhat-cho-doi-moi-sang-tao-post910005.vnp',
'https://www.vietnamplus.vn/thu-tuong-chinh-phu-tao-moi-dieu-kien-thuan-loi-nhat-cho-doi-moi-sang-tao-post910005.vnp',
'https://www.vietnamplus.vn/tai-nang-khoi-nghiep-doi-moi-sang-tao-buyo-bioplastics-gianh-giai-nhat-post909883.vnp',
'https://www.vietnamplus.vn/khai-mac-trien-lam-san-pham-dich-vu-khoi-nghiep-doi-moi-sang-tao-post909780.vnp',
'https://www.vietnamplus.vn/xanh-hoa-nganh-det-may-doanh-nghiep-viet-phai-co-dinh-huong-chien-luoc-ro-rang-post910026.vnp',
'https://www.vietnamplus.vn/di-tim-loi-giai-cho-bai-toan-phat-huy-gia-tri-tuong-trong-doi-song-hien-dai-post910004.vnp',
'https://www.vietnamplus.vn/canh-bao-gio-manh-song-lon-tren-nhieu-vung-bien-cua-ca-nuoc-post909994.vnp',
'https://www.vietnamplus.vn/canh-bao-gio-manh-song-lon-tren-nhieu-vung-bien-cua-ca-nuoc-post909994.vnp',
'https://www.vietnamplus.vn/con-nhieu-su-kien-dien-ra-lon-xon-mat-my-quan-o-khu-ven-ho-hoan-kiem-post910019.vnp',
'https://www.vietnamplus.vn/con-nhieu-su-kien-dien-ra-lon-xon-mat-my-quan-o-khu-ven-ho-hoan-kiem-post910019.vnp',
'https://www.vietnamplus.vn/phat-trien-quan-he-voi-trung-quoc-la-lua-chon-chien-luoc-lau-dai-cua-viet-nam-post910022.vnp',
'https://www.vietnamplus.vn/phat-trien-quan-he-voi-trung-quoc-la-lua-chon-chien-luoc-lau-dai-cua-viet-nam-post910022.vnp',
'https://www.vietnamplus.vn/topic/tin-moi-nhan-111.vnp',
'https://www.vietnamplus.vn/quang-ninh-nam-hoc-sinh-o-van-don-nghi-ngo-doc-sau-khi-an-keo-la-post910021.vnp',
'https://www.vietnamplus.vn/nhieu-bat-cap-trong-kiem-soat-hoat-dong-khai-thac-thuy-san-tai-cang-ca-post910023.vnp',
'https://www.vietnamplus.vn/tin-nong-2511-ban-bi-thu-yeu-cau-khong-tham-hoi-chuc-tet-lanh-dao-post910012.vnp',
'https://www.vietnamplus.vn/phu-nu-hay-len-tieng-khi-bi-bao-luc-hoac-nhin-thay-bao-luc-post909999.vnp',
'https://www.vietnamplus.vn/ha-noi-di-doi-6-ho-dan-ra-khoi-khu-vuc-sut-lun-tai-huyen-quoc-oai-post909997.vnp'
    ]
        for url in link:
            print("BAI SO--------------------------------------------------------------------------------------------------------------------------------------" )
            # self.x=self.x+1
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
            file.write(f'\n\n\n\n\n\n\n\n\n\n\n'
                       f'______________________________________________________________________________________________________'
                       f'Title: {title}\n'
                       f'Author: {author}\n\n'
                       f'Date: {publish_date}\n\n'
                       f'Sapo: {sapo}\n\n\n'
                       f'Category: {category}\n\n\n'
                       # f'url_avatar: {avatar}\n\n\n'
                       f'Tag: {allTag}\n\n\n\n'
                       f'Content:\n{content}\n\n')
