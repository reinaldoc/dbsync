"""
Strings - a class to string related code

"""
class Strings(object):

	@staticmethod
	def is_string(string):
		if type(string) == type("str"):
			return True
		return False

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

	@staticmethod
	def capitalize(string):
		"""
		Receive a string and returns a copy of that with all words capitalized,
		except the prepositions.
		"""
		if not Strings.is_string(string):
			return string

		prepositions = (" Da ", " Das ", " Do ", " Dos ", " De ", " Du ", " E ")
		string = string.title()
		for prep in prepositions:
			string = string.replace(prep, prep.lower())

		return string

	@staticmethod
	def replace_string(string, s_from, s_to):
		"""
		Replace strings, receiving the "actual" string and replacing it as "to" string.
		Also, converts any entry type to string.
		"""
		try:
			string = string.replace(s_from, s_to)
		except Exception as erro:
			print(erro)
		
		return string
