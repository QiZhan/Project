from utilities.wordFrequency import Words, WORDS_FILE, WORDS_STR
from utilities.tools import printLine
from utilities.genderProbList import GenderProbList, GENDER_M, GENDER_F, GENDER_UNKNOWN
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

''''NOTE: the delimiter of each blog is ###'''

def main():
	
	file = raw_input("please specify the text that will be graded: ")
	
	br = BlogReader()
	blogList = br.read(resource_delimiter, file)
	
	print "begin to reading blogs"
	print "begin to grade every blog!"
	
	sr = ScoreReporter(NOT_CLEAR_SCORE_EACH_TIME)
	sr.init(wordData, sufData, symData)
	
	for blog in blogList:
		sr.grade(GENDER_UNKNOWN, str(blog))
	
	print "grade is completed!"

	sr.save(file)
	
	
if __name__ == "__main__":
    main()