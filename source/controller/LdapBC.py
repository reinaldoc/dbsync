"""
LdapBC - business rules for Ldap backend

A dynamic loaded class by SyncBC for 'type = Ldap' connection section.
Must implement method load() when as source and sync() when as destination database
"""

from dao.ConfigDAO import ConfigDAO
from dao.LdapDAO import LdapDAO
from controller.SyncBC import SyncBC
from util.Strings import Strings
from util.Message import Debug
from util.Message import Info

class LdapBC:

	def __init__(self, db_section, sync_section):
		self.c = ConfigDAO()
		self.db_section = db_section
		self.sync_section = sync_section
		self.conn = LdapDAO(self.c.config.get(db_section, "uri"), self.c.config.get(db_section, "username"), self.c.config.get(db_section, "password"), self.c.config.get(self.db_section, "basedn"))
		self.update_template = SyncBC.get_update_template(sync_section)
		self.binary_attrs = SyncBC.get_connection_binary_attrs(db_section)

		# rename binary attributes from "to update template"
		for key, value in self.update_template.items():
			if key in self.binary_attrs:
				self.update_template["%s;binary" % key] = self.update_template[key]
				del self.update_template[key]

	def load(self):
		return []

	def flush(self):
		pass

	def sync(self, sync_section, data):
	
		# make a query from a "to match template"
		query = SyncBC.get_match_query(sync_section, data)
		if query is None:
			return
		Info("\nIdentity query: %s" % query)

		# try get a entry for the match query
		# retrieve only attributes to be changed from "to update template"
		# (this is mandatory but current attributes will be removed)
		entry = self.conn.getSingleResult(query, self.update_template.keys())
		if not entry:
			Info("No entry found for query: %s" % query)
			return

		# set variables
		dn = entry.keys()[0]
		old_attributes = entry.values()[0]

		# process "to update template"
		new_attributes = self.update_template.copy()
		for key, value in new_attributes.items():
			# attributes to be removed from LDAP
			if value is None:
				del new_attributes[key]
				continue
		
			# process binary attributes
			if key.split(";")[0] in self.binary_attrs:
				value = data[self.__get_template_id(value, len(data))]
				if value:
					new_attributes[key] = [value]
				else:
					del new_attributes[key]
				continue

			# process string attributes
			new_attributes[key] = Strings.replace_from_array(new_attributes.get(key), data, SyncBC.get_source_connection_encoding(sync_section))
			if new_attributes[key].find("%") != -1:
				del new_attributes[key]
			else:
				new_attributes[key] = [new_attributes[key]]

		Info("DN for update: %s" % dn)
		Debug("Current attributes: %s" % old_attributes)
		Debug("Rules for update:   %s" % new_attributes)
		self.conn.modify(dn, old_attributes, new_attributes)

	def __get_template_id(self, template, max_id):
		for i in range(max_id-1, -1, -1):
			if template.find("%%%s" % i) != -1:
				return i
