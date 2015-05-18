from riak import RiakClient
from riak.datatypes import Set


class DbEngine(object):
    def __init__(self):
        self.client = RiakClient(pb_port=8087, protocol='pbc')

    def add_query(self, user, query):
        bucket = self.client.bucket_type('set').bucket('queries')
        queries_bucket = Set(bucket, str(user.id))
        queries_bucket.add(str(query))
        queries_bucket.store()

    def get_queries(self, user):
        bucket = self.client.bucket_type('set').bucket('queries')
        queries_bucket = Set(bucket, str(user.id))
        queries_bucket.reload()
        return queries_bucket.value

    def add_keywords(self, keywords):
        bucket = self.client.bucket_type('set').bucket('keywords')
        keywords_bucket = Set(bucket, 'keywords')
        for keyword in keywords:
            keywords_bucket.add(str(keyword))
        keywords_bucket.store()

    def get_keywords(self):
        bucket = self.client.bucket_type('set').bucket('keywords')
        keywords_bucket = Set(bucket, 'keywords')
        keywords_bucket.reload()
        return keywords_bucket.value

    def add_url(self, url, keywords):
        bucket = self.client.bucket_type('set').bucket('urls')
        for keyword in keywords:
            urls_bucket = Set(bucket, str(keyword))
            urls_bucket.add(str(url))
            urls_bucket.store()

    def get_urls(self, keywords):
        urls = set()
        bucket = self.client.bucket_type('set').bucket('urls')
        for keyword in keywords:
            urls_bucket = Set(bucket, str(keyword))
            urls_bucket.reload()
            urls |= urls_bucket.value
        return urls