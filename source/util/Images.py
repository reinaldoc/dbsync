"""
Images - manipulate images

"""

import Image
from cStringIO import StringIO
from util.Strings import Strings

class Images():

	@staticmethod
	def get_image_from_string(string):
		return Image.open(StringIO(string))

	@staticmethod
	def get_string_from_image(image, output_format):
		result = StringIO()
		image.save(result, format=output_format)
		return result.getvalue()

	@staticmethod
	def resize_image_keeping_height_ratio(image, width, resizemode=Image.ANTIALIAS):
		wpercent = (width / float(image.size[0]))
		hsize = int((float(image.size[1]) * float(wpercent)))
		return image.resize((width, hsize), resizemode)

	@staticmethod
	def resize_string_keeping_height_ratio(string, width, output_format=None, resizemode=Image.ANTIALIAS):
		if not Strings.is_string(string):
			return string

		image = Images.get_image_from_string(string)
		if output_format is None:
			output_format = image.format

		image = Images.resize_image_keeping_height_ratio(image, width)
		return Images.get_string_from_image(image, output_format)
