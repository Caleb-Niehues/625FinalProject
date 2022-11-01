$# LS-DYNA Keyword file created by LS-PrePost(R) V4.8.25 - 04Jan2022
$# Created on Jan-30-2022 (22:51:26)
*KEYWORD
*TITLE
$#                                                                         title
LS-DYNA keyword deck by LS-PrePost
*CONTROL_ACCURACY
$#     osu       inn    pidosu      iacc    
         0         2   2100000         0
*CONTROL_CONTACT
$#  slsfac    rwpnal    islchk    shlthk    penopt    thkchg     orien    enmass
       0.0       0.0         0         2         1         0         1         0
$#  usrstr    usrfrc     nsbcs    interm     xpene     ssthk      ecdt   tiedprj
         0         0         0         0       4.0         0         0         0
$#   sfric     dfric       edc       vfc        th     th_sf    pen_sf      
       0.0       0.0       0.0       0.0       0.0       0.0       0.0
$#  ignore    frceng   skiprwg    outseg   spotstp   spotdel   spothin       
         1         0         0         0         0         0       0.0
$#    isym    nserod    rwgaps    rwgdth     rwksf      icov    swradf    ithoff
         0         0         1       0.0       1.0         0       0.0         0
$#  shledg    pstiff    ithcnt    tdcnof     ftall    unused    shltrw    igactc
         0         0         0         0         0                 0.0         0
*CONTROL_ENERGY
$*    hgen      rwen    slnten     rylen
$#    hgen      rwen    slnten     rylen     irgen     
         2         2         2         2         2
*CONTROL_OUTPUT
$*   npopt    neecho    nrefup    iaccop     opifs    ipnint    ikedit    iflush
$#   npopt    neecho    nrefup    iaccop     opifs    ipnint    ikedit    iflush
         1         3         0         0       0.0         0       100      5000
$*   iprtf
$#   iprtf    ierode   tet10s8    msgmax    ipcurv      gmdt   ip1dblt      eocs
         2         0         2        50         0       0.0         0         0
$#   tolev    newleg    frfreq     minfo    solsig    msgflg    cdetol      
         2         0         1         0         0         0      10.0
$# phschng    demden   icrfile   spc2bnd    penout    shlsig   hisnout    engout
         0         0         0         0         0         0         0         0
*CONTROL_PARALLEL
$#    ncpu    numrhs     const      para    
         1         0         2         2
*CONTROL_SHELL
$*  wrpang     esort     irnxx    istupd    theory       bwc     miter      proj
$#  wrpang     esort     irnxx    istupd    theory       bwc     miter      proj
       0.0         1        -2         0         2         2         1         0
$# rotascl    intgrd    lamsht    cstyp6    thshel      
       1.0         0         0         1         0
$# psstupd   sidt4tu     cntco    itsflg    irquad    w-mode   stretch      icrq
         0         0         0         0         2       0.0       0.0         0
*CONTROL_TERMINATION
$*  endtim    endcyc     dtmin    endeng    endmas
$#  endtim    endcyc     dtmin    endeng    endmas     nosol     
      0.75         0       0.0       0.0       0.0         0
*CONTROL_TIMESTEP
$*  dtinit    tssfac      isdo    tslimt     dt2ms      lctm     erode     ms1st
$#  dtinit    tssfac      isdo    tslimt     dt2ms      lctm     erode     ms1st
       0.0      0.67         03.44000E-6-3.4400E-6         0         0         0
$#  dt2msf   dt2mslc     imscl    unused    unused     rmscl    unused      ihdo
       0.0         0         0                           0.0                   0
*DATABASE_MATSUM
$#      dt    binary
  0.001000         3
*DATABASE_NODOUT
$#      dt    binary
      1E-3         3
*END
