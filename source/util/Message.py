"""
Message - message handling

"""

from dao.ConfigDAO import ConfigDAO

class Info():
	# Construtor da classe Info
	def __init__(self, msg):
		if ConfigDAO().config.get("General", "info") == "True":
			print(msg)

class Debug():
	def __init__(self, msg):
		if ConfigDAO().config.get("General", "debug") == "True":
			print(msg)
