"""
OracleBC - business rules for Oracle backend

A dynamic loaded class by SyncBC for 'type = Oracle' connection section.
Must implement method load() when as source and sync() when as destination database
"""

from dao.ConfigDAO import ConfigDAO
from dao.OracleDAO import OracleDAO

class OracleBC:

	def __init__(self, db_section, sync_section):
		self.c = ConfigDAO()
		self.db_section = db_section
		self.sync_section = sync_section
		self.conn = OracleDAO(self.c.config.get(db_section, "uri"), self.c.config.get(db_section, "username"), self.c.config.get(db_section, "password"))
		self.conn.execute_results_blob_as_bytes = True

	def load(self):
		return self.conn.execute(self.c.config.get(self.sync_section, "from query"))

	def sync(self, sync_section, row):
		pass
