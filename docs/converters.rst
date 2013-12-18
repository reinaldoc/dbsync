
**********
Converters
**********

The converters are responsible for convert acquired data before persist.

ResizeImageKeepingHeightRatio
=============================

The converter ResizeImageKeepingHeightRatio resize images keeping height ratio.
Use case: ::

    [Sync Picture]
    type = sync
    from = Oracle1 DB
    from query = SELECT E_MAIL, PICTURE from vw_foto where E_MAIL like 'rei%'
    convert data = ( (1, "ResizeImageKeepingHeightRatio", 200, "JPEG") )

1.  The first parameter (mandatory) is the field to be passed to converter. 0 for E_MAIL, 1 for PICTURE.

2.  The second parameter (mandatory) is the width to picture to be resized.

3.  The third parameter (optional) is the image format to convert.
    If ommited the original format will be used.

