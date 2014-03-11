
**********
Converters
**********

The converters are responsible for convert acquired data before persist. The
convert rules are processed by parameters in **convert data** property.

ResizeImageKeepingHeightRatio
=============================

The converter ResizeImageKeepingHeightRatio resize images keeping height ratio.
Use case: ::

    [Sync Picture]
    type = sync
    from = Example DB
    from query = SELECT E_MAIL, PICTURE from vw_foto where E_MAIL like 'rei%'
    convert data = ( (1, "ResizeImageKeepingHeightRatio", 200, "JPEG") )


* **convert data**: specify the converters.

1.  The first parameter (mandatory) is the field to be passed to converter. 0 for E_MAIL, 1 for PICTURE.

2.  The second parameter (mandatory) is the converter class name.

3.  The third parameter (mandatory) is the width to picture to be resized.

4.  The fourth parameter (optional) is the image format to convert.
    If ommited the original format will be used.

NameUpperCase
=============

The converter ResizeImageKeepingHeightRatio resize images keeping height ratio.
Use case: ::

    [Sync Personal Info]
    type = sync
    from = Example DB
    from query = SELECT NAME, SURNAME from PEOPLE where NAME like 'tiago%'
    convert data = ( (0, "NameUpperCase"), (1, "NameUpperCase") )

1.  The first parameter (mandatory) is the field to be passed to converter. 0 for NAME, 1 for SURNAME.

2.  The second parameter (mandatory) is the converter class name.

**Note**: This converter has no optional property.