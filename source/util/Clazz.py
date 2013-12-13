
class Clazz:

	@staticmethod
	def get_instance(clazz):
	    parts = clazz.split('.')
	    module = ".".join(parts[:-1])
	    m = __import__(module)
	    for comp in parts[1:]:
	        m = getattr(m, comp)            
	    return m
