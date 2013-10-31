
import ConfigParser

class ConfigDAO(object):

  def __init__(self):
    self.config = ConfigParser.ConfigParser()
    self.config.read("dbsync.conf")

  def getSyncSections(self):
    result = []
    for section in self.config.sections():
      if self.config.get(section, "type") == "sync":
        result.append(section)
    return result
