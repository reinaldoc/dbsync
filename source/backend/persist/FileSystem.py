"""
FileSystem - implementation for persist data to FileSystem

A dynamic loaded class by SyncBC for 'type = FileSystem' connection section.
Must implement the methods sync() and flush()
"""

import ast
from dao.ConfigDAO import ConfigDAO
from dao.LdapDAO import LdapDAO
from controller.SyncBC import SyncBC
from util.Strings import Strings
from util.Message import Debug
from util.Message import Info

class FileSystem:

	def __init__(self, db_section, sync_section):
		self.c = ConfigDAO()
		self.db_section = db_section
		self.sync_section = sync_section
		self.path_template = ast.literal_eval(self.c.config.get(sync_section, "to path template"))
		self.field_content = int(self.c.config.get(sync_section, "to field content"))

	def flush(self):
		pass

	def sync(self, data):
		content = data[self.field_content]
		
		data[self.field_content] = ""
		data[0] = "%s" % data[0]
		print data

		#return

		# make the path from "to path template"
		path = Strings.replace_from_array(self.path_template, data)
		print path

