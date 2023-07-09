'''python program to convert tuple to a string '''
def convertTuple(tup):
	str = ''
	for item in tup:
		str = str + item
	return str

tuple = ('p', 'y', 't', 'h', 'o', 'n')
str = convertTuple(tuple)
print(str)
