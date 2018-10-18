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
        # with open('./data/irregular.json') as f:
        #     self.irregularNouns = json.load(f)

        with open('./data/exceptions.json') as f:
            self.exceptionNouns = json.load(f)

    # def isIrregularNoun(self, word):
    #     return word in self.irregularNouns
    # def isExceptionNoun(self, word):
    #     return word in self.exceptionNouns

    def getPluralForm(self, word):
        vowels = self.vowels
        consonants = self.consonants
        # if self.isIrregularNoun(word):
        #     return self.irregularNouns[word]

        # if self.isExceptionNoun(word):
        #     return self.exceptionNouns[word]

        # ID-7. Ends in VOWEL + O
        if word.endswith("o") and word[-2:][0] in vowels:
            return word + "s"

        # ID-2: Ends in consonants + Y
        if word.endswith("y") and word[-2:][0] in consonants:
            return word[:-1] + "ies"

        # ID-9: Ends in -IS
        if word.endswith("is"):
            return word[:-2] + "es"

        # ID-3: Ends in S, CH, SH, X or Z
        if word.endswith("s") or word.endswith("ch") or word.endswith("sh") or word.endswith("x") or word.endswith("z"):
            return word + "es"

        # ID-4: Ends in F or FE
        if word.endswith("f") or word.endswith("fe"):
            #ID-5 Ends in two vowels plus -f
            if word.endswith("oof") or word.endswith("ief") or word.endswith("ff"):
                return word + "s"
            if word.endswith("f"):
                return word[:-1] + "ves"
            if word.endswith("fe"):
                return word[:-2] + "ves"



        # ID-. Ends in consonants + O
        # if word.endswith("o") and word[-2:][0] in consonants:
        #     return word + "es"

        # ID-1: Most nouns
        return word + "s"
