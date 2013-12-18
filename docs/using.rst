
*****
Using
*****

dbsync is extensible to support any kind of data synchronization,
and data conversion. All synchronization rules are defined on dbsync.conf 

dbsync.conf - Sync definitions
==============================

All synchronization rules are defined on dbsync.conf

Connection section
------------------

A connection section is identified by a backend on 'type' attribute.
The example below has 'Oracle1 DB' as connection name and use a 'OracleBC'
backend. ::

    [Oracle1 DB]
    type = Oracle
    uri = 10.13.1.1:1521/adm
    username = xxxxx
    password = xxxxx
    encoding = iso-8859-1   

Each backend is a class on 'controller' package prefixed with 'BC' like
OracleBC. Each backend class must implement method **load()** to be used as
source connection and **sync()** and **flush()** to be used as destination
connection.

A backend can be created to read or write any kind of data. Whether to
read data from an spread sheet file or write data on a hierarchical database.

Connection section name must be reffered by a synchronization section or will
be ignored.

Synchronization section
-----------------------

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
* **from**: define the source connection name.
* **to**: define the destination connection name.

Others attributes are specified by the connection backend.


