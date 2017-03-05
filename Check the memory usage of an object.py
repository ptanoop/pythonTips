import sys
x=1
print(sys.getsizeof(x))
 
#-> 28
# In Python 2.7, a 32-bit integer consumes 24-bytes whereas it utilizes 28-bytes in Python 3.5
