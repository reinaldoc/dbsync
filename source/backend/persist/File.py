"""
File - implementation for persist data (files) to FileSystem

A dynamic loaded class by SyncBC for 'type = FileSystem' connection section.
Must implement the methods sync() and flush()
"""

import ast
import collections
from dao.ConfigDAO import ConfigDAO
from dao.FileDAO import FileDAO
from util.Strings import Strings

class File:

	def __init__(self, db_section, sync_section):
		self.c = ConfigDAO()
		self.db_section = db_section
		self.sync_section = sync_section
		self.path_template = ast.literal_eval(self.c.config.get(sync_section, "to path template"))
		self.field_content = int(self.c.config.get(sync_section, "to field content"))
		self.mime_types = self.__loadMimeTypes()

	def __loadMimeTypes(self):
		content = FileDAO.read("/etc/mime.types").replace("\t", " ").split("\n")
		#for element in range(len(content)):
			#key = content[
			#print(content[element].split(" ",1))
			#key = content[element].
		
	def flush(self):
		pass

	def sync(self, data):
		content = data[self.field_content]
		del data[self.field_content]

		# make the path from "to path template"
		path = Strings.replace_from_array(self.path_template, data)
		# print("PATH: " + path)
		
		FileDAO.makedirs(path)
		FileDAO.writeToBinaryFile(path, content)

		if self.c.config.get("General", "debug"):
			print("File '%s' was saved." % path)
