"""
Oracle - implementation for acquire data from Oracle database

A dynamic loaded class by SyncBC for 'type = Oracle' connection section.
Must implement the method load()
"""

from dao.ConfigDAO import ConfigDAO
from dao.FileDAO import FileDAO
from dao.Oracle21DAO import OracleDAO
from util.Message import Debug

class Oracle21:

	def __init__(self, db_section, sync_section):
		self.c = ConfigDAO()
		self.db_section = db_section
		self.sync_section = sync_section
		self.conn = OracleDAO(self.c.config.get(db_section, "uri"), self.c.config.get(db_section, "username"), self.c.config.get(db_section, "password"))
		self.conn.execute_results_blob_as_bytes = True

	def load(self):
		if self.c.config.get(self.sync_section, "from query"):
			sql = self.c.config.get(self.sync_section, "from query")
			return self.conn.execute(sql)
		if self.c.config.get(self.sync_section, "from query file"):
			path = self.c.config.get(self.sync_section, "from query file")
			sql = FileDAO.read(path)
			Debug(sql)
			return self.conn.execute(sql)
		raise Exception("'from query' or 'from query file' must be defined")

