"""
Print - a converter to print receveid data

"""

class Print(object):

	def __init__(self, data, args=()):
		self.value = data
		print(data)

	def get_value(self):
		return self.value
