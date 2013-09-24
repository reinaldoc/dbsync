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

from LDAP import LDAP

l = LDAP()
l.connect("ldap://10.13.0.10:3268")
l.bind("rei@redetre.jus.br","12345678")
result = l.search("(mail=rei@tre-pa.gov.br)", "DC=REDETRE,DC=JUS,DC=BR")
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
