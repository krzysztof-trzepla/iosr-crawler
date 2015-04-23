from scrapy.crawler import Crawler
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.settings import Settings
from twisted.internet import reactor
from bs4 import BeautifulSoup
from ..searchEngine.SearchEngine import SearchEngine


class IOSRCrawler():

    def __init__(self):
        self.searchEngine = SearchEngine()
        self.spider = ConfigurableSpider().setSearchEngine(self.searchEngine)


    def startCrawling(self):
        settings = Settings()
        crawler = Crawler(settings)
        crawler.configure()
        crawler.crawl(self.spider)
        crawler.start()
        reactor.run()

    def addRequestedPhrase(self, requestedPhrase):
        self.searchEngine.addPhraseToSearch(requestedPhrase)

class ConfigurableSpider(CrawlSpider):

    name = "wiki_spider"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Programming_language"]
    rules = (
        Rule(
            SgmlLinkExtractor(allow_domains=("en.wikipedia.org",)),
            callback='parse_page', follow=True
        ),
    )

    def setSearchEngine(self, searchEngine):
        self.searchEngine = searchEngine
        return self

    def parse_page(self, response):
        soup = BeautifulSoup(response.body, from_encoding="utf-8")
        textToSearch = soup.get_text()
        results = self.searchEngine.search(textToSearch)
        for result in results:
           #TODO save in database
           print result + "  on url: " + response.url










