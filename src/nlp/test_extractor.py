from unittest import TestCase

from nlp.extractor import NLPExtractor


class TestExtractor(TestCase):
    def test_keywords_extraction(self):
        # given
        extractor = NLPExtractor()

        # when
        text = 'Java and Python programming books.'

        # then
        self.assertEqual(['java', 'python'], extractor.keywords(text))
