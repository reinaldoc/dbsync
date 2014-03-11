
**********
Converters
**********

The converters are responsible for convert acquired data before persist. The
convert rules are processed by parameters in **convert data** property.

ResizeImageKeepingHeightRatio
=============================

This converter resize images keeping height ratio and support file format 
spacification. Use case: ::

    [Sync Picture]
    type = sync
    from = Example DB
    from query = SELECT E_MAIL, PICTURE from vw_foto where E_MAIL like 'rei%'
    convert data = ( (1, "ResizeImageKeepingHeightRatio", 200, "JPEG") )


* **convert data**: specify the converters.

1.  The first parameter (mandatory) is the field to be passed to converter. 0 
for E_MAIL, 1 for PICTURE.

2.  The second parameter (mandatory) is the converter class name.

3.  The third parameter (mandatory) is the width to picture to be resized.

4.  The fourth parameter (optional) is the image format to convert.
    If ommited the original format will be used.

NameUpperCase
=============

This converter receives a string parameter and formats it with all words 
capitalized, except it's prepositions. Use case: ::

    [Sync Personal Info]
    type = sync
    from = Example DB
    from query = SELECT NAME, SURNAME from PEOPLE where NAME like 'tiago%'
    convert data = ( (0, "NameUpperCase"), (1, "NameUpperCase") )

1.  The first parameter (mandatory) is the field to be passed to converter. 0 
for NAME, 1 for SURNAME.

2.  The second parameter (mandatory) is the converter class name.

**Note**: This converter has no optional property.

StringReplace
=============

This converter receives a string, looks up for a substring passed as first 
parameter and replaces it by another passed as second parameter. Use case: ::

    [Sync Personal Info]
    type = sync
    from = Example DB
    from query = SELECT NAME, SURNAME, BIRTH_DATE from PEOPLE'
    convert data = ( (2, "StringReplace", "-", "/") )
    
1.  The first parameter (mandatory) is the field to be passed to converter. 0 
for NAME, 1 for SURNAME or 2 for BIRTH_DATE.

2.  The second parameter (mandatory) is the converter class name.

3.  The third parameter is the substring to be replaced.

4. The fourth parameter is the string to substitute.

In this example, all birth date information found in the form xx-xx-xxxx, after the
application of the converter, will become in the xx/xx/xxxx form.