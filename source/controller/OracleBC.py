
from dao.OracleDAO import OracleDAO

class OracleBC:

	def __init__(self, db_section, sync_section):
		self.db_section = db_section
		self.sync_section = sync_section
		self.conn = OracleDAO(db_section, sync_section)

	def load(self):
		return []

	def sync(self, sync_section, row):
		pass
