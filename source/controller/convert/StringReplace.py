"""
StringReplace - a converter to replace section(s) of a string to strings passed
as parameters

"""

from dao.ImageDAO import ImageDAO
from util.Strings import Strings

class StringReplace(object):

	def __init__(self, data, args=()):
		"""
		Receive the data to be converted and parameters.
		"""
		self.value = data
		if not data:
			print("WARN: data invalid parameters")
			return

		actual_string = args[0]
		to_string = args[1]		

		try:
			self.value = Strings.replace_string(data, actual_string, to_string)
		except Exception as erro:
			print(erro)

	def get_value(self):
		return self.value
