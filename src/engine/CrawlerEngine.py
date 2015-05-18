import os
from threading import Thread

from scrapy.crawler import Crawler
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.settings import Settings
from scrapy.selector import Selector
from twisted.internet import reactor
from .search_engine.SearchEngine import SearchEngine
from .db_engine.DbEngine import DbEngine
from nlp import extractor


class CrawlerEngine(object):
    db_engine = DbEngine()
    search_engine = SearchEngine()

    def add_query(self, user, query):
        keywords = extractor.keywords(query)
        self.db_engine.add_query(user, query)
        self.db_engine.add_keywords(keywords)
        self.search_engine.reload_keywords()
        self.start_crawling()

    def get_queries(self, user):
        return self.db_engine.get_queries(user)

    def get_urls(self, keywords):
        return self.db_engine.get_urls(keywords)

    def start_crawling(self):
        if not reactor.running:
            settings = Settings()
            crawler = Crawler(settings)
            crawler.configure()
            crawler.crawl(self.CustomSpider())
            crawler.start()
            Thread(target=reactor.run, args=(False,)).start()

    class CustomSpider(CrawlSpider):
        name = "spider"
        config_path = os.path.join(os.path.dirname(__file__), "conf.crawler")
        with open(config_path) as config_file:
            config = eval(config_file.read())
            allowed_domains = [config["allowed_domains"]]
            start_urls = [config["start_urls"]]

        rules = (
            Rule(
                SgmlLinkExtractor(), callback='parse_page', follow=True
            ),
        )

        @staticmethod
        def parse_page(response):
            text = ''.join(Selector(response).xpath(
                "//body/descendant-or-self::*[not(self::script)]/text()").
                extract()).strip()
            url = response.url
            CrawlerEngine.search_engine.search_in_url(url, text)






