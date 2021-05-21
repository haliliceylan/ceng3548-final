from scrapy_crawler.sitemap import SitemapSpider
from scrapy_crawler.items import BlogSiteData

class NonBlogsitemapSpider(SitemapSpider):
    name = 'NonBlogSitemap'
    sitemap_urls = [
        "https://www.1001oyun.com/",
        "https://www.kraloyun.com/",
        "https://www.oyunskor.com/",
        "https://games.aarp.org/",
        "https://www.rhiannonnavin.com/",
        "https://www.ximenavengoechea.com/",
        "https://www.orestisgeorgiou.com/",
    ]

    def parse(self, loc):
        return BlogSiteData({
            "url": loc,
            "is_blog": 0
        })

