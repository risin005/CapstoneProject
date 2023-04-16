#import GUI
import nltk

def highlightedKeywords(analyzedText, keyWords):
    start = '$'
    end = '*'
    index = 0 #Index

    print("anaylzedText:")
    print(analyzedText)
    print("")
    print("KeyWords:")
    print(keyWords)
    print("")
    keyWords = nltk.word_tokenize(keyWords)

    for keywords in keyWords:
        for word in analyzedText:
            if keywords == word:
                #print("Found")
                keyWords[index] = start + word + end
        index+=1

    print("Highlights:")
    print(keyWords)
    print("")

    newString = " ".join(keyWords)
    print("Final String")
    print(newString)

    '''
    for word in analyzedText[0]: #Going to walkthrough the tokenized sentence
        if word in keyWords: #Going to check to see if the word was filtered
            highlight = start+word+end #If found, go ahead and attach the highlighting brackets
            analyzedText[index] = highlight #And then add the new string to the sentence
        index+=1
    

    newString = " ".join(keyWords)

    print(newString) #Place holder for a function to call the GUI function to paste this string
   '''

