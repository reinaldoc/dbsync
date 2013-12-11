
import sys, os
os.environ["NLS_LANG"] = "AMERICAN_AMERICA.WE8MSWIN1252"

import cx_Oracle
from ConfigDAO import ConfigDAO

class OracleDAO(object):

	def __init__(self, db_section, sync_section):
		self.db_section = db_section
		self.sync_section = sync_section
		self.c = ConfigDAO()
		try:
			self.conn = cx_Oracle.connect("%s/%s@%s" % (self.c.config.get(db_section, "username") , self.c.config.get(db_section, "password") , self.c.config.get(db_section, "uri")))
		except cx_Oracle.DatabaseError, e:
			print(e[0].message.strip())
			print("Unable to connect to '%s'. Aborting..." % db_section)
			sys.exit()
		self.cursor = self.conn.cursor()

	def execute(self):
		try:
			self.cursor.execute(self.c.config.get(self.sync_section, "from query"))
			return self.convert(self.cursor.fetchall())
		except cx_Oracle.DatabaseError, e:
			print(e[0].message.strip())
			print("Malformed query '%s' in setcion '%s'" % (self.c.config.get(self.sync_section, "from query"), self.sync_section))
			sys.exit()

	def test(self):
		if not self.c.get("General", "stage") == "Test":
			return

		print "\nRunning test to '%s'" % self.db_section
		self.cursor.execute(self.c.config.get(self.sync_section, "from query"))
		result = self.cursor.fetchone()

		if result == None:
			print("Nenhum Resultado")
		else:
			while result:
				print result
				result = self.cursor.fetchone()

	def __del__(self):
		try:
			self.cursor.close()
			self.conn.close()
		except Exception, e:
			pass

	def convert(self, ilist):
		if not self.c.get(self.sync_section, "from field type"):
			return ilist
		for i in range(0, len(ilist)):
			item = list(ilist[i])
			print type(item[2])
			item[2] = item[2].read()
			ilist[i] = item
		return ilist
