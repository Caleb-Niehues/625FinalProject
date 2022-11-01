*KEYWORD
$
$ --------------------- Tractor ----------------
$
*INCLUDE
01a_Trac_Day_2010-0520.k
*INCLUDE
02initial-stress.k
*INCLUDE
01c_Airide_60psi.k
$
$ ------------------ Semi-Trailer --------------
$
*INCLUDE
02_SemiTrailer48_10-0521.k
*INCLUDE
02b_AirRideTrailer72p5psi_2.k
*INCLUDE
02_TrailerMaterials_2010-0217.k
*INCLUDE
03Tractor2Trailer_09-0206.k
$
$ --------------------   Ballast ----------------
$
*DEFINE_TRANSFORMATION
1
TRANSL, 1660., 0., -6.
*INCLUDE_TRANSFORM
05NJB-Ballast-foam11b.k
1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000
1000000,
0, 0,0, 0, 0
1
*INCLUDE
05contact11.k
$
$ --------------------- Barrier ----------------
$
*DEFINE_TRANSFORMATION
2
TRANSL, -1490.0, 0.0, 0.0
*INCLUDE_TRANSFORM
15TL-5_Median_Barrier_Elastic.k
0, 0, 0, 0, 0, 0, 0
0,
0, 0,0, 0, 0
2
*INCLUDE
15contact-tractor2010-0323.k
*INCLUDE
15contact-trailer2.k
$
$ ------------------ Control Cards --------------
$
*INCLUDE
20control1.k
*END
