
import sys, os
os.environ["NLS_LANG"] = "AMERICAN_AMERICA.WE8MSWIN1252"

import cx_Oracle

class OracleDAO(object):

	def __init__(self, uri, username, password):
		self.execute_results_blob_as_bytes = False
		try:
			self.conn = cx_Oracle.connect("%s/%s@%s" % (username, password, uri))
			self.cursor = self.conn.cursor()
		except cx_Oracle.DatabaseError, e:
			print(e[0].message.strip())
			print("Unable to connect to '%s'. Aborting..." % uri)
			sys.exit()

	def __del__(self):
		try:
			self.cursor.close()
			self.conn.close()
		except:
			pass

	def execute(self, query):
		try:
			self.cursor.execute(query)
			return self.convert(self.cursor.fetchall())
		except cx_Oracle.DatabaseError, e:
			print(e[0].message.strip())
			print("Malformed query '%s'" % query)
			sys.exit()

	def convert(self, ilist):

		if not self.execute_results_blob_as_bytes:
			return ilist

		# find blob cols from first row
		blob_cols = []
		if len(ilist) > 0:
			first_row = ilist[0]
			for i in range(0,len(first_row)):
				if isinstance(first_row[i], cx_Oracle.LOB):
					blob_cols.append(i)
					
		# replace cx_Oracle.LOB object for bytes
		if blob_cols:
			for i in range(0, len(ilist)):
				row = list(ilist[i])
				for blob_col in blob_cols:
					if row[blob_col]:
						row[blob_col] = row[blob_col].read()
				ilist[i] = row

		return ilist
