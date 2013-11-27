from utilities.resource import resource_delimiter
import itertools as it

class BlogReader():
	def __init__(self, tag = 0):
		self.tag = tag
		self.blogList = []
		
	'''def _read_(self, delimiter, fileName):
		with open(fileName, "r") as fo:
			for line in fo:
				if line.startswith(delimiter):
					print "start"'''
					
	def read(self, delimiter, fileName):
		
		del self.blogList[:]
		self.blogList[:] = []
		
		with open(fileName,'r') as fo:
			for key,group in it.groupby(fo,lambda line: line.startswith(delimiter)):	
				if not key:
					self.blogList.append(list(group))	
		return self.blogList
		
