import re
from tools import tsplit
import datetime
from resource import resource_suffix_list, resource_symbol_lst


GENDER_M = 1 #male
GENDER_F = 0 #femle
GENDER_UNKNOWN = 2 #unknown


class WordFreq():

	def __init__(self, word, freq):
		self.word = word
		self.freq = freq
		
	def __eq__(self, other):
		return self.word == other.word

	def __ne__(self, other):
		return not self.__eq__(other)
        
class WordProb():
	
	def __init__(self, word, mProb, fProb):
		self.word = word
		self.mProb = mProb
		self.fProb = fProb
		self.weightedProb = 0
	
	def calWeightedProb(self):
		self.weightedProb = self.mProb - self.fProb


class ProbList():
	def __init__(self, mDict, fDict):
		self.mDict = mDict
		self.fDict = fDict
		self.genderProbList = []
		
	def sortList(self):
		self.genderProbList.sort(key = lambda WordProb : (float(WordProb.mProb)))
		
	def _calProb_(self):
		pass
	
	def _save_(self, name):
		self.sortList()
		'''outputName = name + "ProbList" + str(datetime.datetime.now().strftime("_%d_%m_%y")) + ".txt"
		fo = open(outputName, "wb")
		for p in self.genderProbList:
			tmp = p.word + "," + str(p.mProb) + "," + str(p.fProb)+ "\n"
			fo.write(tmp)'''
		
		outputName =  "_" + name + "_data" + ".txt"
		#fo = open(outputName, "wb")
		with open(outputName, 'w') as fo:
			for p in self.genderProbList:
				p.calWeightedProb()
				tmp = p.word + "," + str(p.weightedProb) + "\n"
				fo.write(tmp)
		
		print "save %s data into %s " %(name, outputName)



class SuffixProbList(ProbList):
	def __init__(self, mDict, fDict, suffixList):
		ProbList.__init__(self, mDict, fDict)
		self.sufList = suffixList
		self.sufFemDict = dict()
		self.sufMalDict = dict()
	
	def convertList2Dict(self):
		for suf in self.sufList:
			self.sufFemDict[suf] = 0
			self.sufMalDict[suf] = 0
	
	def calProb(self):
		self.convertList2Dict()

		
		for suf in self.sufList:
			for key in set(self.mDict):
				if key.endswith(suf):
					self.sufMalDict[suf] += self.mDict[key]
					
		for suf in self.sufList:
			for key in set(self.fDict):
				if key.endswith(suf):
					self.sufFemDict[suf] += self.fDict[key]
		
		for key in set(self.sufFemDict) & set(self.sufMalDict):
			mProb = 0
			fProb = 0
			if (self.sufFemDict[key] == 0) and (self.sufMalDict[key] != 0):
				mProb = 1
			elif (self.sufMalDict[key] == 0) and (self.sufFemDict[key] != 0):
				fProb = 1
			elif (self.sufFemDict[key] != 0) and (self.sufMalDict[key] != 0):
				mProb = float(float(self.sufMalDict[key])/(float(self.sufMalDict[key]) + float(self.sufFemDict[key])))
				fProb = 1 - mProb
			self.genderProbList.append(WordProb(key, mProb, fProb))		
		
		
	def save(self):
		self._save_("suffix")
		
class SymbolProbList(ProbList):
	def __init__(self, mDict, fDict, symList):
		ProbList.__init__(self, mDict, fDict)
		self.symList = symList
		#self.sufDict = dict()
		self.symFemDict = dict()
		self.symMalDict = dict()
	
	def convertList2Dict(self):
		for sym in self.symList:
			self.symFemDict[sym] = 0
			self.symMalDict[sym] = 0
	
	def calProb(self):
		self.convertList2Dict()

		
		for sym in self.symList:
			for key in set(self.mDict):
				if key.find(sym) != -1:
					self.symMalDict[sym] += self.mDict[key]
					
		for sym in self.symList:
			for key in set(self.fDict):
				if key.find(sym) != -1:
					self.symFemDict[sym] += self.fDict[key]
		
		for key in set(self.symFemDict) & set(self.symMalDict):
			mProb = 0
			fProb = 0
			if (self.symFemDict[key] == 0) and (self.symMalDict[key] != 0):
				mProb = 1
			elif (self.symMalDict[key] == 0) and (self.symFemDict[key] != 0):
				fProb = 1
			elif (self.symFemDict[key] != 0) and (self.symMalDict[key] != 0):
				mProb = float(float(self.symMalDict[key])/(float(self.symMalDict[key]) + float(self.symFemDict[key])))
				fProb = 1 - mProb
			self.genderProbList.append(WordProb(key, mProb, fProb))		
		
		
	def save(self):
		self._save_("symbol")
	



		
class WordProbList(ProbList):
	def __init__(self, mDict, fDict):
		ProbList.__init__(self, mDict, fDict)

	
	def calProb(self):
		mProb = 0
		fProb = 0
		for key in set(self.mDict) & set(self.fDict):
			mProb = float(float(self.mDict[key])/(float(self.mDict[key]) + float(self.fDict[key])))
			fProb = 1 - mProb
			self.genderProbList.append(WordProb(key, mProb, fProb))
		
		mKeys=set(self.mDict.keys())
		fKeys=set(self.fDict.keys())
		male_exclusive = mKeys - fKeys
		female_exclusive = fKeys - mKeys
		
		for m in male_exclusive:
			self.genderProbList.append(WordProb(m, 1, 0))
		
		for f in female_exclusive:
			self.genderProbList.append(WordProb(f, 0, 1))
			
	def save(self):
		self._save_("word")

		

class GenderProbList():

	def __init__(self, maleWordList = [], femaleWordList = []):
		self.mDict = dict()
		self.fDict = dict()
		self.wordProbList = 0
		self.sufProbList = 0
		self.symProbList = 0
	
	
	def getMaleWordList(self, listFlie):
		self.mDict.clear()
		with open(listFlie, "r") as fo:
			for line in fo:
				w, f = line.split(',')
				w = w.replace("(", "")
				w = w.replace("'", "")
				f = f.replace(")", "")
				self.mDict[w] = int(f)
		print "got male word frequency list!"
	
	def getFemaleWordList(self, listFlie):
		self.fDict.clear()
		with open(listFlie, "r") as fo:
			for line in fo:
				w, f = line.split(',')
				w = w.replace("(", "")
				w = w.replace("'", "")
				f = f.replace(")", "")
				self.fDict[w] = int(f)
		print "got female word frequency list!"
	
	def getWordFreqList(self, gender, listFlie):
		if gender == GENDER_M:
			self.getMaleWordList(listFlie)
		elif gender == GENDER_F:
			self.getFemaleWordList(listFlie)
			
	
	
	def calProb(self):
		self.wordProbList = WordProbList(self.mDict, self.fDict)
		self.wordProbList.calProb()
		
		self.suffixProbList = SuffixProbList(self.mDict, self.fDict, resource_suffix_list)
		self.suffixProbList.calProb()
		
		self.symProbList = SymbolProbList(self.mDict, self.fDict, resource_symbol_lst)
		self.symProbList.calProb()
	
	def save(self):
		self.wordProbList.save()
		self.suffixProbList.save()
		self.symProbList.save()
