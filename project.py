
import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nltk.wsd import lesk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
from nltk.corpus import wordnet as wn

class StackOverflow:
    def penn_to_wn(self, tag):
        if tag.startswith('J'):
            return wn.ADJ
        elif tag.startswith('N'):
            return wn.NOUN
        elif tag.startswith('R'):
            return wn.ADV
        elif tag.startswith('V'):
            return wn.VERB
        return None

    def get_synset_tokens(self, tagged):
        synsets = []
        lemmatzr = WordNetLemmatizer()
        for token in tagged:
            wn_tag = self.penn_to_wn(token[1])
            if not wn_tag:
                continue

            lemma = lemmatzr.lemmatize(token[0], pos=wn_tag)
            synsets.append(WordData(token[0], wn.synsets(lemma, pos=wn_tag)[0]))

        print(synsets)
        return synsets

class WordData:
    def __init__(self, token, synset):
        self.token = token
        self.synset = synset

class SynonymSentenceParser:
    """Changes all the words in a sentence synonyms and sorts them by percentage"""
    """Identifierar verb, adjektiv etc 'viktiga ord' och erbjuder synonymer"""

    minAcceptableSimilarity = 0.7
    def __init__(self, text):
        # Tokenize
        self.tokensArray = nltk.word_tokenize(text)

        # Part of Speech
        pos_tag = nltk.pos_tag(self.tokensArray)

        # Get synset from part of speech tags
        self.synsets = StackOverflow().get_synset_tokens(pos_tag)

        # Test methods with print
        print(self.get_similiar_synsets(self.synsets))


    def is_synset_similar(self, synset1, synset2):
        try:
            return synset1.wup_similarity(synset2) > self.minAcceptableSimilarity
        except:
            return False

    def get_similiar_synsets(self, synsets):
        stuff = []
        for word_data in synsets:
            stuff.append(self.get_similiar_synset(word_data))
        print(stuff)

    def get_similiar_synset(self, word_data):
        return [{word_data.token: synset} for synset in wordnet.synsets(word_data.token) if self.is_synset_similar(word_data.synset, synset)]
