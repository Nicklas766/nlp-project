import nltk

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

from nltk.wsd import lesk
from SynonymSentenceParser import SynonymSentenceParser


parser = SynonymSentenceParser("The problem with quotes found on the internet is that they are often not true");
#parser = SynonymSentenceParser("Hi people, what is going on?");
#parser = SynonymSentenceParser("Great");
#parser = SynonymSentenceParser("I am greater than you");

# parser = SynonymSentenceParser("I am currently cooking and I am also angry")
#print(nltk.pos_tag(nltk.word_tokenize("what is happening?")))
#print(nltk.pos_tag(nltk.word_tokenize("what is occur?")))

#print(convert("occur", "VBN", "VBG"))
# parser = SynonymSentenceParser("helo");
# parser = SynonymSentenceParser("I was outside running, now I feel pretty good");
# parser = SynonymSentenceParser("Jag var ute och sprang i skogen, nu mår jag bra");


# print(wordnet.synsets("good"))
# w1 = wordnet.synset("good.n.01")
# w2 = wordnet.synset("well.n.01")
# print(parser.is_word_similarity_acceptable(w1, w2))



# print("-----------------------------------------------------------------------")
# print("-----------------------------------------------------------------------")
# sent = nltk.word_tokenize("I was outside and charging fire, on forest taking a walk, it was nice!")
# print(lesk(sent, 'charging'))
#
# synset = lesk(sent, 'charging');
# print(synset.lemma_names())

## print(lemmatizer.lemmatize("better", pos="a"))

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
