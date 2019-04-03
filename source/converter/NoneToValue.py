"""
NoneToValue - a converter from None field to defined value

"""

class NoneToValue(object):

	def __init__(self, data, args=()):
		"""
		Receive the data to be converted and parameters.
		"""
		if not args:
			print("Error: NoneToValue takes 1 argument: %s" % args)
			return

		self.value = data

		if data is None:
			self.value = args[0]


	def get_value(self):
		return self.value
