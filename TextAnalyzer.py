import TextHighlighter

import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def rawText(file):

    tokens = nltk.word_tokenize(file) #Tokenizes the setence

    filtered_words = []
    for index in range(len(tokens)):
        if tokens[index] not in stop_words and tokens[index] != "the":
            if tokens[index].isdigit() and index >0: #ADjust this to find the previous JJ or JJs
                filtered_words.append(tokens[index] + " " + tokens[index-1])
                filtered_words.append(tokens[index-1] + " " + tokens[index])
            filtered_words.append(tokens[index])
        index+=1

    print(filtered_words)
    tag = nltk.pos_tag(filtered_words) #Tags the non-stop words
    print(tag)
    TextHighlighter.highlightedKeywords(tokens, filtered_words)
'''
def providedKeywordContext(keyWords):

    context = [()]
    for words in KeyWords:
        context.append(Corpus.checkCorpus(word[0]))
'''


rawText("Going south on the 15 and heading on the west 15")