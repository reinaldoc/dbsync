 
"""
Ldap - Implementation for acquire data from LDAP

"""

from dao.ConfigDAO import ConfigDAO
from dao.LdapDAO import LdapDAO
from controller.SyncBC import SyncBC

class Ldap: 

	def __init__(self, db_section, sync_section):
		self.c = ConfigDAO()
		self.db_section = db_section
		self.sync_section = sync_section
		self.conn = LdapDAO(self.c.config.get(db_section, "uri"), self.c.config.get(db_section, "username"), self.c.config.get(db_section, "password"), self.c.config.get(self.db_section, "basedn"))
	
	def load(self):
		attrs = SyncBC.get_config_as_list(self.sync_section, "from attrs")
		ldap_data = self.conn.search(self.c.get(self.sync_section, "from query"), self.c.config.get(self.db_section, "basedn"), attrs)
		result = []
		for dn in ldap_data.keys():
			data = []
			for attr in attrs:
				try:
					data.append(ldap_data[dn].get(attr)[0])
				except:
					data.append("")
			result.append(data)
		return result
