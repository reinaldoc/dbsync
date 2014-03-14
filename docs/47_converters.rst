
**********
Converters
**********

The converters are responsible for convert acquired data before persist. The
convert rules are processed by parameters in **converters** property on a
synchronization section.

ResizeImageKeepingHeightRatio
=============================

This converter resize images keeping height ratio and support image format
conversion. Use case: ::

    [Sync Picture]
    type = sync
    acquire = Example DB
    acquire query = SELECT E_MAIL, PICTURE from vw_foto where E_MAIL like 'rei%'
    converters = (1, "ResizeImageKeepingHeightRatio", 200, "JPEG")
    #...


* **The first parameter (mandatory)**: the field to be passed to converter. 0 for E_MAIL, 1 for PICTURE.

* **The second parameter (mandatory)**: the converter class name.

* **The third parameter (mandatory)**: the width to image to be resized.

* **The fourth parameter (optional)**: the image format to be converted. If ommited the original format will be used.

NameUpperCase
=============

This converter format a string to all letters capitalized, except it's
prepositions. Use case: ::

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

This converter looks up for a substring and replaces it by another. Use case: ::

    [Sync Personal Info]
    type = sync
    acquire = Example DB
    acquire query = SELECT NAME, SURNAME, BIRTH_DATE from PEOPLE'
    converters = (2, "StringReplace", "-", "/")
    #...
    
* **The first parameter (mandatory)**: the field to be passed to converter. 0 for NAME, 1 for SURNAME or 2 for BIRTH_DATE.

* **The second parameter (mandatory)**: the converter class name.

* **The third parameter (mandatory)**: the substring to be replaced.

* **The fourth parameter (mandatory)**: the string to substitute.

In this example, all birth date information found in the form xx-xx-xxxx,
after the application of the converter, will become in the xx/xx/xxxx form.
