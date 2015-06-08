from re import split
from django.conf import settings
from engine.db_engine.DbEngine import DbEngine


class SearchEngine(object):
    def __init__(self):
        self.db_engine = DbEngine()
        self.queries = self.db_engine.get_all_queries()

    def reload_queries(self):
        self.queries = self.db_engine.get_all_queries()

    def search_in_url(self, url, content):
        queries = self.search(content)
        for query in queries:
            self.db_engine.add_url(query, url)

    def search(self, content):
        content = split('\W*', content.lower())
        queries = set()
        for query in self.queries:
            keywords = self.db_engine.get_keywords(query)
            found = 0
            for keyword in keywords:
                if keyword in content:
                    found += 1
            if float(found) / len(keywords) >= settings.KEYWORD_THRESHOLD:
                queries.add(query)
        return queries
