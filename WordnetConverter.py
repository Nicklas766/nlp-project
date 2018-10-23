from nltk.corpus import wordnet
from nltk import pos_tag, word_tokenize
from nltk.stem import WordNetLemmatizer
from WordData import WordData

class WordnetConverter:

    def __init__(self):
        self.ConversionData = {
            "synsets": [],
            "spellingErrors": []
        }

    def penn_to_wordnet(self, tag):
        if tag.startswith('J'):
            return wordnet.ADJ
        elif tag.startswith('N'):
            return wordnet.NOUN
        # elif tag.startswith('R'):
        #      return wordnet.ADV
        # elif tag.startswith('V'):
        #      return wordnet.VERB
        return None

    def get_synset_tokens(self, tagged):
        lemmatzr = WordNetLemmatizer()
        for token in tagged:
            wordnet_tag = self.penn_to_wordnet(token[1])
            if not wordnet_tag:
                continue

            lemma = lemmatzr.lemmatize(token[0], pos=wordnet_tag)

            # If it can't append on try it's probably a spelling error
            try:
                self.ConversionData["synsets"].append(WordData(token[0], wordnet.synsets(lemma, pos=wordnet_tag)[0]))
            except:
                self.ConversionData["spellingErrors"].append(token[0])


        return self.ConversionData
