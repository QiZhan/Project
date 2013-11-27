from utilities.wordFrequency import Words
from utilities.tools import printLine
from utilities.genderProbList import GenderProbList, ENUM_M, ENUM_F
from utilities.classifer import Classifer
import sys
import getopt

sufData = "_suffix_data.txt"
symData = "_symbol_data.txt"
wordData = "_word_data.txt"

def input_n(message):
	x = raw_input(message)
	try:
   		val = int(x)
	except ValueError:
   		print("That's not an int!")
   		exit()
	return x

def analyzeFreq(file):
	w = Words(file)
	f = w.wordFreqList()
	printLine()
	print "the amount of unique words is ", len(f)
	printLine()
	print f
	w.save()



def main():

	'''r = raw_input("do you want to analyze the word frequency of files? Y/N:")
	str(r).lower()
	
	
	while( r == "y"):
		f = raw_input("enter the file name you want to analyze:")
		analyzeFreq(f)
		r = raw_input("do you want to continue analyzing the word frequency of files? Y/N:")
		str(r).lower()

	
	probList = GenderProbList()
	
	maleFile = raw_input("enter the file name of male word frequency list:")
	probList.getWordFreqList(ENUM_M, maleFile)
	
	femaleFile = raw_input("enter the file name of female word frequency list:")
	probList.getWordFreqList(ENUM_F, femaleFile)

	probList.calProb()
	probList.save()
	'''
	
	c = Classifer()
	c.init(wordData, sufData, symData)
	c.classify("f", "male.txt")
	c.save()
	

if __name__ == "__main__":
    main()