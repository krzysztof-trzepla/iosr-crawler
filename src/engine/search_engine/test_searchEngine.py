from unittest import TestCase

from SearchEngine import SearchEngine


class TestSearchEngine(TestCase):
    def test_search_should_return_two_element_keyword_list(self):
        # given
        search_engine = SearchEngine()
        search_engine.keywords = ['python', 'jython', 'cpython']

        # when
        text = 'Jython is very good programming language. Cpython too.'
        keywords = search_engine.search(text)

        # then
        self.assertTrue('python' not in keywords)
        self.assertTrue('jython' in keywords)
        self.assertTrue('cpython' in keywords)
        self.assertEqual(len(keywords), 2)

    def test_search_should_return_empty_keyword_list(self):
        # given
        search_engine = SearchEngine()
        search_engine.keywords = ['python', 'jython', 'cpython']

        # when
        text = 'This is a sample sentence.'
        keywords = search_engine.search(text)

        # then
        self.assertTrue('python' not in keywords)
        self.assertTrue('jython' not in keywords)
        self.assertTrue('cpython' not in keywords)
        self.assertEqual(len(keywords), 0)