"""
Images - manipulate images

"""

from PIL import Image
from io import StringIO
from io import BytesIO
from util.Strings import Strings

class Images():

	@staticmethod
	def get_image_from_bytes(data):
		return Image.open(BytesIO(data))

	@staticmethod
	def get_bytes_from_image(image, output_format):
		result = BytesIO()
		image.save(result, format=output_format)
		return result.getvalue()

	@staticmethod
	def resize_image_keeping_height_ratio(image, width, resizemode=Image.LANCZOS):
		wpercent = (width / float(image.size[0]))
		hsize = int((float(image.size[1]) * float(wpercent)))
		return image.resize((width, hsize), resizemode)

	@staticmethod
	def resize_bytes_keeping_height_ratio(data, width, output_format=None, resizemode=Image.LANCZOS):
		if data is None:
			return None

		by = type(bytes())
		if type(data) != by:
			raise Exception('field is not bytes: %s' % type(data))

		image = Images.get_image_from_bytes(data)
		if output_format is None:
			output_format = image.format

		image = Images.resize_image_keeping_height_ratio(image, width)
		return Images.get_bytes_from_image(image, output_format)
