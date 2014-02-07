import re
import os
import os.path
from wordnode import WordNode
from random import choice
import json

BEGIN_TOKEN = "____BEGIN____"
END_TOKEN =   "____END______"

# grab text data from a set of poems (in a directory)
def pullData(directory):
    files = os.listdir(directory)
    text = []

    for f in files:
        contents = ''
        with open(os.path.join(directory,f),'r') as file:
            contents = file.read()
        # strip non-alphabetical or space
        contents = ''.join([c for c in contents if c.isalpha() or c.isspace()])
        text.append(contents)

    text = [t.replace('\n',' ') for t in text]        
    return text

def grabTrigram(wordNode, prev, next):
    wordNode.addForward(next if next is not None else END_TOKEN);
    wordNode.addBackward(prev if prev is not None else BEGIN_TOKEN);
    return wordNode

def makeWordMap(source, baseMap):
    assert baseMap is not None
    
    rawWordList = [word.lower() for word in source.split(' ') if len(word) > 0]
    wordNodes = baseMap
    for k, word in enumerate(rawWordList):
        prevWord = None
        nextWord = None
        if (k-1 >= 0):  prevWord = rawWordList[k-1];
        if (k+1 < len(rawWordList)):    nextWord = rawWordList[k+1];
        if (word not in wordNodes.keys()):
            wordNodes[word] = WordNode(word);
        wordNodes[word] = grabTrigram(wordNodes[word], prevWord, nextWord);

    return wordNodes

def getWordMap():
    text = pullData('data/shakespeare')   
    wordMap = dict()
    for src in text:
        wordMap = makeWordMap(src, wordMap)
    return wordMap

def main():
    getWordMap()

if __name__ == "__main__":
	ret = main()
	if (ret is None):
		print "OK"
	else:
		print "Script didn't execute properly"