"""
ResizeImageKeepingHeightRatio - a converter to resize images based on original ratio

"""

from dao.ImageDAO import ImageDAO

class ResizeImageKeepingHeightRatio(object):

	def __init__(self, data, args=()):
		"""
		Receive the data to be converted and parameters.
		"""
		self.value = None
		if not args or type(args[0]) != type(0):
			print("WARN: invalid parameters for ResizeImageKeepingHeightRatio: %s" % args)
			return

		width = args[0]
		try:
			output_format = args[1]
		except IndexError:
			output_format = None

		if data:
			self.value = ImageDAO.resize_string_keeping_height_ratio(data, args[0], output_format=output_format)

	def get_value(self):
		return self.value
