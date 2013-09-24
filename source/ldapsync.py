#!/usr/bin/python

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
