# [on_true] if [expression] else [on_false]

 	
x = 10 if (y == 9) else 20
print(x)

'''
  assign 10 to x if y is 9, otherwise assign 20 to x. 
  We can though extend the chaining of operators if required.
'''

'''
  Likewise, we can do the same for class objects.
'''

x = (classA if y == 1 else classB)(param1, param2)

'''
   classA and classB are two classes and one of the class constructors would get called.
'''

# Evaluate smallest number
def small(a, b, c):
	return a if a <= b and a <= c else (b if b <= a and b <= c else c)
	
print(small(1, 0, 1))
print(small(1, 2, 2))
print(small(2, 2, 3))
print(small(5, 4, 3))
 
#Output
#0 #1 #2 #3

# use of a ternary operator with the list comprehension.

[m**2 if m > 10 else m**4 for m in range(50)]
 
#=> [0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401]
