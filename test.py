import unittest

from project import SynonymSentenceParser

class TestSynonymSentenceParserMethods(unittest.TestCase):

    sentence = "Hello my name is Nicklas, and I love computer science."

    def setUp(self):
        self.synonymSentenceParser = SynonymSentenceParser(self.sentence)

    def tearDown(self):
        self.synonymSentenceParser = None

    def test_is_word_similarity_acceptable(self):
        self.assertEqual(self.synonymSentenceParser.is_word_similarity_acceptables(), '')



if __name__ == '__main__':
    unittest.main()
