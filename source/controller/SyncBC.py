"""
SyncBC - support code to synchronization

Load dynamically backends and converters processor support code
"""

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
	def get_connection_binary_attrs(db_section):
		binary_attrs = ConfigDAO().get(db_section, "binary attrs")
		if binary_attrs:
			return ast.literal_eval(binary_attrs)
		return []

	@staticmethod
	def __get_handle(db_section, sync_section):
		type = ConfigDAO().config.get(db_section, "type")
		conn = Clazz.get_instance("controller.%s.%s" % ( "%sBC" % type, "%sBC" % type))
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
		query = Strings.replace_from_array(SyncBC.get_match_template(sync_section), data, SyncBC.get_source_connection_encoding(sync_section))
		if query.find("%") != -1:
			print "WARN: can not build a query to find a id for: %s" % data
			return None
		return query

	@staticmethod
	def get_sync_sections():
		return ConfigDAO().get_sync_sections()

	@staticmethod
	def get_convert_data(sync_section):
		try:
			convert_data = ConfigDAO().get(sync_section, "convert data")
			if convert_data:
				return ast.literal_eval(convert_data)
		except SyntaxError, e:
			print("Error parsing convert data from '%s': %s" % (sync_section, e[1][3]))
		return []

	@staticmethod
	def convert(sync_section, data):
		# unpack variables
		rules = SyncBC.get_convert_data(sync_section)
		if not rules:
			return data

		if type(rules[0]) != type(()):
			rules = (rules,)

		for rule in rules:
			data = SyncBC.__convert(data, rule)

		return data

	@staticmethod
	def __convert(data, rule):
		data_id = rule[0]
		convert_class = rule[1]
		class_args = rule[2:]

		# process data conversion
		callable_converter = SyncBC.__get_convert_instance(rule[1])
		if data_id == -1:
			data = callable_converter(data, class_args).get_value()
		else:
			data[data_id] = callable_converter(data[data_id], class_args).get_value()

		return data

	@staticmethod
	def __get_convert_instance(clazz):
		return Clazz.get_instance("controller.convert.%s.%s" % (clazz, clazz))
