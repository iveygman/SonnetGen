import re
import os
import os.path

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

def makeWordMap(source, baseMap):
    assert baseMap is not None
    
    wordList = [word for word in source.split(' ') if len(word) > 0]
    for k,word in enumerate(wordList):
        
        
    return baseMap

def main():
    text = pullData('data/shakespeare')   
    wordMap = dict()
    for src in text:
        wordMap = makeWordMap(src, wordMap)


if __name__ == "__main__":
	ret = main()
	if (ret is None):
		print "OK"
	else:
		print "Script didn't execute properly"