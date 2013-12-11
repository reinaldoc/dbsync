
class Clazz:

	@staticmethod
	def get_instance(package, filename, classname):
		module = __import__("%s.%s" % (package, filename))	# import
		module = getattr(module, "%s" % classname)			# filename
		module = getattr(module, "%s" % classname)			# classname
		return module
