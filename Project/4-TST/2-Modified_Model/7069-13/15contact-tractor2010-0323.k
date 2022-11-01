$# LS-DYNA Keyword file created by LS-PrePost(R) V4.7.7 - 17Feb2020
$# Created on Mar-14-2021 (00:12:44)
*KEYWORD
$
*CONTACT_AUTOMATIC_SURFACE_TO_SURFACE
$#     cid                                                                 title
$$$ Truck body to barrier
$#    ssid      msid     sstyp     mstyp    sboxid    mboxid       spr       mpr
   2000025   4000004         2         3         0         0         0         0
$#      fs        fd        dc        vc       vdc    penchk        bt        dt
      0.25      0.25       0.0       0.0      10.0         0       0.0       0.0
$#     sfs       sfm       sst       mst      sfst      sfmt       fsf       vsf
       0.0       0.0       0.0       0.0       0.0       0.0       0.0       0.0
$#    soft    sofscl    lcidab    maxpar     sbopt     depth     bsort    frcfrq
         2       0.0         0       0.0       0.0         5        10         1
$#  penmax    thkopt    shlthk     snlog      isym     i2d3d    sldthk    sldstf
       0.0         0         0         0         0         0       0.0       0.0
*SET_PART_LIST_TITLE
Impact Side
$#     sid       da1       da2       da3       da4    solver      
   2000025       0.0       0.0       0.0       0.0MECH
$#    pid1      pid2      pid3      pid4      pid5      pid6      pid7      pid8
   2000001   2000002   2000003   2000004   2000020   2000037   2000050   2000060
   2000116   2000118   2000122   2000146   2000147   2000151   2000152   2000165
   2000166   2000167   2000168   2000169   2000170   2000171   2000172   2000173
   2000177   2000180   2000182   2000184   2000187   2000190   2000191   2000192    
   2000195   2000198   2000203   2000206   2000207   2000209   2000256   2000265
   2000266   2000274         0         0         0         0         0         0
*CONTACT_AUTOMATIC_SURFACE_TO_SURFACE
$#     cid                                                                 title
$$ Truck Front Tires and Rims to Barrier
$#    ssid      msid     sstyp     mstyp    sboxid    mboxid       spr       mpr
   2200161   4000004         2         3         0         0         0         0
$#      fs        fd        dc        vc       vdc    penchk        bt        dt
      0.65      0.65       0.0       0.0      10.0         0       0.0       0.0
$#     sfs       sfm       sst       mst      sfst      sfmt       fsf       vsf
       0.0       0.0       0.0       0.0       0.0       0.0       0.0       0.0
$#    soft    sofscl    lcidab    maxpar     sbopt     depth     bsort    frcfrq
         2       0.0         0       0.0       0.0         5        10         1
$#  penmax    thkopt    shlthk     snlog      isym     i2d3d    sldthk    sldstf
       0.0         0         0         0         0         0       0.0       0.0
*SET_PART_LIST_TITLE
Impact Side Tires and Rims - Front
$#     sid       da1       da2       da3       da4    solver      
   2200161       0.0       0.0       0.0       0.0MECH
$#    pid1      pid2      pid3      pid4      pid5      pid6      pid7      pid8
   2000234   2000237   2000257   2000258         0         0         0         0
*CONTACT_AUTOMATIC_SURFACE_TO_SURFACE
$#     cid                                                                 title
$$ Truck Rear Tandem Tires Only to Barrier
$#    ssid      msid     sstyp     mstyp    sboxid    mboxid       spr       mpr
   2200163   4000004         2         3         0         0         0         0
$#      fs        fd        dc        vc       vdc    penchk        bt        dt
      0.65      0.65       0.0       0.0      10.0         0       0.0       0.0
$#     sfs       sfm       sst       mst      sfst      sfmt       fsf       vsf
       0.0       0.0       0.0       0.0       0.0       0.0       0.0       0.0
$#    soft    sofscl    lcidab    maxpar     sbopt     depth     bsort    frcfrq
         2       0.0         0       0.0       0.0         5        10         1
$#  penmax    thkopt    shlthk     snlog      isym     i2d3d    sldthk    sldstf
       0.0         0         0         0         0         0       0.0       0.0
*SET_PART_LIST_TITLE
Impact Side Tires
$#     sid       da1       da2       da3       da4    solver      
   2200163       0.0       0.0       0.0       0.0MECH
$#    pid1      pid2      pid3      pid4      pid5      pid6      pid7      pid8
   2000023   2000024   2000032   2000051   2000052   2000057   2000072   2000083
*CONTACT_AUTOMATIC_SURFACE_TO_SURFACE
$#     cid                                                                 title
$$ Truck RIMS to Barrier
$#    ssid      msid     sstyp     mstyp    sboxid    mboxid       spr       mpr
   2200162   4000004         2         3         0         0         0         0
$#      fs        fd        dc        vc       vdc    penchk        bt        dt
       0.2       0.2       0.0       0.0      10.0         0       0.0       0.0
$#     sfs       sfm       sst       mst      sfst      sfmt       fsf       vsf
       0.0       0.0       0.0       0.0       0.0       0.0       0.0       0.0
$#    soft    sofscl    lcidab    maxpar     sbopt     depth     bsort    frcfrq
         2       0.0         0       0.0       0.0         5        10         1
$#  penmax    thkopt    shlthk     snlog      isym     i2d3d    sldthk    sldstf
       0.0         0         0         0         0         0       0.0       0.0
*SET_PART_LIST_TITLE
Rims
$#     sid       da1       da2       da3       da4    solver      
   2200162       0.0       0.0       0.0       0.0MECH
$#    pid1      pid2      pid3      pid4      pid5      pid6      pid7      pid8
   2000021   2000053   2000062   2000084   2000085   2000099   2000100   2000105
*END
