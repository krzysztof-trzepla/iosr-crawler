from re import split
from engine.db_engine.DbEngine import DbEngine


class SearchEngine(object):
    def __init__(self):
        self.db_engine = DbEngine()
        self.keywords = self.db_engine.get_keywords()

    def reload_keywords(self):
        self.keywords = self.db_engine.get_keywords()

    def search_in_url(self, url, content):
        keywords = self.search(content)
        self.db_engine.add_url(url, keywords)

    def search(self, content):
        content = split('\W*', content.lower())
        keywords = set()
        for keyword in self.keywords:
            if keyword in content:
                keywords.add(keyword)
        return keywords



