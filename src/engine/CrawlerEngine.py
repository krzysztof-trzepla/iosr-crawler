import os
import logging
import requests
from threading import Thread

from django.conf import settings
from scrapy.crawler import Crawler
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.settings import Settings
from bs4 import BeautifulSoup
from twisted.internet import reactor
from .search_engine.SearchEngine import SearchEngine
from .db_engine.DbEngine import DbEngine
from nlp.extractor import NLPExtractor

logger = logging.getLogger(__name__)


class CrawlerEngine(object):
    def __init__(self):
        self.db_engine = DbEngine()
        self.search_engine = SearchEngine()
        self.extractor = NLPExtractor()

    def add_query(self, user_id, query):
        """
        Add crawling query for given user.

        :param int user_id: ID of user associated with the query.
        :param str query: User's query.
        """

        keywords = self.extractor.run(query)
        logger.info("Found following keywords for query '{0}': '{1}'".
                    format(query, "', '".join(keywords)))
        self.db_engine.add_query(user_id, query)
        self.db_engine.add_keywords(query, keywords)
        self.notify_agents()

    @staticmethod
    def notify_agents():
        """
        Notifies agent about new crawling query.
        """

        for url in settings.AGENT_URLS:
            try:
                requests.get('{0}/start_crawling'.format(url))
            except Exception as e:
                logger.error('Cannot connect to agent {0} due to: {1}'.format(
                    url, e.message))

    def get_user_queries(self, user_id):
        """
        Retrieves user queries form database.

        :param int user_id: Id of user associated with the query.
        :return: list of user queries.
        """

        return self.db_engine.get_user_queries(user_id)

    def get_urls(self, query):
        """
        Retrieves all URLs associated with given query form database.

        :return: list of URLs.
        """

        return self.db_engine.get_urls(query)

    def start_crawling(self):
        """
        Notifies all agents and if crawling process in not started, starts it.
        """

        self.search_engine.reload_queries()
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
            soup = BeautifulSoup(response.body)

            for script in soup(["script", "style"]):
                script.extract()

            text = " ".join(soup.get_text().split())
            url = response.url
            CrawlerEngine.search_engine.search_in_url(url, text)
