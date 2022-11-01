$# LS-DYNA Keyword file created by LS-PrePost(R) V4.7.7 - 17Feb2020
$# Created on Mar-14-2021 (00:12:44)
*KEYWORD
$
*CONTACT_NODES_TO_SURFACE
$#     cid                                                                 title
$$ Trailer to Barrier
$#    ssid      msid     sstyp     mstyp    sboxid    mboxid       spr       mpr
         9   4000004         2         3         0         0         0         0
$#      fs        fd        dc        vc       vdc    penchk        bt        dt
       0.2       0.2       0.0       0.0       1.0         0       0.0       0.0
$#     sfs       sfm       sst       mst      sfst      sfmt       fsf       vsf
       0.0       0.0       0.0       0.0       0.0       0.0       0.0       0.0
$#    soft    sofscl    lcidab    maxpar     sbopt     depth     bsort    frcfrq
         1       0.0         0       0.0       0.0         2         0         1
$#  penmax    thkopt    shlthk     snlog      isym     i2d3d    sldthk    sldstf
       0.0         0         0         0         0         0       0.0       0.0
*CONTACT_NODES_TO_SURFACE
$#     cid                                                                 title
$$ Trailer tires to Barrier
$#    ssid      msid     sstyp     mstyp    sboxid    mboxid       spr       mpr
      2002   4000004         2         3         0         0         0         0
$#      fs        fd        dc        vc       vdc    penchk        bt        dt
      0.65      0.65       0.0       0.0      10.0         0       0.0       0.0
$#     sfs       sfm       sst       mst      sfst      sfmt       fsf       vsf
       0.0       0.0       0.0       0.0       0.0       0.0       0.0       0.0
$#    soft    sofscl    lcidab    maxpar     sbopt     depth     bsort    frcfrq
         1       0.0         0       0.0       0.0         2         0         1
$#  penmax    thkopt    shlthk     snlog      isym     i2d3d    sldthk    sldstf
       0.0         0         0         0         0         0       0.0       0.0
*SET_PART_LIST
$#     sid       da1       da2       da3       da4    solver      
      2002       0.0       0.0       0.0       0.0MECH
$#    pid1      pid2      pid3      pid4      pid5      pid6      pid7      pid8
        58        64         0         0         0         0         0         0
*CONTACT_NODES_TO_SURFACE
$#     cid                                                                 title
$$ Trailer RIMS to Barrier
$#    ssid      msid     sstyp     mstyp    sboxid    mboxid       spr       mpr
      2003   4000004         2         3         0         0         0         0
$#      fs        fd        dc        vc       vdc    penchk        bt        dt
       0.6       0.6       0.0       0.0      10.0         0       0.0       0.0
$#     sfs       sfm       sst       mst      sfst      sfmt       fsf       vsf
       0.0       0.0       0.0       0.0       0.0       0.0       0.0       0.0
$#    soft    sofscl    lcidab    maxpar     sbopt     depth     bsort    frcfrq
         1       0.0         0       0.0       2.0         2         0         1
$#  penmax    thkopt    shlthk     snlog      isym     i2d3d    sldthk    sldstf
       0.0         0         0         0         0         0       0.0       0.0
*SET_PART_LIST_TITLE
Tires
$#     sid       da1       da2       da3       da4    solver      
      2003       0.0       0.0       0.0       0.0MECH
$#    pid1      pid2      pid3      pid4      pid5      pid6      pid7      pid8
        62        68         0         0         0         0         0         0
*END
