import TextHighlighter
import nltk
from nltk.corpus import stopwords


def rawText(file):

    stop_words = set(stopwords.words('english'))

    #file = "Dispatch, this is Officer Brown. I have a suspect in custody at the corner of 5th Ave. and Main St."
    tokens = nltk.word_tokenize(file) #Tokenizes the setence

    filtered_words = []

    for w in tokens:
        if w not in stop_words:
            filtered_words.append(w)

    tag = nltk.pos_tag(filtered_words) #Tags the non-stop words

    TextHighlighter.highlightedKeywords(tokens, filtered_words)
'''
def providedKeywordContext(keyWords):

    context = [()]
    for words in KeyWords:
        context.append(Corpus.checkCorpus(word[0]))
'''


rawText("Dispatch, this is Officer Brown. I have a suspect in custody at the corner of 5th Ave. and Main St.")