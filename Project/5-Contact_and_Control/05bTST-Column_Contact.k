$# LS-DYNA Keyword file created by LS-PrePost(R) V4.8.25 - 04Jan2022
$# Created on Jan-24-2022 (02:10:19)
*KEYWORD
*TITLE
$#                                                                         title
LS-DYNA keyword deck by LS-PrePost
*CONTACT_AUTOMATIC_SURFACE_TO_SURFACE_ID
$#     cid                                                                 title
         3Truck into Column
$#    ssid      msid     sstyp     mstyp    sboxid    mboxid       spr       mpr
         9   5000002         2         2         0         0         0         2
$#      fs        fd        dc        vc       vdc    penchk        bt        dt
      0.25      0.25       0.0       0.0         0         0       0.01.00000E20
$#     sfs       sfm       sst       mst      sfst      sfmt       fsf       vsf
       1.0       1.0       0.0       0.0       1.0       1.0       1.0       1.0
*CONTACT_AUTOMATIC_SURFACE_TO_SURFACE
$$$ Truck body to barrier
$#    ssid      msid     sstyp     mstyp    sboxid    mboxid       spr       mpr
   2000025   5000002         2         2         0         0         0         0
$#      fs        fd        dc        vc       vdc    penchk        bt        dt
0.25000000 0.2500000      0.00 0.0000000      10.0         0 0.0000000 0.0000000
$#     sfs       sfm       sst       mst      sfst      sfmt       fsf       vsf
       0.0       0.0       0.0       0.0       0.0       0.0       0.0       0.0
$#    soft    sofscl    lcidab    maxpar     sbopt     depth     bsort    frcfrq
         2       0.0         0       0.0       0.0         5        10
$#  penmax    thkopt    shlthk     snlog      isym     i2d3d    sldthk    sldstf
       0.0         0         0         0         0         0       0.0       0.0
*END
