from unittest import TestCase
from mock import MagicMock

from SearchEngine import SearchEngine


class TestSearchEngine(TestCase):
    def test_search_should_return_one_element_query_list(self):
        # given
        search_engine = SearchEngine()
        query = 'I like python, jython and cpython'
        search_engine.queries = [query]
        search_engine.db_engine.get_keywords = MagicMock(
            return_value=['python', 'jython', 'cpython'])

        # when
        text = 'Jython is very good programming language. Cpython too.'
        queries = search_engine.search(text)

        # then
        self.assertTrue(query in queries)
        self.assertEqual(len(queries), 1)

    def test_search_should_return_empty_query_list(self):
        # given
        search_engine = SearchEngine()
        query = 'I like python, jython and cpython'
        search_engine.queries = [query]
        search_engine.db_engine.get_keywords = MagicMock(
            return_value=['python', 'jython', 'cpython'])

        # when
        text = 'This is a sample sentence.'
        queries = search_engine.search(text)

        # then
        self.assertTrue(query not in queries)
        self.assertEqual(len(queries), 0)
