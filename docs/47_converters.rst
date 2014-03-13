
**********
Converters
**********

The converters are responsible for convert acquired data before persist. The
convert rules are processed by parameters in **converters** property.

ResizeImageKeepingHeightRatio
=============================

This converter resize images keeping height ratio and support file format 
spacification. Use case: ::

    [Sync Picture]
    type = sync
    acquire = Example DB
    acquire query = SELECT E_MAIL, PICTURE from vw_foto where E_MAIL like 'rei%'
    converters = ( (1, "ResizeImageKeepingHeightRatio", 200, "JPEG") )
    #...


* **The first parameter (mandatory)**: the field to be passed to converter. 0 for E_MAIL, 1 for PICTURE.

* **The second parameter (mandatory)**: the converter class name.

* **The third parameter (mandatory)**: the width to image resize.

* **The fourth parameter (optional)**: the image format to convert. If ommited the original format will be used.

NameUpperCase
=============

This converter receives a string parameter and formats it with all words 
capitalized, except it's prepositions. Use case: ::

    [Sync Personal Info]
    type = sync
    acquire = Example DB
    acquire query = SELECT NAME, SURNAME from PEOPLE where NAME like 'tiago%'
    converters = ( (0, "NameUpperCase"), (1, "NameUpperCase") )
    #...

* **The first parameter (mandatory)**: the field to be passed to converter. 0 for NAME, 1 for SURNAME.

* **The second parameter (mandatory)**: the converter class name.

**Note**: This converter has no optional property.

StringReplace
=============

This converter receives a string, looks up for a substring passed as first 
parameter and replaces it by another passed as second parameter. Use case: ::

    [Sync Personal Info]
    type = sync
    acquire = Example DB
    acquire query = SELECT NAME, SURNAME, BIRTH_DATE from PEOPLE'
    converters = ( (2, "StringReplace", "-", "/") )
    #...
    
* **The first parameter (mandatory)**: the field to be passed to converter. 0 for NAME, 1 for SURNAME or 2 for BIRTH_DATE.

* **The second parameter (mandatory)**: the converter class name.

* **The third parameter (mandatory)**: the substring to be replaced.

* **The fourth parameter (mandatory)**: the string to substitute.

In this example, all birth date information found in the form xx-xx-xxxx, after the
application of the converter, will become in the xx/xx/xxxx form.
