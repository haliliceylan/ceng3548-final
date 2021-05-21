# Scrapy settings for scrapy_crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_crawler'

SPIDER_MODULES = ['scrapy_crawler.spiders']
NEWSPIDER_MODULE = 'scrapy_crawler.spiders'


FEEDS = {
    'data/items.csv': {
       'format': 'csv',
       'fields': ['url', 'is_blog', 'qty_dot_url', 'qty_hyphen_url', 'qty_underline_url', 'qty_slash_url', 'qty_questionmark_url', 'qty_equal_url', 'qty_at_url', 'qty_and_url', 'qty_exclamation_url', 'qty_space_url', 'qty_tilde_url', 'qty_comma_url', 'qty_plus_url', 'qty_asterisk_url', 'qty_hashtag_url', 'qty_dollar_url', 'qty_percent_url', 'length_url', 'email_in_url', 'qty_dot_domain', 'qty_hyphen_domain', 'qty_underline_domain', 'qty_slash_domain', 'qty_questionmark_domain', 'qty_equal_domain', 'qty_at_domain', 'qty_and_domain', 'qty_exclamation_domain', 'qty_space_domain', 'qty_tilde_domain', 'qty_comma_domain', 'qty_plus_domain', 'qty_asterisk_domain', 'qty_hashtag_domain', 'qty_dollar_domain', 'qty_percent_domain', 'length_domain', 'in_ip_domain', 'server_client_domain', 'qty_dot_path', 'qty_hyphen_path', 'qty_underline_path', 'qty_slash_path', 'qty_questionmark_path', 'qty_equal_path', 'qty_at_path', 'qty_and_path', 'qty_exclamation_path', 'qty_space_path', 'qty_tilde_path', 'qty_comma_path', 'qty_plus_path', 'qty_asterisk_path', 'qty_hashtag_path', 'qty_dollar_path', 'qty_percent_path', 'length_path', 'qty_dot_query', 'qty_hyphen_query', 'qty_underline_query', 'qty_slash_query', 'qty_questionmark_query', 'qty_equal_query', 'qty_at_query', 'qty_and_query', 'qty_exclamation_query', 'qty_space_query', 'qty_tilde_query', 'qty_comma_query', 'qty_plus_query', 'qty_asterisk_query', 'qty_hashtag_query', 'qty_dollar_query', 'qty_percent_query', 'length_query', 'qty_elements_query', 'tdl_present_query', 'qty_dot_fragment', 'qty_hyphen_fragment', 'qty_underline_fragment', 'qty_slash_fragment', 'qty_questionmark_fragment', 'qty_equal_fragment', 'qty_at_fragment', 'qty_and_fragment', 'qty_exclamation_fragment', 'qty_space_fragment', 'qty_tilde_fragment', 'qty_comma_fragment', 'qty_plus_fragment', 'qty_asterisk_fragment', 'qty_hashtag_fragment', 'qty_dollar_fragment', 'qty_percent_fragment', 'length_fragment'],
    },
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_crawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapy_crawler.middlewares.ScrapyCrawlerSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy_crawler.middlewares.ScrapyCrawlerDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'scrapy_crawler.pipelines.InternalMetricPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
