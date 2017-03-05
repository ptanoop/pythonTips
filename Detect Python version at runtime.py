import sys

#Detect the Python version currently in use.
if not hasattr(sys, "hexversion") or sys.hexversion != 50660080:
print("Sorry, you aren't running on Python 3.5\n")
print("Please upgrade to 3.5.\n")
sys.exit(1)

#Print Python version in a readable format.
print("Current Python version: ", sys.version)

'''

  Alternatively, you can usesys.version_info >= (3, 5) to replacesys.hexversion!= 50660080 in the above code.
  It was a suggestion from one of the informed reader.
  
'''
