from riak import RiakClient
from riak.datatypes import Set


class DbEngine(object):
    def __init__(self):
        self.client = RiakClient(pb_port=8087, protocol='pbc')

    def add_query(self, user_id, query, bucket_name='user_queries'):
        bucket = self.client.bucket_type('set').bucket(bucket_name)
        queries_bucket = Set(bucket, str(user_id))
        queries_bucket.add(str(query))
        queries_bucket.store()
        bucket = self.client.bucket_type('set').bucket('all_queries')
        queries_bucket = Set(bucket, 'queries')
        queries_bucket.add(str(query))
        queries_bucket.store()

    def get_user_queries(self, user_id, bucket_name='user_queries'):
        bucket = self.client.bucket_type('set').bucket(bucket_name)
        queries_bucket = Set(bucket, str(user_id))
        queries_bucket.reload()
        return queries_bucket.value

    def get_all_queries(self, bucket_name='all_queries'):
        bucket = self.client.bucket_type('set').bucket(bucket_name)
        queries_bucket = Set(bucket, 'queries')
        queries_bucket.reload()
        return queries_bucket.value

    def add_keywords(self, query, keywords, bucket_name='keywords'):
        bucket = self.client.bucket_type('set').bucket(bucket_name)
        keywords_bucket = Set(bucket, str(query))
        for keyword in keywords:
            keywords_bucket.add(str(keyword))
        keywords_bucket.store()

    def get_keywords(self, query, bucket_name='keywords'):
        bucket = self.client.bucket_type('set').bucket(bucket_name)
        keywords_bucket = Set(bucket, str(query))
        keywords_bucket.reload()
        return keywords_bucket.value

    def add_url(self, query, url, bucket_name='urls'):
        bucket = self.client.bucket_type('set').bucket(bucket_name)
        urls_bucket = Set(bucket, str(query))
        urls_bucket.add(str(url))
        urls_bucket.store()

    def get_urls(self, query, bucket_name='urls'):
        urls = set()
        bucket = self.client.bucket_type('set').bucket(bucket_name)
        urls_bucket = Set(bucket, str(query))
        urls_bucket.reload()
        urls |= urls_bucket.value
        return urls
