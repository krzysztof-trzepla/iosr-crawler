from scrapy.crawler import Crawler
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.settings import Settings
from scrapy.selector import Selector
from twisted.internet import reactor
from search_engine.SearchEngine import SearchEngine
import os
from threading import Thread



class CrawlerEngine:
    searchEngine = SearchEngine()

    def __init__(self):
        pass

    def addRequest(self, phrase):
        self.searchEngine.add_phrase(phrase)
        self.searchEngine.save_phrases_list_to_db()

    def start_crawling(self):
        if not reactor.running:
            settings = Settings()
            crawler = Crawler(settings)
            crawler.configure()
            crawler.crawl(self.CustomSpider())
            crawler.start()
            Thread(target=reactor.run, args=(False,)).start()

    class CustomSpider(CrawlSpider):

        name = "iosr_spider"
        allowed_domains = [eval(open(os.path.join(os.path.dirname(__file__), "conf.crawler")).read())["allowed_domains"]]
        start_urls = [eval(open(os.path.join(os.path.dirname(__file__), "conf.crawler")).read())["start_urls"]]
        rules = (
            Rule(
                SgmlLinkExtractor(),  callback='parse_page', follow=True
            ),
        )

        def parse_page(self, response):
            # geting plain text from excluding scripts
            text = ''.join(Selector(response).xpath("//body/descendant-or-self::*[not(self::script)]/text()").extract()).strip()
            url = response.url
            CrawlerEngine.searchEngine.search_in_url(url, text)






