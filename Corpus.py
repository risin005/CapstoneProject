import TextAnalyzer
import json
import nltk

def corpusMatch(keyWord):
    return

def oneTimeStartUp(): #This is just a script to initially fill our Corpus of possible street associations.
    file = open("startingCorpus.txt", "r")
    test = []
    for x in file.readlines():
        test.append(x)

    finalString = " ".join(test)

    print(finalString)

    file.close()

    tokens = nltk.word_tokenize(finalString)

    print(tokens)

    corpus = dict()
    for x in tokens:
        corpus.update({x:"streets"})

    with open("corpus.json", "w") as file:
        json.dump(corpus, file)

    print(corpus)


oneTimeStartUp()