
import ast

from dao.ConfigDAO import ConfigDAO
from util.Clazz import Clazz
from util.Strings import Strings

class SyncBC:

	@staticmethod
	def get_source_connection_section(sync_section):
		return ConfigDAO().config.get(sync_section, "from")

	@staticmethod
	def get_dest_connection_section(sync_section):
		return ConfigDAO().config.get(sync_section, "to")

	@staticmethod
	def get_connection_encoding(db_section):
		return ConfigDAO().config.get(db_section, "encoding")

	@staticmethod
	def get_source_connection_encoding(sync_section):
		return SyncBC.get_connection_encoding(SyncBC.get_source_connection_section(sync_section))

	@staticmethod
	def __get_handle(db_section, sync_section):
		type = ConfigDAO().config.get(db_section, "type")
		conn = Clazz.get_instance("controller", "%sBC" % type, "%sBC" % type)
		return conn(db_section, sync_section)

	@staticmethod
	def get_handle(db_section, sync_section):
		handle = SyncBC.__get_handle(db_section, sync_section)
		return handle

	@staticmethod
	def get_source_handle(sync_section):
		source_db_section = SyncBC.get_source_connection_section(sync_section)
		return SyncBC.get_handle(source_db_section, sync_section)

	@staticmethod
	def get_dest_handle(sync_section):
		dest_db_section = SyncBC.get_dest_connection_section(sync_section)
		return SyncBC.get_handle(dest_db_section, sync_section)

	@staticmethod
	def	get_field_types(sync_section):
		return ConfigDAO().get(sync_section, "to field type")

	@staticmethod
	def	get_update_template(sync_section):
		return ast.literal_eval(ConfigDAO().get(sync_section, "to update template"))

	@staticmethod
	def	get_match_template(sync_section):
		return ConfigDAO().get(sync_section, "to match template")

	@staticmethod
	def	get_match_query(sync_section, data):
		query = Strings.replaceList(SyncBC.get_match_template(sync_section), data, SyncBC.get_source_connection_encoding(sync_section))
		if query.find("%") != -1:
			print "WARN: can not build a query to find a id for: %s" % data
			return None
		return query

	@staticmethod
	def get_sync_sections():
		return ConfigDAO().get_sync_sections()
