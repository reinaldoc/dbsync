import psycopg2 as pg

class PostgreSqlDAO(object):
	
	def __init__(self, uri, user, password, schema):
		self._dbUri = uri
		self._dbUser = user
		self._dbSchema = schema
		self._dbPassword = password
		self._connect()
	
	def _connect(self):
		self._dbConnection = pg.connect("dbname={0} user={1} password={2} host={3}".format(self._dbSchema, self._dbUser, self._dbPassword, self._dbUri))
		self._dbCursor = self._dbConnection.cursor()
	
	def __del__(self):
		self._dbConnection.close()

	def execute(self, query):
		self._dbCursor.execute(query)
		self._dbConnection.commit()
		try:
			return self._dbCursor.fetchall()
		except pg.ProgrammingError, e:
			return []
