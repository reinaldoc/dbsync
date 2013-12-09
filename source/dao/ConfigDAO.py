
import ConfigParser

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
		self.config = ConfigParser.ConfigParser()
		self.config.read("dbsync.conf")

	def getSyncSections(self):
		result = []
		for section in self.config.sections():
			try:
				if self.config.get(section, "type") == "sync":
					result.append(section)
			except Exception, e:
				pass
		return result
