
********
Backends
********

The backends are responsible for acquire and persist data on a file,
on a database, whatever you like.

Acquire backends
================

Oracle
------

Oracle backend

Oracle - Prerequisites
^^^^^^^^^^^^^^^^^^^^^^

The following software packages are required to be installed:

- Oracle instant client
- cx_Oracle

See cx_Oracle howto: http://reinaldoc.wordpress.com/2013/12/14/python-oracle/

Properties
^^^^^^^^^^

When used as source connection the synchronization section must have
this attribute:

* **acquire query**: specify a SQL to be executed on a Oracle database.


Persist backends
================

Ldap
----

LDAP backend

Ldap - Prerequisites
^^^^^^^^^^^^^^^^^^^^

The following software packages are required to be installed:

- python-ldap

Properties
^^^^^^^^^^

When used as destination connection the synchronization section must have
this attributes:

* **persist lookup dn**: specify a ldap filter to find the distinguished name.
* **persist update rules**: specify the attributes and values to be updated.

