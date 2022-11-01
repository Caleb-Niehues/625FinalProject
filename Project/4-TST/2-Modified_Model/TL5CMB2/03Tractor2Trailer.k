*KEYWORD
*TITLE
Tractor to Trailer Interface Hardware
*NODE
  1111111, -6509.70, 0.0, 1151.31
  1130001, -6509.70, 0.0, 1151.31
*SET_NODE_LIST
     11111
   1111111   2007215   2007216   2007244   2007245   2014088   2014089   2014117
   2014118   2019356
*CONSTRAINED_NODAL_RIGID_BODY
     11111
*SET_NODE_LIST_TITLE
king pin on trailer
$#     sid       da1       da2       da3       da4
     11112
$#    nid1      nid2      nid3      nid4      nid5      nid6      nid7      nid8
   1130001
*CONSTRAINED_EXTRA_NODES_SET
$#     pid      nsid
       358     11112
*CONSTRAINED_JOINT_SPHERICAL_ID
     11110
   1111111   1130001
$$$$$$$$$$$$$$$$$$$$$$$
*CONTACT_AUTOMATIC_NODES_TO_SURFACE_ID
     11001
$#    ssid      msid     sstyp     mstyp    sboxid    mboxid       spr       mpr
       354   2000086         3         3         0         0         0         0
$#      fs        fd        dc        vc       vdc    penchk        bt        dt
0.15000000 0.1500000      0.00 0.0000000      10.0         0 0.0000000 0.0000000
$#     sfs       sfm       sst       mst      sfst      sfmt       fsf       vsf
       0.0       0.0       0.0       0.0       0.0       0.0       0.0       0.0
$#    soft    sofscl    lcidab    maxpar     sbopt     depth     bsort    frcfrq
         1       0.0         0       0.0       0.0
$#  penmax    thkopt    shlthk     snlog      isym     i2d3d    sldthk    sldstf
       0.0         0         0         0         0         0       0.0       0.0
$$$$$$$$$$$$$$
*CONTACT_AUTOMATIC_SURFACE_TO_SURFACE
$$ Truck wheels to trailer floor
$#    ssid      msid     sstyp     mstyp    sboxid    mboxid       spr       mpr
   2200007     98989         2         2         0         0         0         0
$#      fs        fd        dc        vc       vdc    penchk        bt        dt
0.65000000 0.6500000      0.00 0.0000000      10.0         0 0.0000000 0.0000000
$#     sfs       sfm       sst       mst      sfst      sfmt       fsf       vsf
       0.0       0.0       0.0       0.0       0.0       0.0       0.0       0.0
$#    soft    sofscl    lcidab    maxpar     sbopt     depth     bsort    frcfrq
         2       0.0         0       0.0       0.0         5        10
$#  penmax    thkopt    shlthk     snlog      isym     i2d3d    sldthk    sldstf
       0.0         0         0         0         0         0       0.0       0.0
*SET_PART_LIST_TITLE
Impact Side Tires
$#     sid       da1       da2       da3       da4
   2200007
$#    pid1      pid2      pid3      pid4      pid5      pid6      pid7      pid8
   2000023   2000024   2000032   2000051   2000052   2000057   2000072   2000083
*END

