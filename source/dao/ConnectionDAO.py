
from dao.ConfigDAO import ConfigDAO

class ConnectionDAO(object):
  def __init__(self):
    pass

  @staticmethod
  def getConnection(db_section, sync_section):
    c = ConfigDAO()
    type = c.config.get(db_section, "type")
    module = __import__("dao.%sDAO" % type)	# import
    module = getattr(module, "%sDAO" % type)	# get file name
    module = getattr(module, "%sDAO" % type)    # get class name
    return module(db_section, sync_section)
    