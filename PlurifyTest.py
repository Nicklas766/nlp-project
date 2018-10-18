import unittest
from Plurify import Plurify

class TestPlurifyMethods(unittest.TestCase):

    def test_plural_forms_that_end_with_es(self):
        # Should pass
        returnedWordForm = Plurify().getPluralForm("bus")
        correctWordForm = "buses"
        self.assertEqual(returnedWordForm, correctWordForm)

        returnedWordForm = Plurify().getPluralForm("match")
        correctWordForm = "matches"
        self.assertEqual(returnedWordForm, correctWordForm)

        returnedWordForm = Plurify().getPluralForm("dish")
        correctWordForm = "dishes"
        self.assertEqual(returnedWordForm, correctWordForm)

        returnedWordForm = Plurify().getPluralForm("box")
        correctWordForm = "boxes"
        self.assertEqual(returnedWordForm, correctWordForm)

        returnedWordForm = Plurify().getPluralForm("quiz")
        correctWordForm = "quizzes"
        self.assertEqual(returnedWordForm, correctWordForm)


    def test_plural_forms_that_end_with_f_or_fe(self):
        # Should pass
        returnedWordForm = Plurify().getPluralForm("leaf")
        correctWordForm = "leaves"
        self.assertEqual(returnedWordForm, correctWordForm)

        returnedWordForm = Plurify().getPluralForm("wolf")
        correctWordForm = "wolves"
        self.assertEqual(returnedWordForm, correctWordForm)

        returnedWordForm = Plurify().getPluralForm("life")
        correctWordForm = "lives"
        self.assertEqual(returnedWordForm, correctWordForm)

        returnedWordForm = Plurify().getPluralForm("knife")
        correctWordForm = "knives"
        self.assertEqual(returnedWordForm, correctWordForm)

        returnedWordForm = Plurify().getPluralForm("roof")
        correctWordForm = "roofs"
        self.assertEqual(returnedWordForm, correctWordForm)

        returnedWordForm = Plurify().getPluralForm("cliff")
        correctWordForm = "cliffs"
        self.assertEqual(returnedWordForm, correctWordForm)


    def test_plural_forms_that_end_with_vowel_and_y(self):
        # Should pass
        returnedWordForm = Plurify().getPluralForm("day")
        correctWordForm = "days"
        self.assertEqual(returnedWordForm, correctWordForm)

        returnedWordForm = Plurify().getPluralForm("key")
        correctWordForm = "keys"
        self.assertEqual(returnedWordForm, correctWordForm)

    def test_plural_forms_that_end_with_consonant_and_y(self):
        # Should pass
        returnedWordForm = Plurify().getPluralForm("city")
        correctWordForm = "cities"
        self.assertEqual(returnedWordForm, correctWordForm)

        returnedWordForm = Plurify().getPluralForm("party")
        correctWordForm = "parties"
        self.assertEqual(returnedWordForm, correctWordForm)

    def test_plural_forms_that_end_with_vowel_and_o(self):
        # Should pass
        returnedWordForm = Plurify().getPluralForm("zoo")
        correctWordForm = "zoos"
        self.assertEqual(returnedWordForm, correctWordForm)

        returnedWordForm = Plurify().getPluralForm("radio")
        correctWordForm = "radios"
        self.assertEqual(returnedWordForm, correctWordForm)

        returnedWordForm = Plurify().getPluralForm("stereo")
        correctWordForm = "stereos"
        self.assertEqual(returnedWordForm, correctWordForm)

    def test_plural_forms_that_end_with_consonant_and_o(self):
        # Should pass
        returnedWordForm = Plurify().getPluralForm("hero")
        correctWordForm = "heroes"
        self.assertEqual(returnedWordForm, correctWordForm)

        returnedWordForm = Plurify().getPluralForm("echo")
        correctWordForm = "echoes"
        self.assertEqual(returnedWordForm, correctWordForm)

        returnedWordForm = Plurify().getPluralForm("tomato")
        correctWordForm = "tomatoes"
        self.assertEqual(returnedWordForm, correctWordForm)

        returnedWordForm = Plurify().getPluralForm("piano")
        correctWordForm = "pianos"
        self.assertEqual(returnedWordForm, correctWordForm)

        returnedWordForm = Plurify().getPluralForm("photo")
        correctWordForm = "photos"
        self.assertEqual(returnedWordForm, correctWordForm)

    def test_plural_forms_that_end_with_is(self):
        # Should pass
        returnedWordForm = Plurify().getPluralForm("analysis")
        correctWordForm = "analyses"
        self.assertEqual(returnedWordForm, correctWordForm)



if __name__ == '__main__':
    unittest.main()
