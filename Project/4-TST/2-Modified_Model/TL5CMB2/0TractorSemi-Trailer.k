*KEYWORD
$
*INCLUDE_PATH
C:/Users/salahatf/Desktop
G:/Other computers/My Office Computer
D:/
$ --------------------- Tractor ----------------
$
*DEFINE_TRANSFORMATION
1
TRANSL, -4700.0, 0.0, 0.0
*INCLUDE_TRANSFORM
/LS-DYNA/4-TST/2-Modified_Model/TL5CMB2/01a_Trac_Day_2010-0520.k
0, 0, 0, 0, 0, 0, 0
0,
0, 0,0, 0, 0
1
*INCLUDE_TRANSFORM
/LS-DYNA/4-TST/2-Modified_Model/TL5CMB2/02initial-stress.k
0, 0, 0, 0, 0, 0, 0
0,
0, 0,0, 0, 0
1
*INCLUDE_TRANSFORM
/LS-DYNA/4-TST/2-Modified_Model/TL5CMB2/01c_Airide_60psi.k
0, 0, 0, 0, 0, 0, 0
0,
0, 0,0, 0, 0
1
$
$ ------------------ Semi-Trailer --------------
$
*INCLUDE_TRANSFORM
/LS-DYNA/4-TST/2-Modified_Model/TL5CMB2/02_SemiTrailer48.k
0, 0, 0, 0, 0, 0, 0
0,
0, 0,0, 0, 0
1
*INCLUDE_TRANSFORM
/LS-DYNA/4-TST/2-Modified_Model/TL5CMB2/02b_AirRideTrailer.k
0, 0, 0, 0, 0, 0, 0
0,
0, 0,0, 0, 0
1
*INCLUDE
/LS-DYNA/4-TST/2-Modified_Model/TL5CMB2/02_TrailerMaterials.k
*INCLUDE_TRANSFORM
/LS-DYNA/4-TST/2-Modified_Model/TL5CMB2/03Tractor2Trailer.k
0, 0, 0, 0, 0, 0, 0
0,
0, 0,0, 0, 0
1
$
$ --------------------   Ballast ----------------
$
*DEFINE_TRANSFORMATION
2
TRANSL, -3040., 0., -6.
*INCLUDE_TRANSFORM
/LS-DYNA/4-TST/2-Modified_Model/TL5CMB2/05NJB-Ballast-foam11b.k
1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000
1000000,
0, 0,0, 0, 0
2
*INCLUDE
/LS-DYNA/4-TST/2-Modified_Model/TL5CMB2/05contact11.k
$
*END
