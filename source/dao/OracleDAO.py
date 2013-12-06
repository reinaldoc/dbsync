
import sys
import cx_Oracle
from ConfigDAO import ConfigDAO

class OracleDAO(object):
  def __init__(self, db_section, sync_section):
    self.sync_section = sync_section
    self.c = ConfigDAO()
    self.conn = cx_Oracle.connect("%s/%s@%s" % (self.c.config.get(db_section, "username") , self.c.config.get(db_section, "password") , self.c.config.get(db_section, "uri")))
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
    self.cursor.close()
    self.conn.close()
