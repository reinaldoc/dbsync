"""
Images - manipulate images

"""

from PIL import Image
from io import StringIO
from io import BytesIO
from util.Strings import Strings

class Images():

	@staticmethod
	def get_image_from_string(string):
		return Image.open(StringIO(string))

	@staticmethod
	def get_string_from_image(image, output_format):
		result = BytesIO()
		image.save(result, format=output_format)
		return result.getvalue()

	@staticmethod
	def resize_image_keeping_height_ratio(image, width, resizemode=Image.LANCZOS):
		wpercent = (width / float(image.size[0]))
		hsize = int((float(image.size[1]) * float(wpercent)))
		return image.resize((width, hsize), resizemode)

	@staticmethod
	def resize_string_keeping_height_ratio(string, width, output_format=None, resizemode=Image.LANCZOS):
		by = type(bytes())
		if type(string) != by:
			raise Exception('field is not bytes')

		image = Image.open(BytesIO(string))
		if output_format is None:
			output_format = image.format

		image = Images.resize_image_keeping_height_ratio(image, width)
		return Images.get_string_from_image(image, output_format)
