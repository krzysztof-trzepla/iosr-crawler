from unittest import TestCase
from SearchEngine import SearchEngine


class TestSearchEngine(TestCase):
    # def setUp(self):
    # self.searchEngine = SearchEngine

    def test_addingPhrasesToEmptySearchEngineShouldAddPhraseToSearchEngine(self):
        # given
        searchEngine = SearchEngine()
        phrase1 = "python"
        # when
        searchEngine.addPhraseToSearch(phrase1)
        # then
        self.assertTrue(phrase1 in searchEngine.getRequestedPhrases())
        self.assertEqual(len(searchEngine.getRequestedPhrases()), 1)


    def test_removingPhraseEngineShouldRemovePhraseFromSearchEngineIfExist(self):
        # given
        searchEngine = SearchEngine()
        phrase1 = "python"
        phrase2 = "jython"
        phrase3 = "cpython"

        searchEngine.addPhraseToSearch(phrase1)
        searchEngine.addPhraseToSearch(phrase2)
        searchEngine.addPhraseToSearch(phrase3)
        # when
        searchEngine.deletePhraseToSearch(phrase2)
        # then
        self.assertTrue(phrase2 not in searchEngine.getRequestedPhrases())
        self.assertEqual(len(searchEngine.getRequestedPhrases()), 2)

    def test_removingPhraseWhichIsNotInSearchEngineShouldDoNothing(self):
        # given
        searchEngine = SearchEngine()
        phrase1 = "python"
        phrase2 = "jython"
        phrase3 = "cpython"

        searchEngine.addPhraseToSearch(phrase1)
        searchEngine.addPhraseToSearch(phrase2)
        searchEngine.addPhraseToSearch(phrase3)
        # when
        searchEngine.deletePhraseToSearch("cokolwiek")
        # then
        self.assertTrue(phrase1 in searchEngine.getRequestedPhrases())
        self.assertTrue(phrase2 in searchEngine.getRequestedPhrases())
        self.assertTrue(phrase3 in searchEngine.getRequestedPhrases())
        self.assertEqual(len(searchEngine.getRequestedPhrases()), 3)

    def test_searchingShouldReturnTwoElementedResultsList(self):
        # given
        searchEngine = SearchEngine()
        phrase1 = "pythonn"
        phrase2 = "jython"
        phrase3 = "cpython"

        searchEngine.addPhraseToSearch(phrase1)
        searchEngine.addPhraseToSearch(phrase2)
        searchEngine.addPhraseToSearch(phrase3)
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
        phrase1 = "python"
        phrase2 = "jython"
        phrase3 = "cpython"

        searchEngine.addPhraseToSearch(phrase1)
        searchEngine.addPhraseToSearch(phrase2)
        searchEngine.addPhraseToSearch(phrase3)
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