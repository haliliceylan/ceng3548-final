import scrapy
from scrapy_crawler.items import BlogSiteData

class BloglistmeSpider(scrapy.Spider):

    name = 'BlogListMe'
    allowed_domains = ['bloglist.me']
    start_urls = ['https://bloglist.me/directory//']
    
    def parse(self, response):
        for blog_site_addres in response.css('.directorist-col-4').css('a::attr(href)').re('^(?!https://bloglist\.me).\S+'):
            yield scrapy.Request(url=blog_site_addres, callback=self.parse)
            yield BlogSiteData({
                "url": blog_site_addres,
                "is_blog": 1
            })
        yield response.follow(response.css("a.next::attr(href)").get(), callback=self.parse)