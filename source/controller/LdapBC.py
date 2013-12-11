
from dao.LdapDAO import dao.LdapDAO
from controller.SyncBC import SyncBC

class LdapBC:

	def __init__(self, db_section, sync_section):
		self.db_section = db_section
		self.sync_section = sync_section
		self.conn = LdapDAO(db_section, sync_section)
		self.update_template = SyncBC.get_update_template(sync_section)

	def load(self):
		return []

	def sync(self, sync_section, row):
		pass

	def merge(self):
		Info("Rules for update: %s" % update_rules)

	def trash(self):
		# make a query from a "to match template"
		query = SyncBC.get_match_query()
		if query is None:
			continue
		Info("")
		Info("Identity query: %s" % query)
		
		continue

		update_rules = update_template.copy()
		for key, value in update_rules.items():
			if c.get(sync_section, "to field type"):
				if key in c.get(sync_section, "to field type"):
					newValue = row[2]
					del update_rules[key]
					fieldMap = json.loads(c.get(sync_section, "to field type"))
					update_rules["%s;%s" % (key, fieldMap.get(key))] = newValue
					continue
			update_rules[key] = Strings.replaceList(update_rules.get(key), row, c.get(origin, "encoding"))
			if update_rules[key].find("%") != -1:
				del update_rules[key]
