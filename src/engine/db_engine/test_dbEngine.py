from unittest import TestCase

from DbEngine import DbEngine


class TestDbEngine(TestCase):
    def test_query_addition_and_retrieval(self):
        # given
        db_engine = DbEngine()
        bucket = 'test_queries'
        self._clean_bucket(db_engine.client, bucket)
        query1 = 'This is the first query.'
        query2 = 'This is the second query.'
        query3 = 'This is the third query.'

        # when
        db_engine.add_query(1, query1, bucket)
        db_engine.add_query(1, query2, bucket)
        db_engine.add_query(2, query3, bucket)

        # then
        self.assertEqual({query1, query2}, db_engine.get_queries(1, bucket))
        self.assertEqual({query3}, db_engine.get_queries(2, bucket))
        self.assertTrue(len(db_engine.get_queries(3, bucket)) == 0)

    def test_keywords_addition_and_retrieval(self):
        # given
        db_engine = DbEngine()
        bucket = 'test_keywords'
        self._clean_bucket(db_engine.client, bucket)
        keyword1 = 'keyword1'
        keyword2 = 'keyword2'
        keyword3 = 'keyword3'

        # when
        db_engine.add_keywords([keyword1, keyword2], bucket)
        db_engine.add_keywords([keyword1], bucket)
        db_engine.add_keywords([keyword2], bucket)
        db_engine.add_keywords([keyword2, keyword3], bucket)

        # then
        self.assertEqual({keyword1, keyword2, keyword3},
                         db_engine.get_keywords(bucket))

    def test_urls_addition_and_retrieval(self):
        # given
        db_engine = DbEngine()
        bucket = 'test_urls'
        self._clean_bucket(db_engine.client, bucket)
        url1 = 'url1'
        url2 = 'url2'
        keyword1 = 'keyword1'
        keyword2 = 'keyword2'
        keyword3 = 'keyword3'

        # when
        db_engine.add_url(url1, [keyword1, keyword2], bucket)
        db_engine.add_url(url1, [keyword1], bucket)
        db_engine.add_url(url2, [keyword1], bucket)

        # then
        self.assertEqual({url1, url2}, db_engine.get_urls([keyword1], bucket))
        self.assertEqual({url1}, db_engine.get_urls([keyword2], bucket))
        self.assertTrue(len(db_engine.get_urls([keyword3], bucket)) == 0)

    def _clean_bucket(self, client, bucket_name):
        bucket = client.bucket_type('set').bucket(bucket_name)
        for keys in bucket.stream_keys():
            for key in keys:
                bucket.delete(key)
