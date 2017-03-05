x, y = 10, 20
print(x, y)
x, y = y, x
print(x, y)

#1 (10, 20)
#2 (20, 10)
'''
  The assignment on the right seeds a new tuple. 
  While the left one instantly unpacks that (unreferenced) tuple to the names <a> and <b>.
  Once the assignment is through, the new tuple gets unreferenced and flagged for garbage collection. 
  The swapping of variables also occurs at eventually.
'''
