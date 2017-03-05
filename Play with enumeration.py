#With enumerators, it’s easy to find an index while you’re inside a loop.
testlist = [10, 20, 30]
for i, value in enumerate(testlist):
	print(i, ': ', value)
 
#1-> 0 : 10
#2-> 1 : 20
#3-> 2 : 30
