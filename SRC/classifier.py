from sklearn import datasets
from sklearn import svm
import numpy


class Classifier():
	
	def __init__(self, tag = 0):
		self.tag = tag
		self.fileName = 0
		self.predict = 0
		
	'''predictFile is the score file you want to predict, \
		note it must be processed by textScore.py'''
	def _predict_(self, scoreFile, targetFile, predictFile):
		
		self.fileName = predictFile
		
		mydata = numpy.genfromtxt(fname=scoreFile, delimiter=",")
		mytarget = numpy.genfromtxt(fname=targetFile, delimiter=",")
		testdata= numpy.genfromtxt(fname=predictFile, delimiter=",")
		
		clf = svm.SVC(C=100.0, cache_size=200, class_weight=None, coef0=0.0, degree=3,\
  		gamma=0.001, kernel='rbf', max_iter=-1, probability=False,\
  		random_state=None, shrinking=True, tol=0.001, verbose=False)
		
		clf.fit(mydata, mytarget)
		self.predict = clf.predict(testdata)
	
	def save(self):
		fName, t = self.fileName.split(".")
		outputName = fName + "_predict_result.txt"
		with open(outputName,"wb") as fo:
			for p in self.predict:
				s = str(p) + "\n"
				fo.write(s)
    
def main():
	
	scoreFile = raw_input("please specify score file: ")
	targetFile = raw_input("please specify taget file: ")
	predictFile = raw_input("please specify the file you want to predict: ")
	
	c = Classifier()
	c._predict_(str(scoreFile), str(targetFile), str(predictFile))
	c.save()
	
	
if __name__ == "__main__":
    main()