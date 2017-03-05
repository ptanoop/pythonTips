import sys
 
x=1001
print(sys.getrecursionlimit())
 
sys.setrecursionlimit(x)
print(sys.getrecursionlimit())
 
#1-> 1000
#2-> 1001

#Python restricts recursion limit to 1000. We can though reset its value.
