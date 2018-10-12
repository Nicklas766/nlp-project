import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from WordnetConverter import WordnetConverter
from WordData import WordData


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
        self.synsets = WordnetConverter().get_synset_tokens(pos_tag)

        # Test methods with print
        print(self.get_synsets(self.synsets))


    def is_synset_similar(self, synset1, synset2):
        try:
            return synset1.wup_similarity(synset2) > self.minAcceptableSimilarity
        except:
            return False

    def get_synsets(self, synsets):
        return [self.get_similiar_synset(word_data) for word_data in synsets]

    def get_similiar_synset(self, word_data):
        return [{word_data.token: synset} for synset in wordnet.synsets(word_data.token) if self.is_synset_similar(word_data.synset, synset)]
