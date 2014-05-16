"""
SyncBC - support code to synchronization

Load dynamically backends and converters processor support code
"""

''' 
ast - abstract syntax trees. Analyzes a Python expression
and permits the conversion, by ast.literal_eval(), to a
Python object.
'''
import ast

from dao.ConfigDAO import ConfigDAO
from util.Clazz import Clazz
from util.Strings import Strings

class SyncBC:

	'''
	Informs the location (packages) where the 
	'''
	BACKEND_ACQUIRE_PACKAGE = "backend.acquire"
	BACKEND_PERSIST_PACKAGE = "backend.persist"

	@staticmethod
	def get_acquire_connection_section(sync_section):
		return ConfigDAO().config.get(sync_section, "from")

	@staticmethod
	def get_persist_connection_section(sync_section):
		return ConfigDAO().config.get(sync_section, "to")

	@staticmethod
	def get_connection_encoding(db_section):
		return ConfigDAO().config.get(db_section, "encoding")

	@staticmethod
	def get_acquire_connection_encoding(sync_section):
		return SyncBC.get_connection_encoding(SyncBC.get_acquire_connection_section(sync_section))

	@staticmethod
	def get_connection_binary_attrs(db_section):
		binary_attrs = ConfigDAO().get(db_section, "binary attrs")
		if binary_attrs:
			return ast.literal_eval(binary_attrs)
		return []

	@staticmethod
	def __get_backend(db_section, sync_section, backend_package):
		type = ConfigDAO().config.get(db_section, "type")
		conn = Clazz.get_instance("%s.%s.%s" % (backend_package, type, type))
		return conn(db_section, sync_section)

	@staticmethod
	def get_acquire_backend(sync_section):
		acquire_db_section = SyncBC.get_acquire_connection_section(sync_section)
		return SyncBC.__get_backend(acquire_db_section, sync_section, SyncBC.BACKEND_ACQUIRE_PACKAGE)

	@staticmethod
	def get_persist_backend(sync_section):
		persist_db_section = SyncBC.get_persist_connection_section(sync_section)
		return SyncBC.__get_backend(persist_db_section, sync_section, SyncBC.BACKEND_PERSIST_PACKAGE)

	@staticmethod
	def get_field_types(sync_section):
		return ConfigDAO().get(sync_section, "to field type")

	@staticmethod
	def get_update_template(sync_section):
		return ast.literal_eval(ConfigDAO().get(sync_section, "to update template"))

	@staticmethod
	def get_match_template(sync_section):
		return ConfigDAO().get(sync_section, "to match template")

	@staticmethod
	def get_match_query(sync_section, data):
		query = Strings.replace_from_array(SyncBC.get_match_template(sync_section), data, SyncBC.get_acquire_connection_encoding(sync_section))
		if query.find("%") != -1:
			print ("WARN: can not build a query to find a id for: %s" % data)
			return None
		return query

	@staticmethod
	def get_sync_sections():
		return ConfigDAO().get_sync_sections()

	@staticmethod
	def get_converters(sync_section):
		try:
			converters = ConfigDAO().get(sync_section, "converters")
			if converters:
				return ast.literal_eval(converters)
		except SyntaxError, e:
			print("Error parsing convert data from '%s': %s" % (sync_section, e[1][3]))
		return []

	@staticmethod
	def convert(sync_section, data):
		rules = SyncBC.get_converters(sync_section)
		if not rules:
			return data

		if type(rules[0]) != type(()):
			rules = (rules,)

		for rule in rules:
			data = SyncBC.__convert(data, rule)

		return data

	@staticmethod
	def __convert(data, rule):
		# unpack variables
		data_id = rule[0]
		converter_class = rule[1]
		converter_args = rule[2:]

		# process data conversion
		callable_converter = SyncBC.__get_convert_instance(converter_class)
		if data_id == -1:
			data = callable_converter(data, converter_args).get_value()
		else:
			data[data_id] = callable_converter(data[data_id], converter_args).get_value()

		return data

	@staticmethod
	def __get_convert_instance(clazz):
		return Clazz.get_instance("converter.%s.%s" % (clazz, clazz))
