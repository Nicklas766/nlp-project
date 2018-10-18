import json

# def writeToJSONFile(path, fileName, a_dict):
#     filePathNameWExt = './' + path + '/' + fileName + '.json'
#
#     with open(filePathNameWExt) as f:
#         data = json.load(f)
#
#     data.update(a_dict)
#
#     with open(filePathNameWExt, 'w') as f:
#         json.dump(data, f)


# Cannot handle irregular Nouns or "no change" very well
class Plurify:
# uses https://www.google.com/search?q=Noun,+plural&num=20&client=firefox-b-ab&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi_x5vg2o_eAhVECSwKHTqIAZQQ_AUIDigB&biw=1920&bih=966#imgrc=pibmJxpzlHHPAM:

    # misses Y
    vowels = ["a", "e", "i", "o", "u"]
    # misses W and Y
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "z"]

    def __init__(self):
        with open('./data/irregular.json') as f:
            self.irregularNouns = json.load(f)

        with open('./data/exceptions.json') as f:
            self.exceptionNouns = json.load(f)

    def isIrregularNoun(self, word):
        return word in self.irregularNouns
    def isExceptionNoun(self, word):
        return word in self.exceptionNouns

    def getPluralForm(self, word):

        if self.isIrregularNoun(word):
            return self.irregularNouns[word]

        if self.isExceptionNoun(word):
            return self.exceptionNouns[word]

        # Ends in S, CH, SH, X or Z
        if word.endswith("s") or word.endswith("ch") or word.endswith("sh") or word.endswith("x") or word.endswith("z"):
            if word.endswith("z"):
                return word + "zes"
            return word + "es"

        # Ends in F or FE
        if word.endswith("f") or word.endswith("fe"):
            if word.endswith("f"):
                return word[:-1] + "ves"
            if word.endswith("fe"):
                return word[:-2] + "ves"

        # 1. Ends in VOWEL + Y
        if word.endswith("y") and word[-2:][0] in self.vowels:
            return word + "s"

        # 1. Ends in consonants + Y
        if word.endswith("y") and word[-2:][0] in self.consonants:
            return word[:-1] + "ies"

        # 1. Ends in VOWEL + O
        if word.endswith("o") and word[-2:][0] in self.vowels:
            return word + "s"

        # 1. Ends in consonants + O
        if word.endswith("o") and word[-2:][0] in self.consonants:
            return word + "es"

        # 1. Regular Noun
        return word + "s"
