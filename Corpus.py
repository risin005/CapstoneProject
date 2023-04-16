import TextAnalyzer
import TemplateBuilder
import json
import nltk
import KeywordFinder

def corpusMatch(keyWord):
    keyWord= ['Dispatch', ',', 'Officer', 'Brown', '.', 'I', 'suspect', 'custody', 'corner', '5th', 'avenue', 'main', 'street', '.', '15 North','Closed']
    with open('corpus.json','r') as corpus:
        corpus_dict = json.load(corpus)
        wordsWithContext = []

    #for word in keyWord:
    for i in range(len(keyWord)):
        if keyWord[i] in corpus_dict:
            if corpus_dict.get(keyWord[i]) == "streets" and i > 0: #If a street name is found, concatinate both parts
                streetName = keyWord[i-1] + " " + keyWord[i]
                element = (streetName, corpus_dict.get(keyWord[i]))
            else: #if just a keyword, then find the given context in the corpus
                element = (keyWord[i], corpus_dict.get(keyWord[i]))
            wordsWithContext.append(element)

    print(wordsWithContext)
    KeywordFinder.providedKeywordContext(wordsWithContext)

   #This will add to the dictionary and as thus will need to add to the JSON file
def addCorpus(word,type):
    #Load in an instance of the current corpus from the json into a dictionary
    with open('corpus.json','r') as corpus:
        corpus_dict = json.load(corpus)
    #Update the dictionary with the new entry
    corpus_dict[word] = type
    #Write it back to the json
    with open("corpus.json", "w") as file:
        json.dump(corpus_dict, file)

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

