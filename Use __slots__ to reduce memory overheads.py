import sys
class FileSystem(object):
 
	def __init__(self, files, folders, devices):
		self.files = files
		self.folders = folders
		self.devices = devices
 
print(sys.getsizeof( FileSystem ))
 
class FileSystem1(object):
 
	__slots__ = ['files', 'folders', 'devices']
	
	def __init__(self, files, folders, devices):
		self.files = files
		self.folders = folders
		self.devices = devices
 
print(sys.getsizeof( FileSystem1 ))
 
#In Python 3.5
#1-> 1016
#2-> 888

'''
  use __slots__ when the memory overhead of a class is unnecessarily large. 
  Do it only after profiling the application. Otherwise, you’ll make the code difficult to change and with no real benefit.
'''
