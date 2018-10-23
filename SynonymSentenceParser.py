import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from WordnetConverter import WordnetConverter
from WordData import WordData
import itertools
from functools import reduce
from nltk.wsd import lesk
from Plurify import Plurify

def getCorrectForm(correctTag, newTag, word):
    if correctTag == "NNS" and newTag == "NN":
        return Plurify().getPluralForm(word)
    if correctTag == "NNS" and newTag == "JJ":
        return Plurify().getPluralForm(word)
    return word

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

        ## compare the lemmas similarity
        print("THE CORRECT:")
        print(pos_tag)
        print(arr)
        for curr in arr:
            for key in curr:
                for value in curr[key]:

                    # print(text.replace(key, value))
                    #if nltk.pos_tag(nltk.word_tokenize(key))[0][1] == nltk.pos_tag(nltk.word_tokenize(value))[0][1]:
                    newSentence = text.replace(key, value)
                    #print(newSentence)
                    newSentence = self.update_some_words(pos_tag, newSentence)

                    if self.is_syntax_acceptable(pos_tag, newSentence):
                        self.newSentences.append(newSentence)
                        print(newSentence)


        print("POTENTIAL SPELLING ERRORS FOUND!: ", spellingErrors)
        self.spellingErrors = spellingErrors
        self.newSentences = set(self.newSentences)

    @staticmethod
    def update_some_words(orginialPosTags, newSentence):
        tokenizeNew =  nltk.word_tokenize(newSentence)
        newSentence = nltk.pos_tag(tokenizeNew)
        #print(newSentence)
        sentence = ""
        for tag1, tag2 in zip(newSentence, orginialPosTags):
            sentence += " " + getCorrectForm(tag2[1], tag1[1], tag1[0])

        return sentence

    @staticmethod
    def is_syntax_acceptable(orginialPosTags, newSentence):
        tokenizeNew =  nltk.word_tokenize(newSentence)
        newSentence = nltk.pos_tag(tokenizeNew)
        #print(newSentence)
        for tag1, tag2 in zip(newSentence, orginialPosTags):
            if (tag2[1] == 'VBN' and tag1[1] != 'VBN'):
                return False
            if (tag2[1] == 'NNS' and tag1[1] == 'NN'):
                return False
            if (tag2[1] == 'VBZ' and tag1[1] == 'VB'):
                return False
            if (tag2[1].startswith('V') and (tag1[1].startswith('V') == False)):
                return False
        return True


    def is_synset_similar(self, synset1, synset2):
        try:
            return synset1.wup_similarity(synset2) > self.minAcceptableSimilarity
        except:
            return False

    def get_synsets(self, synsets):
         return list(map(self.get_similiar_synset, synsets))


    def get_similiar_synset(self, word_data):
        synsetsList = filter(lambda synset: self.is_synset_similar(word_data.synset, synset), wordnet.synsets(word_data.token))
        lemmasNestedList = map(self.get_lemmas_name, synsetsList)
        lemmas = [lemma for lemmaList in lemmasNestedList for lemma in lemmaList]
        #lemmas = map(lambda lemma: lemma.name(), word_data.synset.lemmas())

        return {
            word_data.token: set(lemmas)
        }

    @staticmethod
    def get_lemmas_name(synset):
        return map(lambda lemma: lemma.name(), synset.lemmas())
