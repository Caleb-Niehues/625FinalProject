*KEYWORD
$
$ --------------------- Tractor ----------------
$
*DEFINE_TRANSFORMATION
1
TRANSL 1216.2,0, 0
*INCLUDE_TRANSFORM
C:\Users\salah\Desktop\home\salahatf\LS-DYNA\4-TST\2-Modified_Model\01a_Trac_Day_10-0621_TTI.k
0, 0, 0, 0, 0, 0, 0
0,
0, 0,0, 0, 0
1
*INCLUDE
C:\Users\salah\Desktop\home\salahatf\LS-DYNA\4-TST\2-Modified_Model\01c_AirideTractor45psi.k
$
$ ------------------ Semi-Trailer --------------
$
*DEFINE_TRANSFORMATION
2
TRANSL 1216.2,0, 0
*INCLUDE_TRANSFORM
C:\Users\salah\Desktop\home\salahatf\LS-DYNA\4-TST\2-Modified_Model\02a_SemiTrailer45_10-0621_TTI7069-13.k
0, 0, 0, 0, 0, 0, 0
0,
0, 0,0, 0, 0
2
*INCLUDE
C:\Users\salah\Desktop\home\salahatf\LS-DYNA\4-TST\2-Modified_Model\02c_AirRideTrailer45psi.k
*INCLUDE
C:\Users\salah\Desktop\home\salahatf\LS-DYNA\4-TST\2-Modified_Model\02b_TrailerMaterials_2010-0217.k
*INCLUDE
$ ---
C:\Users\salah\Desktop\home\salahatf\LS-DYNA\4-TST\2-Modified_Model\03Tractor2Trailer_connection.k
$
*END
