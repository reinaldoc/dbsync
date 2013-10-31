#!/usr/bin/python
# -*- coding: utf-8 -*-
# ldapsync v2013-alpha
# Copyright (c) 2013 - Reinaldo Gil Lima de Carvalho <reinaldoc@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA.


import json

from controller.ConnectionBC import ConnectionBC

from dao.ConfigDAO import ConfigDAO
from dao.LdapDAO import LdapDAO
from dao.OracleDAO import OracleDAO


c = ConfigDAO()

for syncSection in c.getSyncSections():
  origin = c.config.get(syncSection, "from")
  print "## FROM "
  print c.config.items(origin)
  print
  conn1 = ConnectionBC.getConnection(origin, syncSection)
  conn1.test()
    
  to = c.config.get(syncSection, "to")
  print "## TO"
  print c.config.items(to)
  print
  conn2 = ConnectionBC.getConnection(to, syncSection)
  conn2.test()

  print "## RULES"
  rule = json.loads(c.config.get(syncSection, "to rules"))
  print rule.get("telephoneNumber")

