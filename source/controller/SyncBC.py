
import json

from dao.ConfigDAO import ConfigDAO
from util.Strings import Strings

class SyncBC:

	@staticmethod
	def	get_update_template(sync_section):
		return json.loads(ConfigDAO().get(sync_section, "to update template"))

	@staticmethod
	def	get_match_template(sync_section):
		return ConfigDAO().get(sync_section, "to match template")

	@staticmethod
	def	get_match_query(sync_section):
		query = Strings.replaceList(SyncBC.get_match_template(sync_section), row, ConnectionBC.get_source_connection_encoding(sync_section))
		if query.find("%") != -1:
			print "WARN: can not build a query to find a id for: " + str(row)
			return None
		return query

	@staticmethod
	def get_sync_sections():
		return ConfigDAO().get_sync_sections()
