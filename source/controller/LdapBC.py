
import ast
from dao.ConfigDAO import ConfigDAO
from dao.LdapDAO import LdapDAO
from controller.SyncBC import SyncBC
from util.Message import Debug
from util.Message import Info

class LdapBC:

	def __init__(self, db_section, sync_section):
		self.c = ConfigDAO()
		self.db_section = db_section
		self.sync_section = sync_section
		self.conn = LdapDAO(self.c.config.get(db_section, "uri"), self.c.config.get(db_section, "username"), self.c.config.get(db_section, "password"), self.c.config.get(self.db_section, "basedn"))
		self.update_template = SyncBC.get_update_template(sync_section)

	def load(self):
		return []

	def sync(self, sync_section, data):

		# make a query from a "to match template"
		query = SyncBC.get_match_query(sync_section, data)
		if query is None:
			return
		Info("Identity query: %s" % query)

		# try get a entry for the match query
		entry = self.conn.getSingleResult(query)
		if not entry:
			Info("No entry found for query: %s" % query)
			return

		#
		dn = entry.keys()[0]
		old_attributes = entry.values()[0]
		new_attributes = self.update_template.copy()

		# read non-string attributes map
		fields_type = SyncBC.get_field_types(sync_section)
		if fields_type:
			fields_type = ast.literal_eval(fields_type)

		# process rule template
		for key, value in new_attributes.items():
			# process non-string attributes
			if fields_type:
				if key in fields_type:
					value = data[self.get_template_id(value, len(data))]
					if value:
						new_attributes["%s;%s" % (key, fields_type.get(key))] = value
					del new_attributes[key]
					continue
			# process string attributes
			new_attributes[key] = Strings.replaceList(new_attributes.get(key), data, SyncBC.get_source_connection_encoding(sync_section))
			if new_attributes[key].find("%") != -1:
				del new_attributes[key]

		Info("DN for update: %s" % dn)
		Info("Rules for update: %s" % new_attributes)
		self.conn.modify(dn, new_attributes)

	def get_template_id(self, template, max_id):
		for i in range(max_id-1, -1, -1):
			if template.find("%%%s" % i) != -1:
				return i
