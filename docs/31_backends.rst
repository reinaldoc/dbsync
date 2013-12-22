
********
Backends
********

The backends are responsible for acquire and persist data on a file,
on a database, whatever you like.

Ldap
====

LDAP backend

Ldap - Prerequisites
^^^^^^^^^^^^^^^^^^^^

The following software packages are required to be installed:

- python-ldap

Ldap as destination
^^^^^^^^^^^^^^^^^^^

When used as destination connection the synchronization section must have
this attributes:

* **to match template**: specify a ldap filter to find the distinguished name.
* **to update template**: specify the attributes and values to be updated.

Oracle
======

Oracle backend

Oracle - Prerequisites
^^^^^^^^^^^^^^^^^^^^^^

The following software packages are required to be installed:

- Oracle instant client
- cx_Oracle

See cx_Oracle howto: http://reinaldoc.wordpress.com/2013/12/14/python-oracle/

Oracle as source
^^^^^^^^^^^^^^^^

When used as source connection the synchronization section must have
this attribute:

* **from query**: specify a SQL to be executed on a Oracle database.
