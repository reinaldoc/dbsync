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

import ldap

from ConfigDAO import ConfigDAO

class LdapDAO(object):
  def __init__(self, db_section, sync_section):
    c = ConfigDAO()
    self.__connect(c.config.get(db_section, "uri"))
    self.__bind(c.config.get(db_section, "username"), c.config.get(db_section, "password"))

  def __connect(self, uri):
    ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, 2)
    ldap.set_option(ldap.OPT_REFERRALS, 0)
    self.l = ldap.initialize(uri)
    self.l.protocol_version = ldap.VERSION3
    return self.l

  def __bind(self, dn, password):
    self.l.simple_bind(dn, password)

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
                    dn = result_data[0][1][0].split('/', 3)[3].split("?")[0]
                    attr, value = dn.split(',')[0].split('=')
                    ldap_result[dn] = {'ref': [result_data[0][1][0]], 'objectClass': ['referral', 'extensibleObject'], attr: [value]}
                else:
                    print "ERROR: result type not implemented. %s" % result_type
            return ldap_result
        except ldap.LDAPError, e:
            if e[0]["desc"] == "Size limit exceeded":
                return ldap_result

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
