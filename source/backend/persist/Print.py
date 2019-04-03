"""
Print - implementation for persist data to STDOUT

A dynamic loaded class by SyncBC for 'type = Print' connection section.

Must implement the methods sync() and flush()
"""

from dao.ConfigDAO import ConfigDAO
from controller.SyncBC import SyncBC
from util.Strings import Strings
from util.Message import Debug
from util.Message import Info

class Print:

	def __init__(self, db_section, sync_section):
		self.c = ConfigDAO()
		self.db_section = db_section
		self.sync_section = sync_section
		self.count = 1

	def flush(self):
		pass

	def sync(self, data):
		query = SyncBC.get_match_query(self.sync_section, data)
		if query is not None:
			print(query)
		else:
			print("%s: %s" % (self.count, data))
			self.count += 1

