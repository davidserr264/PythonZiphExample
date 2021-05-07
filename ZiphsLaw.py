# Caution: The matplotlib plugin is required for this program to work
#To install matplotlib, open cmd and paste "pip install matplotlib"

import json
import itertools
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

fileNames=["Lord of The Rings","Little Women","Moby Dick","Empress Theresa"]
allWordsText=open("allwords.txt", "r", encoding='utf8') 
allWordsDict = dict()

# Takes WikiCorpus words and puts it into a dictionary. 
# Keys being words and values being their frequencies.
for line1 in allWordsText:
	line1 = line1.strip().split("\t")
	allWordsDict[line1[0]] = int(line1[1])

def checkForPunc(listofwords):	#runs through a list, removes puncuations and returns list.
	charToErase = '''">^:(*,~/"?_<];#[%)@}!.&'{$>'''
	revisedWord = ""
	listToReturn = []
	for string in listofwords:
		revisedWord = ""
		for x in string:
			if x not in charToErase:
				revisedWord = revisedWord + x
		listToReturn.append(revisedWord)
	return(listToReturn)

def createDict(filename):
	dictforfiles = dict()
	text = open(filename+".txt", "r", encoding='utf8') 
	for line2 in text:	#Takes text and puts it into a dictionary
		line2 = line2.strip().lower() 
		words = line2.split(" ") 
		checkedWords = checkForPunc(words)
		for word in checkedWords:	#Goes through every word, adds one for each time a word pops up
			if word in dictforfiles:
				dictforfiles[word] = dictforfiles[word] + 1
			else:
				dictforfiles[word] = 1
	listCreator(dictforfiles)

def listCreator(dictionary):	#Sorts dictionary and creates lists for graphing later
	sortedTextList = {key: val for key, val in sorted(dictionary.items(), key = lambda ele: ele[1], reverse = True)}
	global textWords, textValues
	textWords= list(sortedTextList)[0:200]
	textValues= list(sortedTextList.values())[0:200]
	allWordsWords= list(allWordsDict)[0:200]
	allWordsValues= list(allWordsDict.values())[0:200]

def graph(x,y):	#creates graphs word frequency with two lists
	y_pos = np.arange(len(x))
	plt.bar(y_pos, y, align='center', alpha=0.5)
	plt.xticks(y_pos, x)
	plt.ylabel('Word Frequency')
	plt.title(title)
	plt.show()

def main():	
	allWordsWords= list(allWordsDict)[0:200]
	allWordsValues= list(allWordsDict.values())[0:200]
	global title
	title= "Wikipedia"
	print("The top ten most frequent words are \n"+str(allWordsWords[0:10]))
	graph(allWordsWords,allWordsValues)
	for text in fileNames:	#Computes and displays graphs
		title = text
		createDict(text)
		print("The top ten most frequent words for "+text+" are \n"+str(textWords[0:10]))
		graph(textWords,textValues)

main() #Starts the code