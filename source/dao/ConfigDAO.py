"""
ConfigDAO - provide access to configuration file

A singleton class to provide access and make validation to configuration file
"""

import ConfigParser, os

class ConfigDAO(object):

	_construct = False
	_instance = None

	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(ConfigDAO, cls).__new__(cls)
		return cls._instance

	def __init__(self):
		# Check if run constructor
		if ConfigDAO._construct:
			return
		ConfigDAO._construct = True

		# Initialize
		self.sync_sections = None
		self.config = ConfigParser.ConfigParser()
		self.config.read("%s/dbsync.conf" % os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
		self.__validate_config()

	def __validate_config(self):
		self.__validate_required_attributes()

	def __validate_required_attributes(self):
		for sync_section in self.get_sync_sections():
			try:
				self.config.get(sync_section, "from")
				self.config.get(sync_section, "from query")
				self.config.get(sync_section, "to")
				self.config.get(sync_section, "to update template")
			except ConfigParser.NoOptionError, e:
				print("Attribute '%s' is mandatory for synchronization '%s'. Aborting..." % (e[0], e[1]))
				exit()

	def get_sync_sections(self):
		if self.sync_sections is not None:
			return self.sync_sections

		self.sync_sections = []
		for section in self.config.sections():
			try:
				if self.config.get(section, "type") == "sync":
					self.sync_sections.append(section)
			except ConfigParser.NoOptionError, e:
				pass
		return self.sync_sections

	def get(self, section, key):
		""" get value by section/attribue from a ConfigParser object. Returns
		None if section or attribute does not exist"""
		try:
			return self.config.get(section, key)
		except ConfigParser.NoOptionError, e:
			return None

