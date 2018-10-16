import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from WordnetConverter import WordnetConverter
from WordData import WordData
import itertools
from functools import reduce


class SynonymSentenceParser:
    """Changes all the words in a sentence synonyms and sorts them by percentage"""
    """Identifierar verb, adjektiv etc 'viktiga ord' och erbjuder synonymer"""

    minAcceptableSimilarity = 0.7

    def __init__(self, text):
        self.newSentences = []
        # Tokenize
        self.tokensArray = nltk.word_tokenize(text)

        # Part of Speech
        pos_tag = nltk.pos_tag(self.tokensArray)
        print(pos_tag)

        # Get synset from part of speech tags while also detecting potential
        # spelling errors
        ConversionData = WordnetConverter().get_synset_tokens(pos_tag)
        synsets = ConversionData["synsets"]
        spellingErrors = ConversionData["spellingErrors"]


        # Test methods with print
        #print(self.get_synsets(synsets))
        arr = self.get_synsets(synsets)

        for curr in arr:
            for key in curr:
                for value in curr[key]:
                    self.newSentences.append(text.replace(key, value))
                    print(text.replace(key, value))

        print("POTENTIAL SPELLING ERRORS FOUND!: ", spellingErrors)
        self.spellingErrors = spellingErrors


    def is_synset_similar(self, synset1, synset2):
        try:
            return synset1.wup_similarity(synset2) > self.minAcceptableSimilarity
        except:
            return False

    def get_synsets(self, synsets):
        #return list(map(lambda word_data: self.get_similiar_synset(word_data), synsets))
         return list(map(self.get_similiar_synset, synsets))


    def get_similiar_synset(self, word_data):
        synsetsList = filter(lambda synset: self.is_synset_similar(word_data.synset, synset), wordnet.synsets(word_data.token))
        lemmasNestedList = map(self.get_lemmas_name, synsetsList)
        lemmas = [lemma for lemmaList in lemmasNestedList for lemma in lemmaList]

        return {
            word_data.token: set(lemmas)
        }

    @staticmethod
    def get_lemmas_name(synset):
        return map(lambda lemma: lemma.name(), synset.lemmas())
