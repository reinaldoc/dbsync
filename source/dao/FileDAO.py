"""

FileDAO - provides data file handling from the file system

"""
import os

class FileDAO(object):

	@staticmethod
	def writeToFile(fileName, content):
		f = open(fileName, "w")
		f.write(content)
		f.close()

	@staticmethod
	def writeToBinaryFile(fileName, content):
		if content is None:
			return
		f = open(fileName, "wb")
		f.write(content)
		f.close()

	@staticmethod
	def makedirs(path):
		print ("----------" + path)
		path = os.path.dirname(path)
		print ("----------" + path)

		try:
			os.makedirs(path)
		except OSError as e:
			print(e)
  
	@staticmethod
	def read(filename):
		f = open(filename, "r")
		data = f.read()
		f.close()
		return data
    