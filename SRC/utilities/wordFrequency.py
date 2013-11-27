from collections import Counter
import re
import datetime
from tools import printLine


WORDS_FILE = 0 #if pass a file to wordFreqList
WORDS_STR = 1#if pass a string to wordFreqList

class Words():

	def __init__(self, tag = 0):
   	  	self.tag = tag
   	  	self.fileName = 0
		self.counter = 0
		self.wordsList = []
	

	def wordFreqList(self, fileType, file):
		words = 0
		if fileType == WORDS_FILE:
			self.fileName = file
			words = re.findall(r'\w+|[~!@$%^&*_{}]', open(self.fileName).read())
		elif fileType == WORDS_STR:
			words = re.findall(r'\w+|[~!@$%^&*_{}]', str(file))
		self.counter = Counter(words).most_common()
		self.wordsList = list(self.counter)
		return self.wordsList

	def save(self):
		fName, t = self.fileName.split(".")
		outputName = fName + "_word_freq.txt"
		with open(outputName, "wb") as fo:
			for w in self.wordsList:
				tmp = str(w) + "\n"
				fo.write(tmp)


	
