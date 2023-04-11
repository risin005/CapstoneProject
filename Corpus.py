import TextAnalyzer
import TemplateBuilder
import json
import nltk

def corpusMatch(keyWord):
    keyWord= ['Dispatch', ',', 'Officer', 'Brown', '.', 'I', 'suspect', 'custody', 'corner', '5th', 'avenue', 'main', 'street', '.']
    with open('corpus.json','r') as corpus:
        corpus_dict = json.load(corpus)
        wordsWithContext = []

    #for word in keyWord:
    for i in range(len(keyWord)):
        if keyWord[i] in corpus_dict:
            element = (keyWord[i],corpus_dict.get(keyWord[i]))
            wordsWithContext.append(element)

    print(wordsWithContext)
    TemplateBuilder.filledTemplate(wordsWithContext)

   #This will add to the dictionary and as thus will need to add to the JSON file
def addCorpus(word,type):

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

corpusMatch("")
