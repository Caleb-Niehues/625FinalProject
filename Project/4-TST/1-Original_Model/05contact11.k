*KEYWORD
$
$ The 'OFFSET' option must be used here, since the contact surfaces of the 
$ bolt-nuts are part of NRB constraints.
$
*CONTACT_TIED_NODES_TO_SURFACE_OFFSET_ID
$#     cid                                                                 title
         4
$#    ssid      msid     sstyp     mstyp    sboxid    mboxid       spr       mpr
   1000095     98989         3         2
$#      fs        fd        dc        vc       vdc    penchk        bt        dt
     0.000     0.000     0.000     0.000     0.000         0     0.000     0.000
$#     sfs       sfm       sst       mst      sfst      sfmt       fsf       vsf
     0.000     0.000     4.000    -4.000     0.000     0.000     0.000     0.000
*SET_PART_LIST_TITLE
Trailer Floor
$#     sid       da1       da2       da3       da4
     98989
$#    pid1      pid2      pid3      pid4      pid5      pid6      pid7      pid8
        36       354
*CONTACT_AUTOMATIC_NODES_TO_SURFACE_ID
$#     cid                                                                 title
         5
$#    ssid      msid     sstyp     mstyp    sboxid    mboxid       spr       mpr
   1000003        12         2         2
$#      fs        fd        dc        vc       vdc    penchk        bt        dt
  0.150000  0.150000     0.000     0.000 10.000000
$#     sfs       sfm       sst       mst      sfst      sfmt       fsf       vsf
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#    soft    sofscl    lcidab    maxpar     sbopt     depth     bsort    frcfrq
         1
$#  penmax    thkopt    shlthk     snlog      isym     i2d3d    sldthk    sldstf
     0.000         0         0         0         0         0     0.000     0.000
$#    igap    ignore    dprfac    dtstif   unused     unused    flangl
         0         0     0.000     0.000         0         0     0.000
*END
