"""
MySqlDAO - Provides access to MySQL data

"""

import MySQLdb

class MySqlDAO(object):

	def __init__(self, uri, user, password, schema=""):
		self._dbUri = uri
		self._dbUser = user
		self._dbSchema = schema
		self._dbPassword = password
		self._connect()

	def _connect(self):
		self._dbConnection = MySQLdb.connect(self._dbUri, self._dbUser, self._dbPassword)
		if self._dbSchema:
			self._dbConnection.select_db(self._dbSchema)
		self._dbCursor = self._dbConnection.cursor()
	
	def __del__(self):
		self._dbConnection.close()
	
	def selectSchema(self, schema):
		self._dbConnection.select_db(schema)
		
	def execute(self, query):
		 self._dbCursor.execute(query)
		 return self._dbCursor.fetchall()

