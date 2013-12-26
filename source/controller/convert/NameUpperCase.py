"""
NameUpperCase - a converter to change first letter for each space separated
string to uppercase

"""

from dao.ImageDAO import ImageDAO
from util.Strings import Strings

class NameUpperCase(object):

	def __init__(self, data, args=()):
		"""
		Receive the data to be converted and parameters.
		"""
		self.value = data

		if not data: 
			return

		self.value = Strings.capitalize(data)

	def get_value(self):
		return self.value
