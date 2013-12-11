
from dao.ConfigDAO import ConfigDAO
from dao.ConnectionDAO import ConnectionDAO
from util.Clazz import Clazz
from util.Message import Info
from util.Message import Debug

class ConnectionBC:

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
		return ConnectionBC.get_connection_encoding(ConnectionBC.get_source_connection_section(sync_section))

	@staticmethod
	def get_connection(db_section, sync_section):
		Debug("\nConnecting to '%s'" % db_section)
		Debug(ConfigDAO().config.items(db_section))
		conn = ConnectionDAO.get_connection(db_section, sync_section)
		conn.test()
		return conn

	@staticmethod
	def get_source_connection(sync_section):
		source_db_section = ConnectionBC.get_source_connection_section(sync_section)
		return ConnectionBC.get_connection(source_db_section, sync_section)

	@staticmethod
	def get_dest_connection(sync_section):
		dest_db_section = ConnectionBC.get_dest_connection_section(sync_section)
		return ConnectionBC.get_connection(dest_db_section, sync_section)

	@staticmethod
	def __get_handle(db_section, sync_section):
		type = ConfigDAO().config.get(db_section, "type")
		conn = Clazz.get_instance("controller", "%sBC" % type, "%sBC" % type)
		return conn(db_section, sync_section)

	@staticmethod
	def get_handle(db_section, sync_section):
		handle = ConnectionBC.__get_handle(db_section, sync_section)
		return handle

	@staticmethod
	def get_source_handle(sync_section):
		source_db_section = ConnectionBC.get_source_connection_section(sync_section)
		return ConnectionBC.get_handle(source_db_section, sync_section)

	@staticmethod
	def get_dest_handle(sync_section):
		dest_db_section = ConnectionBC.get_dest_connection_section(sync_section)
		return ConnectionBC.get_connection(dest_db_section, sync_section)
