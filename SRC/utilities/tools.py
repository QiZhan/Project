def printLine():
	line = "#"
	for i in range(1,50):
		line += "#"
	print line
	
def tsplit(string, delimiters):
	delimiters = tuple(delimiters)
	stack = [string,]
	for delimiter in delimiters:
		for i, substring in enumerate(stack):
			substack = substring.split(delimiter)
			stack.pop(i)
			for j, _substring in enumerate(substack):
				stack.insert(i+j, _substring)
	return stack

def input_n(message):
	x = raw_input(message)
	try:
   		val = int(x)
	except ValueError:
   		print("That's not an int!")
   		exit()
	return x