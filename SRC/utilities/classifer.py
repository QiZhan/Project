from utilities.wordFrequency import Words

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

class Classifer():
	def __init__(self, tag = 0):
		self.tag = tag
		self.wordDict = dict()
		self.sufDict = dict()
		self.symDict = dict()
		self.textDict = dict()
		self.ScoreList = []
	
	
	def getData(self, dict, data):
		dict.clear()
		fo = open(data, "r")
		for line in fo:
			w, p = line.split(',')
			dict[w] = float(p)
	
	def init(self, wordData, sufData, symData):
		self.getData(self.wordDict, wordData)
		self.getData(self.sufDict, sufData)
		self.getData(self.symDict, symData)
		
	def convert2Dict(self, wordFreq):
		for word in wordFreq:
			#print word
			w, f = str(word).split(',')
			w = w.replace("(", "")
			w = w.replace("'", "")
			f = f.replace(")", "")
			self.textDict[w] = int(f)
	
	def classify(self, gender, text):
	
		w = Words(text)
		f = w.wordFreqList()
		
		
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
		
		self.ScoreList.append(TextScore(gender, wordScore, suffixScore, symbolScore))
		
	def save(self):
		for s in self.ScoreList:
			print s.gender, s.wordScore, s.sufScore, s.symScore
		pass