from engine.db_engine.DbEngine import DbEngine


class SearchEngine(object):
    def __init__(self):
        self.db_engine = DbEngine()
        self.keywords = self.db_engine.get_keywords()
        print(self.keywords)

    def reload_keywords(self):
        self.keywords = self.db_engine.get_keywords()
        print(self.keywords)

    def search_in_url(self, url, content):
        keywords = self.search(content.lower())
        if len(keywords) > 0:
            print(keywords)
        self.db_engine.add_url(url, keywords)

    def search(self, content):
        keywords = set()
        for keyword in self.keywords:
            if keyword in content:
                keywords.add(keyword)
        return keywords



