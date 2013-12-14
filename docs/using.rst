
*****
Using
*****

dbsync is a extensible to support any kind of data synchronization,
including data convertation. All synchronization rules is defined
on dbsync.conf 

dbsync.conf - Synchronization definitions
=========================================

All synchronization rules is defined on dbsync.conf

Connection section
------------------

A connection section is identified by a backend on 'type' attribute.

[Oracle1 DB]
type = Oracle
uri = 10.13.1.1:1521/adm
username = xxxxx
password = xxxxx
encoding = iso-8859-1   


Synchronization section
-----------------------

A synchronization section is identified by 'type = sync'.

[Sync SGRH]
type = sync
from = Oracle1 DB
from query = SELECT NOM, E_MAIL, TELEFONE, FONE_CELULAR_SERV, RAMAL, SIGLA_UNIDADE, LOTACAO, CARGO from vw_mat_servidores where NOM like 'REI%'
to = LDAP1 DB
to match template = (&(objectClass=user)(mail=%1))
to update template = { "telephoneNumber": "%4", "homePhone": "%2", "mobile":"%3", "physicalDeliveryOfficeName": "%5 - %6", "department": "%5 - %6", "title": "%7", "description": "%7" }



