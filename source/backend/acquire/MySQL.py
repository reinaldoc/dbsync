"""
MySQL - Implementation for acquire data from MySQL database system

"""

from dao.ConfigDAO import ConfigDAO
from dao.MySqlDAO import MySqlDAO

class MySQL: 

	def __init__(self, db_section, sync_section):
		self.config_file = ConigDAO()
		self.db_section = db_section
		self.sync_section = sync_section
		self.conn = MySqlDAO(self.config_file.get(db_section, "uri"), self.config_file.get(db_section, "username"), self.config_file.get(db_section, "username"))
	
	def load(self):
		self.conn.execute(self.config_file.get(db_section, "from query"))