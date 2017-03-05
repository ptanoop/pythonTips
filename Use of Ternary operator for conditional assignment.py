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
