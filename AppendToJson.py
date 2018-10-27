import json

# Since json has to be read everytime - this solution to gather sentences should be changed
class AppendToJson:
    """Saves searches into a json file"""

    def saveSentenceToJsonFile(sentence):
        filePathNameWExt = './data.json'

        with open(filePathNameWExt) as f:
            data = json.load(f)

        data["sentences"].append(sentence)


        with open(filePathNameWExt, 'w') as f:
            json.dump(data, f)