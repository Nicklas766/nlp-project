import unittest

from project import SynonymSentenceParser



class TestSynonymSentenceParserMethods(unittest.TestCase):

    sentence = "Hello my name is Nicklas, and I love computer science."

    def setUp(self):
        self.synonymSentenceParser = SynonymSentenceParser(self.sentence)

    def tearDown(self):
        self.synonymSentenceParser = None

    def test_helloWorld(self):
        self.assertEqual(self.synonymSentenceParser.helloWorld(), 'hello world')

    def test_CreateSentenceWithNewSynonyms(self):
        self.assertEqual(self.synonymSentenceParser.CreateSentenceWithNewSynonyms(), '')



if __name__ == '__main__':
    unittest.main()
