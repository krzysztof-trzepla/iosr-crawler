from unittest import TestCase

from SearchEngine import SearchEngine


class TestSearchEngine(TestCase):

    def test_addingPhrasesToEmptySearchEngineShouldAddPhraseToSearchEngine(self):
        # given
        searchEngine = SearchEngine()
        size = len(searchEngine.get_phrases())
        phrase1 = "python"
        # when
        searchEngine.add_phrase(phrase1)
        # then
        self.assertTrue(phrase1 in searchEngine.get_phrases())
        self.assertEqual(len(searchEngine.get_phrases()), size+1)


    def test_removingPhraseEngineShouldRemovePhraseFromSearchEngineIfExist(self):
        # given
        searchEngine = SearchEngine()
        size = len(searchEngine.get_phrases())
        phrase1 = "python"
        phrase2 = "jython"
        phrase3 = "cpython"

        searchEngine.add_phrase(phrase1)
        searchEngine.add_phrase(phrase2)
        searchEngine.add_phrase(phrase3)
        # when
        searchEngine.delete_phrase(phrase2)
        # then
        self.assertTrue(phrase2 not in searchEngine.get_phrases())
        self.assertEqual(len(searchEngine.get_phrases()),  size+2)

    def test_removingPhraseWhichIsNotInSearchEngineShouldDoNothing(self):
        # given
        searchEngine = SearchEngine()
        size = len(searchEngine.get_phrases())
        phrase1 = "python"
        phrase2 = "jython"
        phrase3 = "cpython"

        searchEngine.add_phrase(phrase1)
        searchEngine.add_phrase(phrase2)
        searchEngine.add_phrase(phrase3)
        # when
        searchEngine.delete_phrase("cokolwiek")
        # then
        self.assertTrue(phrase1 in searchEngine.get_phrases())
        self.assertTrue(phrase2 in searchEngine.get_phrases())
        self.assertTrue(phrase3 in searchEngine.get_phrases())
        self.assertEqual(len(searchEngine.get_phrases()),  size +3)

    def test_searchingShouldReturnTwoElementedResultsList(self):
        # given
        searchEngine = SearchEngine()
        searchEngine.requestedPhrases = []
        phrase1 = "pythonn"
        phrase2 = "jython"
        phrase3 = "cpython"

        searchEngine.add_phrase(phrase1)
        searchEngine.add_phrase(phrase2)
        searchEngine.add_phrase(phrase3)
        # when
        textToSearch = """ Jython is very good programining language.
        cpython too.
         """
        results = searchEngine.search(textToSearch)

        # then
        self.assertTrue(phrase1 not in results)
        self.assertTrue(phrase2 in results)
        self.assertTrue(phrase3 in results)
        self.assertEqual(len(results), 2)

    def test_searchingShouldReturnEmptyListResults(self):
        # given
        searchEngine = SearchEngine()
        searchEngine.requestedPhrases = []
        phrase1 = "python"
        phrase2 = "jython"
        phrase3 = "cpython"

        searchEngine.add_phrase(phrase1)
        searchEngine.add_phrase(phrase2)
        searchEngine.add_phrase(phrase3)
        # when
        textToSearch = """ fsdsadsa sadasdas  fsadsa afdasdas daw dawxasd gweghtrnhfdf
        dfdsf s sdfg s.
        cpythsdson too.
         """
        results = searchEngine.search(textToSearch)

        # then
        self.assertTrue(phrase1 not in results)
        self.assertTrue(phrase2 not in results)
        self.assertTrue(phrase3 not in results)
        self.assertEqual(len(results), 0)