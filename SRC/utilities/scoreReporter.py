from utilities.wordFrequency import Words, WORDS_STR



NOT_CLEAR_SCORE_EACH_TIME = 0 # do not clear the previous score list when grade new file
CLEAR_SCORE_EACH_TIME = 1 #clear the previous score list when grade new file


class TextScore():
	def __init__(self, gender, wordScore, suffixScore, symbolScore):
		self.gender = gender
		self.wordScore = wordScore
		self.sufScore = suffixScore
		self.symScore = symbolScore
	
	def adjustWeight(wordWeight, sufWeight, symWeight):
		self.wordScore = self.wordScore*wordWeight
		self.sufScore = self.sufScore*sufWeight
		self.symScore = self.symScore*symWeight

class ScoreReporter():
	def __init__(self, tag = 0):
		self.tag = tag
		self.wordDict = dict()
		self.sufDict = dict()
		self.symDict = dict()
		self.textDict = dict()
		self.scoreList = []
	
	
	def getData(self, dict, data):
		dict.clear()
		with open(data, "r") as fo:
			for line in fo:
				w, p = line.split(',')
				dict[w] = float(p)
	
	def init(self, wordData, sufData, symData):
		self.getData(self.wordDict, wordData)
		self.getData(self.sufDict, sufData)
		self.getData(self.symDict, symData)
		
	def convert2Dict(self, wordFreq):
		for word in wordFreq:
			w, f = str(word).split(',')
			w = w.replace("(", "")
			w = w.replace("'", "")
			f = f.replace(")", "")
			self.textDict[w] = int(f)
	
	def grade(self, gender, text):
		if self.wordDict and self.sufDict and self.symDict:
			self._grade_(gender, text)
		else:
			print "please initialize ScoreReporter!"
	
	def _grade_(self, gender, text):
	
		self.textDict.clear()
		
		if self.tag == CLEAR_SCORE_EACH_TIME:
			del self.scoreList[:]
			self.scoreList[:] = []
		
		w = Words()
		f = w.wordFreqList(WORDS_STR, text)
		
		self.convert2Dict(f)
		
		
		wordScore = 0
		for key in set(self.textDict) & set(self.wordDict):
			wordScore += self.wordDict[key]*self.textDict[key]
		
		suffixScore = 0
		for key in set(self.textDict) & set(self.sufDict):
			suffixScore += self.sufDict[key]*self.textDict[key]
		
		symbolScore = 0
		for key in set(self.textDict) & set(self.symDict):
			symbolScore += self.symDict[key]*self.textDict[key]
		
		self.scoreList.append(TextScore(gender, wordScore, suffixScore, symbolScore))
		print "gender: %d, wordScore: %f, suffixScore: %f, symbolScore: %f" %(gender, wordScore, suffixScore, symbolScore)
		
	def save(self, fileName = "report"):
		scoreFile = fileName + "_score.txt"
		with open(scoreFile, "wb") as fo:
			for s in self.scoreList:
				line = "%f, %f, %f\n" %(s.wordScore, s.sufScore, s.symScore)
				fo.write(line)
		print scoreFile, "is saved!"
		targetFile = fileName + "_target.txt"
		with open(targetFile, "wb") as fo:
			for s in self.scoreList:
				line = "%d\n" %(s.gender)
				fo.write(line)
		print targetFile, " is saved!"
		
	
		