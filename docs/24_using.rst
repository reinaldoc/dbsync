
*****
Using
*****

dbsync is extensible to support any kind of data synchronization,
and data conversion. All synchronization rules are defined on **dbsync.conf**

This configuration has two section types. The backend section to declare the
acquire and persist backends to be referred by a synchronization section.

Backend section
===============

A backend section is identified by a backend on 'type' attribute.
The example below has 'Oracle1 DB' as backend section name and use 'Oracle'
as backend. ::

    [Oracle1 DB]
    type = Oracle
    uri = 10.13.1.1:1521/adm
    username = xxxxx
    password = xxxxx
    encoding = iso-8859-1   

Each backend is a class on 'backend/acquire' or 'backend/persist' packages
like Oracle or Ldap. Each acquire backend class must implement method
**load()** and each persist backend class must implement the methods
**sync(data)** and **flush()**.

A backend can be created to acquire or persit any kind of data. Whether to
acquire data from an spread sheet file, from snmp agent or a relational
database or persist data on csv file, a hierarchical database, etc.

Backend section name must be reffered by a synchronization section or will
be ignored.

Synchronization section
=======================

A synchronization section is identified by 'type = sync'. ::

    [Sync SGRH]
    type = sync
    from = Oracle1 DB
    from query = SELECT NOM, E_MAIL, TELEFONE, FONE_CELULAR_SERV, RAMAL, SIGLA_UNIDADE, LOTACAO, CARGO from vw_mat_servidores where NOM like 'REI%'
    to = LDAP1 DB
    to match template = (&(objectClass=user)(mail=%1))
    to update template = { "telephoneNumber": "%4", "homePhone": "%2", "mobile":"%3", "physicalDeliveryOfficeName": "%5 - %6", "department": "%5 - %6", "title": "%7", "description": "%7" }


Each synchronization section is processed sequentially, and have three
mandatories attributes:

* **type**: identify a synchronization section when value is exactly **sync**.
* **from**: define the backend section name to be used to acquire data (data source).
* **to**: define the backend section name to be used to persist data (data destination).

Others attributes are specified by the backend implementation, see backend
documentation. Each backend have mandatories and optionals attributes. A same
backend can be used to acquire and persit data. 
