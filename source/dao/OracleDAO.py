
import sys, os
os.environ["NLS_LANG"] = "AMERICAN_AMERICA.WE8MSWIN1252"

import cx_Oracle
from ConfigDAO import ConfigDAO

class OracleDAO(object):
  def __init__(self, db_section, sync_section):
    self.sync_section = sync_section
    self.c = ConfigDAO()
    try:
	self.conn = cx_Oracle.connect("%s/%s@%s" % (self.c.config.get(db_section, "username") , self.c.config.get(db_section, "password") , self.c.config.get(db_section, "uri")))
    except cx_Oracle.DatabaseError, e:
	print("Erro: " + str(e))
	sys.exit()
    self.cursor = self.conn.cursor()

  def execute(self):
    self.cursor.execute(self.c.config.get(self.sync_section, "from query"))
    return self.cursor.fetchall()

  def test(self):
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

