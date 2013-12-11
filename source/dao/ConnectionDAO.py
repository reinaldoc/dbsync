
from dao.ConfigDAO import ConfigDAO
from util.Clazz import Clazz

class ConnectionDAO(object):
  def __init__(self):
    pass

  @staticmethod
  def get_connection(db_section, sync_section):
    type = ConfigDAO().config.get(db_section, "type")
    conn = Clazz.get_instance("dao", "%sDAO" % type, "%sDAO" % type)
    return conn(db_section, sync_section)
