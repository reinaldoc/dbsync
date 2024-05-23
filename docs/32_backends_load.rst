
*************
Load Backends
*************

The backends are responsible to persist data on a file, on a database or
whatever you like.

LDAP
====


Ldap - Prerequisites
^^^^^^^^^^^^^^^^^^^^

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

When used as destination connection the synchronization section must have
this attribute:

* **to match template**: specify a ldap filter to find the distinguished name.
* **to update template**: specify the attributes and values to be updated.

::

    [Sync RH]
    type = sync
    from = Oracle1 DB
    from query = SELECT MAIL, PHONE, UNIT_PREFIX, UNIT, OFFICE from vw_mat_servidores where NOM like 'REI%'
    to = LDAP1 DB
    to match template = (&(objectClass=user)(mail=%0))
    to update template = { "telephoneNumber": "%1", "physicalDeliveryOfficeName": "%2 - %3", "department": "%2 - %3", "title": "%4", "description": "%4" }

