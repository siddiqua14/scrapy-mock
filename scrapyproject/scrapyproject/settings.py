# Scrapy settings for scrapyproject project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os
BOT_NAME = "scrapyproject"

SPIDER_MODULES = ["scrapyproject.spiders"]
NEWSPIDER_MODULE = "scrapyproject.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "scrapyproject (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


# Set settings whose default value is deprecated to a future-proof value
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
ITEM_PIPELINES = {
    'scrapyproject.pipelines.ScrapyprojectPipeline': 300,
    'scrapyproject.pipelines.ScrapyprojectPipeline': 200,
}
# Set the folder to store images in your local system
IMAGES_STORE = 'images'

# Configure the image URL to be used for downloading
IMAGES_URLS_FIELD = 'Image'

# Configure database URL from environment variable (configured in docker-compose)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://scraper_user:scraper_password@localhost:5432/scraper_db")