from riak import RiakClient
from riak.datatypes import Set


class DbEngine(object):
    def __init__(self):
        self.client = RiakClient(pb_port=8087, protocol='pbc')

    def add_query(self, user_id, query, bucket_name='user_queries'):
        """
        Adds query to database.

        :param int user_id: Id of user associated with the query.
        :param str query: Query to be saved into database.
        """

        bucket = self.client.bucket_type('set').bucket(bucket_name)
        queries_bucket = Set(bucket, str(user_id))
        queries_bucket.add(str(query))
        queries_bucket.store()
        bucket = self.client.bucket_type('set').bucket('all_queries')
        queries_bucket = Set(bucket, 'queries')
        queries_bucket.add(str(query))
        queries_bucket.store()

    def get_user_queries(self, user_id, bucket_name='user_queries'):
        """
        Retrieves user queries form database.

        :param int user_id: Id of user associated with the query.
        :return: list of user queries.
        """

        bucket = self.client.bucket_type('set').bucket(bucket_name)
        queries_bucket = Set(bucket, str(user_id))
        queries_bucket.reload()
        return queries_bucket.value

    def get_all_queries(self, bucket_name='all_queries'):
        """
        Retrieves all queries form database.

        :return: list of all queries.
        """

        bucket = self.client.bucket_type('set').bucket(bucket_name)
        queries_bucket = Set(bucket, 'queries')
        queries_bucket.reload()
        return queries_bucket.value

    def add_keywords(self, query, keywords, bucket_name='keywords'):
        """
        Adds keywords for given query to database.

        :param str query: Query associated with keywords.
        :param list keywords: List of keywords produced from the query.
        """

        bucket = self.client.bucket_type('set').bucket(bucket_name)
        keywords_bucket = Set(bucket, str(query))
        for keyword in keywords:
            keywords_bucket.add(str(keyword))
        keywords_bucket.store()

    def get_keywords(self, query, bucket_name='keywords'):
        """
        Retrieves all keywords associated with given query form database.

        :return: list of keywords.
        """

        bucket = self.client.bucket_type('set').bucket(bucket_name)
        keywords_bucket = Set(bucket, str(query))
        keywords_bucket.reload()
        return keywords_bucket.value

    def add_url(self, query, url, bucket_name='urls'):
        """
        Adds url for given query to database.

        :param str query: Query associated with url.
        :param str url: URL of page satisfying search requirements.
        """

        bucket = self.client.bucket_type('set').bucket(bucket_name)
        urls_bucket = Set(bucket, str(query))
        urls_bucket.add(str(url))
        urls_bucket.store()

    def get_urls(self, query, bucket_name='urls'):
        """
        Retrieves all URLs associated with given query form database.

        :return: list of URLs.
        """

        urls = set()
        bucket = self.client.bucket_type('set').bucket(bucket_name)
        urls_bucket = Set(bucket, str(query))
        urls_bucket.reload()
        urls |= urls_bucket.value
        return urls
