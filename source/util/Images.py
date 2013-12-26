"""
Images - manipulate images

"""

import Image, ImageOps
from cStringIO import StringIO

class Images():

	@staticmethod
	def resize_image_keeping_height_ratio(image, width, resizemode=Image.ANTIALIAS):
		wpercent = (width / float(image.size[0]))
		hsize = int((float(image.size[1]) * float(wpercent)))
		return image.resize((width, hsize), resizemode)

	@staticmethod
	def resize_string_keeping_height_ratio(string, width, resizemode=Image.ANTIALIAS, output_format=None):

		image = Image.open(StringIO(string))
		if output_format is None:
			output_format = image.format

		image = Images.resize_image_keeping_height_ratio(image, width)
		result = StringIO()
		image.save(result, format=output_format)
		return result.getvalue()
