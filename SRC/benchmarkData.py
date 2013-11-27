from utilities.wordFrequency import Words, WORDS_FILE, WORDS_STR
from utilities.tools import printLine
from utilities.genderProbList import GenderProbList, GENDER_M, GENDER_F
from utilities.scoreReporter import ScoreReporter, NOT_CLEAR_SCORE_EACH_TIME
from utilities.blogReader import BlogReader
from utilities.resource import resource_delimiter
import sys
import getopt
from collections import Counter
import re

sufData = "_suffix_data.txt"
symData = "_symbol_data.txt"
wordData = "_word_data.txt"



def analyzeFreq(file):
	w = Words()
	f = w.wordFreqList(WORDS_FILE, file)
	printLine()
	print "the amount of unique words is ", len(f)
	printLine()
	print f
	w.save()



def main():

	r = raw_input("do you want to analyze the word frequency of files? Y/N:")
	str(r).lower()
	
	
	while( r == "y"):
		file = raw_input("enter the file name you want to analyze its word frequency:")
		analyzeFreq(file)
		r = raw_input("do you want to continue analyzing the word frequency of files? Y/N:")
		str(r).lower()
	
	
	probList = GenderProbList()
	
	maleFile = raw_input("enter the file name of male word frequency list:")
	probList.getWordFreqList(GENDER_M, maleFile)
	
	femaleFile = raw_input("enter the file name of female word frequency list:")
	probList.getWordFreqList(GENDER_F, femaleFile)
	
	probList.calProb()
	probList.save()
	
	maleFile = raw_input("enter the file name of male blog files:")
	femaleFile = raw_input("enter the file name of female word frequency list:")
	
	mbr = BlogReader()
	maleBlogList = mbr.read(resource_delimiter, maleFile)
	
	fbr = BlogReader()
	femaleBlogList = fbr.read(resource_delimiter, femaleFile)
	
	print "begin to reading blogs"
	print "begin to grade every blog!"
	
	sr = ScoreReporter(NOT_CLEAR_SCORE_EACH_TIME)
	sr.init(wordData, sufData, symData)
	
	for blog in maleBlogList:
		sr.grade(GENDER_M, str(blog))
	
	for blog in femaleBlogList:
		sr.grade(GENDER_F, str(blog))
	
	sr.save("result")
	print "grading is completed!"

if __name__ == "__main__":
    main()