"""
ResizeImageKeepingHeightRatio - a converter to resize images based on original ratio

"""

from util.Images import Images

class ResizeImageKeepingHeightRatio(object):

	def __init__(self, data, args=()):
		"""
		Receive the data to be converted and parameters.
		"""
		if not args or type(args[0]) != type(0):
			print("Error: ResizeImageKeepingHeightRatio takes 1 integer argument: %s" % args)
			return

		self.data = data
		self.width = args[0]
		try:
			self.output_format = args[1]
		except IndexError:
			self.output_format = None

	def get_value(self):
		return Images.resize_string_keeping_height_ratio(self.data, self.width, self.output_format)
