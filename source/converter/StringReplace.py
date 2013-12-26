"""
StringReplace - a converter to replace section(s) of a string to strings passed
as parameters

"""

from util.Strings import Strings

class StringReplace(object):

	def __init__(self, data, args=()):
		"""
		Receive the data to be converted and parameters.
		"""
		self.value = data

		if not data:
			return

		try:
			s_from = args[0]
			s_to = args[1]
			self.value = Strings.replace_string(data, s_from, s_to)
		except IndexError:
			print("Error: StringReplace takes exactly 2 arguments (%s given): %s" % (len(args), args) )
		except Exception, e:
			print(e)

	def get_value(self):
		return self.value
