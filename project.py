
import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')




class SynonymSentenceParser:
    """Changes all the words in a sentence synonyms and sorts them by percentage"""
    """Identifierar verb, adjektiv etc 'viktiga ord' och erbjuder synonymer"""

    def __init__(self, text):
        self.tokensArray = nltk.word_tokenize(text)

    def breakAllSentences(text):
        return nltk.sent_tokenize(text)

    def helloWorld(self):
        return "hello world"

    def CreateSentenceWithNewSynonyms(self):
        for token in self.tokensArray:
            try:
                # Only takes snyonyms with the highest semantic similarity
                highestSimilarity = 0
                minAcceptableSimilarity = 0.6
                originalWord = wordnet.synsets(token)[0];

                print("WORD::::::::::::::::::", originalWord)
                for synset in wordnet.synsets(token):
                    if originalWord.wup_similarity(synset) > minAcceptableSimilarity and originalWord != synset:
                        print(synset)
            except:
                print("none found")



parser = SynonymSentenceParser("Hi there, my name is Nicklas, I truly love computers and nature, I usually take some walks outside");
parser.CreateSentenceWithNewSynonyms();

## sentence = """Hej är mitt namn. hej mitt är namn? ehj på dig."""

# Sentence Segmentation: break the text apart into separate sentences
#  sentenceSegmentation = nltk.sent_tokenize(sentence);

# Word Tokenization: break each sentence into separate words or tokens
## tokens = nltk.word_tokenize(sentence)

#Predicting Parts of Speech for Each Token: look at each token and try to guess its part of speech — whether it is a noun, a verb, an adjective and so on.#

## partOfSpeech = nltk.pos_tag(tokens)


# print(nltk.sent_tokenize(sentence))

#
# print(tokens)
# for ss in wordnet.synsets('best'):
#    print(ss.lemma_names())
