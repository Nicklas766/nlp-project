import unittest

from SynonymSentenceParser import SynonymSentenceParser

class TestSynonymSentenceParserMethods(unittest.TestCase):


    # def setUp(self):
    #     self.synonymSentenceParser = SynonymSentenceParser(self.sentence)
    #
    # def tearDown(self):
    #     self.synonymSentenceParser = None

    def test_spelling_error(self):
        # Should fail
        SynonymSentenceParser("Hi people")
        self.assertEqual(self.synonymSentenceParser, '')







if __name__ == '__main__':
    unittest.main()
