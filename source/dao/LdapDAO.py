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

import ldap, ldap.modlist as modlist

from ConfigDAO import ConfigDAO

class LdapDAO(object):
  def __init__(self, db_section, sync_section):
    self.c = ConfigDAO()
    self.db_section = db_section
    self.__connect(self.c.config.get(db_section, "uri"))
    self.__bind(self.c.config.get(db_section, "username"), self.c.config.get(db_section, "password"))

  def __connect(self, uri):
    ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, 2)
    ldap.set_option(ldap.OPT_REFERRALS, 0)
    self.l = ldap.initialize(uri)
    self.l.protocol_version = ldap.VERSION3
    return self.l

  def __bind(self, dn, password):
    self.l.simple_bind(dn, password)

  def getId(self, ldap_filter):
    result = self.getSingleResult(ldap_filter)
    if len(result) == 0:
      print "WARN: no entry found on destination database for this query: %s" % ldap_filter
      return None
    return result.keys()[0]
    
  def getSingleResult(self, ldap_filter, attrs=None):
    result = self.search(ldap_filter, self.c.config.get(self.db_section, "basedn"), attrs)
    if result is None:
        return {}
    if len(result) > 1:
        raise Exception("Destination database returned more than one entry for this query: %s" % ldap_filter)
    return result

  def search(self,ldap_filter="(objectClass=*)",baseDN=None,attrs=None,scope=ldap.SCOPE_SUBTREE):
        
        try:
            ldap_result_id = self.l.search(baseDN, scope, ldap_filter, attrs)
            ldap_result = {}
            while 1:
                result_type, result_data = self.l.result(ldap_result_id, 0)
                if result_type == ldap.RES_SEARCH_RESULT:
                    break
                elif result_type == ldap.RES_SEARCH_ENTRY:
                    ldap_result[result_data[0][0]] = result_data[0][1]
                elif result_type == ldap.RES_SEARCH_REFERENCE:
                    continue
                    #dn = result_data[0][1][0].split('/', 3)[3].split("?")[0]
                    #attr, value = dn.split(',')[0].split('=')
                    #ldap_result[dn] = {'ref': [result_data[0][1][0]], 'objectClass': ['referral', 'extensibleObject'], attr: [value]}
                else:
                    print "ERROR: result type not implemented. %s" % result_type
            return ldap_result
        except ldap.LDAPError, e:
            if e[0]["desc"] == "Size limit exceeded":
                return ldap_result

  def update(self, query, rules):

      x = []
      for i in rules.keys():
        x.append(i.encode('utf-8'))

      entry = self.getSingleResult(query, x)
      # return if don't find a entry on destination database
      if not entry:
        return

      print "# ID: %s" % entry.keys()[0]
      print "# Rules"
      print rules
      
      updateRules = {}
      
      for k,v in rules.items():
          updateRules[k.encode('utf-8')] = [v.encode('utf-8')]
          
      print updateRules    

      print "OLD: " + str(entry.values()[0])
      print "NEW: " + str(updateRules)
      print modlist.modifyModlist(entry.values()[0], updateRules)   
      print self.l.modify(entry.keys()[0], modlist.modifyModlist(entry.values()[0], updateRules))

  def test(self):
    result = self.search("(mail=rei@tre-pa.gov.br)", "DC=REDETRE,DC=JUS,DC=BR")
    for dn in result.keys():
        print "DN:     " + dn
        print "NOME:   " + result.get(dn).get("cn")[0]
        print "CARGO:  " + result.get(dn).get("description")[0]
        print "E-MAIL: " + result.get(dn).get("mail")[0]
        print
        print "## LDAP ATTRIBUTES ###"
        print result.get(dn).keys()
        print
        print "### DATA ###"
        print result.get(dn)
