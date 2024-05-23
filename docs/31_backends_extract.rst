
****************
Extract Backends
****************

Extract backends are responsible for acquire data from a file, a database or
whatever you like.

Oracle
======

Prerequisites
^^^^^^^^^^^^^

The following software packages are required to be installed:

- Oracle instant client
- cx_Oracle

See cx_Oracle howto: http://reinaldoc.wordpress.com/2013/12/14/python-oracle/


Configuration example
^^^^^^^^^^^^^^^^^^^^^

Oracle connection: ::

    [Oracle1 DB]
    type = Oracle
    uri = 10.13.1.1:1521/adm
    username = xxxxx
    password = xxxxx
    encoding = iso-8859-1

Sync Properties
^^^^^^^^^^^^^^^

When used as source connection the synchronization section must have
this attribute:

* **from query**: specify a SQL to be executed on a Oracle database.

::

    [Sync RH]
    type = sync
    from = Oracle1 DB
    from query = SELECT NAME, MAIL, PHONE, UNIT vw_mat_servidores where NOM like 'REI%'
    to = Prompt


LDAP
====


Prerequisites
^^^^^^^^^^^^^

The following software packages are required to be installed:

- python-ldap


Configuration example
^^^^^^^^^^^^^^^^^^^^^

Ldap connection: ::

    [LDAP1 DB]
    type = Ldap
    uri = ldap://10.13.1.1:389
    basedn = OU=Unit,DC=Domain
    username = account@domain
    password = password
    binary attrs = ["jpegPhoto", "thumbnailPhoto"]
    encoding = utf-8


Sync Properties
^^^^^^^^^^^^^^^

When used as source connection the synchronization section must have
this attribute:

* **from query**: specify a LDAP filter to select registers from LDAP database.
* **from attrs**: specify a list of attributes names to retrieve from registers.

::

    [Sync LDAP to Prompt]
    type = sync
    from = LDAP1 DB
    from query = (objectClass=user)
    from attrs = ["cn", "mail", "whenCreated"]
    to = Prompt
