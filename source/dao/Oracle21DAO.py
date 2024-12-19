"""
OracleDAO - provide access to Oracla data

"""

import sys, os
os.environ["NLS_LANG"] = "AMERICAN_AMERICA.WE8MSWIN1252"

import oracledb

class OracleDAO(object):

	def __init__(self, uri, username, password):
		self.execute_results_blob_as_bytes = False
		try:
			self.conn = oracledb.connect("%s/%s@%s" % (username, password, uri))
			self.cursor = self.conn.cursor()
		except oracledb.Error as e:
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
			for row in self.cursor:
				yield self.convert_row(row)
		except oracledb.Error as e:
			print("Error message: '%s'" % e)
			print("Executing query: '%s'" % query)
			sys.exit()
		except Exception as e:
			print(e[0])
			sys.exit()

	def convert(self, ilist):

		if not self.execute_results_blob_as_bytes:
			return ilist

		# find blob cols from first row
		blob_cols = []
		if len(ilist) > 0:
			first_row = ilist[0]
			for i in range(0,len(first_row)):
				if isinstance(first_row[i], oracledb.LOB):
					blob_cols.append(i)

		# replace oracledb.LOB object for bytes
		if blob_cols:
			for i in range(0, len(ilist)):
				row = list(ilist[i])
				for blob_col in blob_cols:
					if row[blob_col]:
						x = row[blob_col].read()
						row[blob_col].close()
						row[blob_col] = x
				ilist[i] = row

		return ilist

	def convert_row(self, row):
		row = list(row)
		for i in range(0,len(row)):
			if isinstance(row[i], oracledb.LOB):
				row[i] = row[i].read()
		return row

		