*KEYWORD
*TITLE
Simulation of TTI Test 7069-13 
*CONTROL_ACCURACY
$#     osu       inn    pidosu
         1         2 
*CONTROL_ENERGY
$#    hgen      rwen    slnten     rylen
         2         2         2         2
*CONTROL_MPP_IO_NOFULL
*CONTROL_OUTPUT
$#   npopt    neecho    nrefup    iaccop     opifs    ipnint    ikedit    iflush
         1         3         0         0  1.000000         1      1000
$#   iprtf
         0
*CONTROL_SOLUTION
$#    soln
         0
*CONTROL_TERMINATION
$#  endtim    endcyc     dtmin    endeng    endmas
  1.500000                 0.9
*CONTROL_TIMESTEP
$#  dtinit    tssfac      isdo    tslimt     dt2ms      lctm     erode     ms1st
     0.000  0.700000         0     0.000  -1.700-6                  11          
$#  dt2msf   dt2mslc
     0.000         0
*CONTROL_SHELL
$#  wrpang     esort     irnxx    istupd    theory       bwc     miter      proj
 45.000000         1
$# rotascl    intgrd    lamsht    cstyp6    tshell    nfail1    nfail4   psnfail
  1.000000         0         0         1
$# psstupd    irquad
         0         0
*DATABASE_ABSTAT
     0.001         3
*DATABASE_ELOUT
$#      dt    binary
  0.000100         3
*DATABASE_GLSTAT
$#      dt    binary
 5.0000E-4
*DATABASE_MATSUM
$#      dt    binary
  0.001000         3
*DATABASE_NODOUT
$#      dt    binary
 3.3333E-5         3
*DATABASE_RWFORC
$#      dt    binary
 1.0000E-4         3
*DATABASE_RCFORC
$#      dt    binary
 1.0000E-4         3
*DATABASE_DEFORC
$#      dt    binary
 1.0000E-4         3
$*DATABASE_SPCFORC
$#      dt    binary
$ 1.0000E-1         3
*DATABASE_JNTFORC
$#      dt    binary
  0.001000         3
*DATABASE_SLEOUT
$#      dt    binary
  0.001000         3
*DATABASE_BINARY_D3PLOT
$#      dt      lcdt      beam     npltc
     0.010
*DATABASE_BINARY_RUNRSF
$#    cycl  not used  not used  not used
    100000
*DATABASE_BINARY_D3DUMP
    100000
*DATABASE_EXTENT_BINARY
$#   neiph     neips    maxint    strflg    sigflg    epsflg    rltflg    engflg
         0         0         3         0         1         1         1         2
$#  cmpflg    ieverp    beamip     dcomp      shge     stssz    n3thdt   ialemat
         0         0
*CONTROL_CONTACT
$#  slsfac    rwpnal    islchk    shlthk    penopt    thkchg     orien    enmass
     0.000     0.000         0         2
$#  usrstr    usrfrc     nsbcs    interm     xpene     ssthk      ecdt   tiedprj
         0         0         0         0     0.000         0         0         0
$#   sfric     dfric       edc       vfc        th     th_sf    pen_sf
     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#  ignore    frceng   skiprwg    outseg   spotstp   spotdel   spothin
         0         0         0         0         0         0     0.000
$#    isym    nserod    rwgaps    rwgdth     rwksf
         0         0         0     0.000  1.000000
*CONTACT_INTERIOR
$#    psid
   2200060
*SET_PART_LIST
$#     sid       da1       da2       da3       da4
   2200060
$#    pid1      pid2      pid3      pid4      pid5      pid6      pid7      pid8
   2200060   
*LOAD_BODY_Z
$#    lcid        sf    lciddr        xc        yc        zc       cid
   2000001 9806.0000
*END
