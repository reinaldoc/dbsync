"""
Strings - a class to string related code

"""
class Strings(object):

	@staticmethod
	def replace_from_array(string, array=[], from_encoding="utf-8", to_encoding="utf-8"):
		"""
		Receives a string template like 'My name is %0 and I am %1 years old' and
		a list with values to be replaced, like ['Tiago Neves', '29']. This
		example produces the string 'My name is Tiago Neves and I am 29 years old'
		"""
		for i in range(len(array)-1, -1, -1):
			data = array[i]
			if data:
				if type(data) == type('string'):
					data = data.decode(from_encoding).encode(to_encoding)
				string = string.replace("%%%s" % i, data)
		return string
