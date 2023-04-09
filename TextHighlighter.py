#import GUI

def highlightedKeywords(analyzedText, keyWords):
    #print(analyzedText)
    #print(keyWords)

    start = '\033[1;32m'
    end = '\033[1;m'
    index = 0 #Index

    for word in analyzedText: #Going to walkthrough the tokenized sentence
        if word in keyWords: #Going to check to see if the word was filtered
            highlight = start+word+end #If found, go ahead and attach the highlighting brackets
            analyzedText[index] = highlight #And then add the new string to the sentence
        index+=1

    newString = " ".join(analyzedText)

    print(newString)


