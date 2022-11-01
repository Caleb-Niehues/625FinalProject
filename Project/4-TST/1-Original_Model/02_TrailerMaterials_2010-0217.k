*KEYWORD
$ ---------------------------------------
$  CAP: Modifications made February 4, 2010
$      - Added material cards for trailer components based on tests conducted
$        at Battelle on 01/28/2010. New material data corresponds to:
$          61) Kingpin Box - Previously mid 22
$          62) Bogie Frame Cross-Member - Previously mid 10
$          63) Bogie Main Frame - Previously mid 10
$          64) Axle Tube - Previously mid 14
$          65) Al Upper Rail - Previously mid 5
$          66) Al Lower Rail - Previously mid 5
$          67) Rear Bumper - Previously mid 11
$          68) Lateral I-Beams - Previously mid 6
$          68) Bogie Slider Rails - Previously mid 10
$          69) Suspension Pivot Support - Previously mid 8
$          70) Suspension Pivot Arm - Previously mid 11
$
$  CRM: Used Srdjan's condensed Stress-Strain Curves 02-08-2010
$  CAP/CRM: Modifications made April-10-2009
$      - Changed density of oak floor from ___ to 7.361E-10 Mg/mm3
$      - Changed density of plywood side pannels from __ to 6.815E-10 Mg/mm3
$      - changed tire density from 3.89E-9 to 3.10E-9
*MAT_SPOTWELD
$#     mid        ro         e        pr      sigy        et        dt     tfail
        99 7.8900E-9 2.0000E+4  0.300000 276.00000 200.00000     0.000     0.000
$#   efail       nrr       nrs       nrt       mrr       mss       mtt        nf
  2.000000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$ Materials for trailer
$ version 01/27/2009
$ Comments:
$ Contains materials for steel and aluminum trailers
$
$ SSUNITS: LENGTH=mm MASS=tonne TIME=s FORCE:=1000kg*0.001m/s^2 = N
$
$ Material List
$ ID DESCRIPTION
$ --------------
$  1 Laminated oak
$  2 Steel - elastic
$  3 Aluminum - elastic
$  4 Aluminum - 6061-T6 (JC Model)
$  5 Aluminum - 6061-T6 (MAT24)
$  6 Steel - ASTM A653/A653M structural quality grade 80
$  7 Steel - CS 1040
$  8 Steel - CS 1095
$  9 Steel - mild steel
$ 10 Steel - HSLA Grade 50 SAE950X
$ 11 Steel - HSLA Grade 80 SAE980X
$ 12 Steel - 4140 Cr-Mo austenized 999C, oil quenched, tempered 399C
$ 13 Steel - 4140 Cr-Mo austenized 999C, oil quenched, tempered 199C
$ 14 Steel - A500 Grade B Shaped Structural Tubing
$ 15 Steel - Leaf Spring Steel 5160 HB 407
$ 16 Steel - Leaf Spring Steel 5160 HB 460
$ 17 Steel - Malleable cast iron, ferritic
$ 18 Steel - Malleable cast iron, whiteheart
$ 19 Steel - Malleable cast iron, pearlitic
$ 20 Steel - AISI 8630 strength 862 MPa
$ 21 Steel - AISI 8630 strength 1034 MPa
$ 22 Steel - AISI 8630 strength 1241 MPa
$ 23 Steel - Stainless steel rivet 302HQ
$ 24 Steel - SAE Grade 5 bolt
$ 25 Steel - SAE Grade 8 bolt
$ 26 Aluminum - A319 casting
$ 27 Steel - A148 casting grade 80-50
$ 28 Aluminum - 3004-H39 (MAT24)
$ 29 Aluminum - 3003-H14 (MAT24)
$ 30 Aluminum - 2117-T4
$ 31 Rigid Steel
$ 32 Tire Rubber (Elastic)
$ 33 Wheel Rim (Yield 270 MPa)
$ 34 Low-Grade Plywood       
$ 35 Shock Absorbers
$ 36 Ballast Elastic
$ 37 Styrofoam Elastic
$
$ -- The following are properties from tests conducted at Battelle 01/28/2010
$ 61 Kingpin Box:  strength 480 MPa (old material 22)
$ 62 Bogie Frame Cross Member: strength 226 MPa (old material 10)
$ 63 Bogie Main Frame:  strength 315 MPa (old material 10)
$ 64 Axle Tube: strength 456 MPa (old material 14)
$ 65 Aluminum Upper Rail:  strength 290 MPa (old material 5)
$ 66 Aluminum Lower Rail:  strength 260 MPa (old material 5)
$ 67 Rear Bumper: strength 375 MPa (old material 11)
$
$........+.........+.........+.........+.........+.........+.........+.........+
$
$ SSMAT-01 Laminated oak
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_ELASTIC
$ Laminated oak
$#     MID        RO         E        PR
         1 7.361E-10 0.1240E+5  0.300000
$
$ SSMAT-02 Steel - elastic
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_ELASTIC
$ Steel - elastic
$#     MID        RO         E        PR
         2 7.8500E-9 2.1000E+5  0.330000
$
$ SSMAT-03 Aluminum - elastic
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_ELASTIC
$ Aluminum - elastic
$#     MID        RO         E        PR
         3 2.7000E-9 0.6900E+5  0.330000
$
$ SSMAT-04 Aluminum - 6061-T6 (JC Model)
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_SIMPLIFIED_JOHNSON_COOK
$ Aluminum - 6061-T6 (JC Model)
$#     MID        RO         E        PR        VP
         4 2.7000E-9 0.6900E+5  0.330000         1
$#       A         B         N         C    PSFAIL    SIGMAX    SIGSAT      EPSO
     289.6     203.4      0.35      0.11
$
$ SSMAT-05 Aluminum - 6061-T6 (MAT24)
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Aluminum - 6061-T6 (MAT24)
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
         5 2.7000E-9 0.6900E+5  0.330000 276.00000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000         5         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Aluminum - 6061-T6 (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
         5         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      2.76000000e+02
      1.06082000e-02      3.18182000e+02
      2.05092000e-02      3.30420000e+02
      3.11174000e-02      3.37413000e+02
      4.10184000e-02      3.44406000e+02
      5.09194000e-02      3.49650000e+02
      8.06223000e-02      3.58392000e+02
      1.00424000e-01      3.65385000e+02
      2.00141000e-01      3.81119000e+02
      3.00566000e-01      3.89860000e+02
      5.00000000e-01      4.03846000e+02
$
$ SSMAT-06 Steel - ASTM A653/A653M structural quality grade 80
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - ASTM A653/A653M structural quality grade 80
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
         6 7.8900E-9 2.1000E+5  0.330000 550.00000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000         6         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - ASTM A653/A653M structural quality grade 80 (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
         6         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      5.50000000e+02
      1.57000000e-02      6.14986391e+02
      4.49000000e-02      6.76238110e+02
      8.25000000e-02      7.28585258e+02
      1.29700000e-01      7.77552681e+02
      1.66400000e-01      8.09405427e+02
      1.99800000e-01      8.35594433e+02
      2.34000000e-01      8.56520946e+02
      2.49800000e-01      8.61521086e+02
$
$ SSMAT-07 Steel - CS 1040
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - CS 1040
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
         7 7.8900E-9 2.1000E+5  0.330000 368.00000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000         7         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - CS 1040 (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
         7         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      3.68000000e+02
      3.23926000e-03      3.73959000e+02
      8.53989000e-03      4.20939000e+02
      1.82576900e-02      4.96106000e+02
      3.81349900e-02      5.91945000e+02
      5.81594900e-02      6.59596000e+02
      7.83312900e-02      6.95300000e+02
      9.83558900e-02      7.19730000e+02
      1.18085890e-01      7.40401000e+02
$
$ SSMAT-08 Steel - CS 1095
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - CS 1095
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
         8 7.8900E-9 2.1000E+5  0.330000 776.00000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000         8         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - CS 1095 (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
         8         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      7.76000000e+02
      3.00885000e-03      8.15953000e+02
      6.72569000e-03      9.14585000e+02
      1.34512900e-02      1.04908000e+03
      2.47787900e-02      1.20151000e+03
      3.18583900e-02      1.27100000e+03
      3.89380900e-02      1.31808000e+03
      4.77875900e-02      1.35843000e+03
      5.55751900e-02      1.38309000e+03
      5.92919900e-02      1.38981000e+03
$
$
$ SSMAT-08 Steel - CS 1095
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - CS 1095
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        81 7.8900E-9 2.1000E+5  0.330000     161.0     0.000     0.132
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000         8         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - CS 1095 (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        81         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00               161.0
              0.0007               221.0
             0.00135               260.3
             0.00179               275.3
             0.00229               283.8
             0.00369               289.0
               0.045               290.0
               0.132               345.0
               0.133               414.0
               0.200               550.0
$
$ SSMAT-09 Steel - mild steel
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - mild steel
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
         9 7.8900E-9 2.1000E+5  0.330000 175.00000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000         9         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - mild steel (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
         9         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      1.75000000e+02
      5.09895054e-03      1.80208135e+02
      1.30594221e-02      1.82945847e+02
      2.52386408e-02      2.03575446e+02
      4.91610068e-02      2.32717756e+02
      7.92934510e-02      2.60632264e+02
      1.22855235e-01      2.92508984e+02
      1.60874779e-01      3.17382473e+02
      1.95701386e-01      3.37975154e+02
      2.43767129e-01      3.57885168e+02
      2.57972940e-01      3.63005500e+02
$
$ SSMAT-10 Steel - HSLA Grade 50 SAE950X
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - HSLA Grade 50 SAE950X
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        10 7.8900E-9 2.1000E+5  0.330000 340.00000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        10         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - HSLA Grade 50 SAE950X (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        10         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      3.40000000e+02
      7.23247881e-03      3.45632583e+02
      1.58428262e-02      3.61727449e+02
      3.49494372e-02      3.96759117e+02
      6.46444144e-02      4.33488597e+02
      9.28219454e-02      4.60031689e+02
      1.23439680e-01      4.83091329e+02
      1.44390313e-01      4.96300627e+02
      1.69823301e-01      5.07555785e+02
$
$ SSMAT-11 Steel - HSLA Grade 80 SAE980X
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - HSLA Grade 80 SAE980X
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        11 7.8900E-9 2.1000E+5  0.330000 557.00000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        11         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - HSLA Grade 80 SAE980X (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        11         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      5.57000000e+02
      1.15053837e-02      5.64468416e+02
      2.57034973e-02      5.92466353e+02
      4.66296083e-02      6.29411040e+02
      7.05025570e-02      6.65457095e+02
      8.91992070e-02      6.89340183e+02
      1.02342743e-01      7.04196262e+02
      1.18532456e-01      7.17147735e+02
      1.31299331e-01      7.24885481e+02
$
$ SSMAT-12 Steel - 4140 Cr-Mo austenized 999C, oil quenched, tempered 399C
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - 4140 Cr-Mo austenized 999C, oil quenched, tempered 399C
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        12 7.8900E-9 2.1000E+5  0.330000 1115.0000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        12         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - 4140 Cr-Mo austenized 999C, oil quenched, tempered 399C (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        12         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      1.11500000e+03
      3.38020000e-04      1.17405000e+03
      8.45070000e-04      1.22205000e+03
      2.11267000e-03      1.27373000e+03
      3.71831000e-03      1.31804000e+03
      5.07038000e-03      1.34757000e+03
      8.61968000e-03      1.39926000e+03
      1.22534800e-02      1.43249000e+03
      1.50422800e-02      1.44726000e+03
      1.91830800e-02      1.46203000e+03
$
$ SSMAT-13 Steel - 4140 Cr-Mo austenized 999C, oil quenched, tempered 199C
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - 4140 Cr-Mo austenized 999C, oil quenched, tempered 199C
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        13 7.8900E-9 2.1000E+5  0.330000 1242.0000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        13         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - 4140 Cr-Mo austenized 999C, oil quenched, tempered 199C (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        13         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      1.24200000e+03
      1.01695000e-03      1.33516000e+03
      2.54237000e-03      1.43684000e+03
      4.40678000e-03      1.52084000e+03
      9.66098000e-03      1.68000000e+03
      1.44914800e-02      1.77284000e+03
      1.99999800e-02      1.84358000e+03
      2.50847800e-02      1.89221000e+03
$
$ SSMAT-14 Steel - A500 Grade B Shaped Structural Tubing
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - A500 Grade B Shaped Structural Tubing
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        14 7.8900E-9 2.1000E+5  0.330000  317.0000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        14         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - A500 Grade B Shaped Structural Tubing (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        14         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      3.17000000e+02
      2.07014169e-01      4.92000000e+02
$
$ SSMAT-15 Steel - Leaf Spring Steel 5160 HB 407
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - Leaf Spring Steel 5160 HB 407
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        15 7.8900E-9 2.1000E+5  0.330000  1200.000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        15         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - Leaf Spring Steel 5160 HB 407 (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        15         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      1.20000000e+03
      1.59411610e-03      1.30817761e+03
      3.67490473e-03      1.37878404e+03
      6.48324279e-03      1.42094536e+03
      9.52680971e-03      1.45088041e+03
      1.28034789e-02      1.47705041e+03
      1.39539031e-02      1.48303514e+03
$
$ SSMAT-16 Steel - Leaf Spring Steel 5160 HB 460
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - Leaf Spring Steel 5160 HB 460
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        16 7.8900E-9 2.1000E+5  0.330000  1247.000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        16         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - Leaf Spring Steel 5160 HB 460 (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        16         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      1.24700000e+03
      9.81049193e-04      1.40503471e+03
      2.20601621e-03      1.51268519e+03
      3.49062015e-03      1.58251534e+03
      6.35968798e-03      1.64662652e+03
      9.58519795e-03      1.69036863e+03
      1.20733250e-02      1.71596731e+03
      1.35874118e-02      1.73142960e+03
$
$ SSMAT-17 Steel - Malleable cast iron, ferritic
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - Malleable cast iron, ferritic
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        17 7.1000E-9 1.7200E+5  0.330000   135.000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        17         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - Malleable cast iron, ferritic (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        17         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      1.35000000e+02
      2.60416425e-04      1.54750806e+02
      7.04491527e-04      1.77046210e+02
      1.24018932e-03      1.91711284e+02
      2.24957133e-03      2.06488809e+02
      3.01358087e-03      2.10488122e+02
      4.25004071e-03      2.14593784e+02
      6.23129322e-03      2.19643615e+02
      7.22044444e-03      2.21404260e+02
$
$ SSMAT-18 Steel - Malleable cast iron, whiteheart
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - Malleable cast iron, whiteheart
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        18 7.1000E-9 1.7200E+5  0.330000   150.000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        18         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - Malleable cast iron, whiteheart (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        18         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      1.50000000e+02
      3.06337012e-04      1.83121134e+02
      6.12573220e-04      2.05403888e+02
      9.49330758e-04      2.20040378e+02
      1.34717169e-03      2.32399972e+02
      1.97421023e-03      2.44057301e+02
      2.83001542e-03      2.51947534e+02
      3.79192661e-03      2.55266274e+02
      4.72241456e-03      2.58582037e+02
      5.69773796e-03      2.60374424e+02
      7.37185510e-03      2.62354339e+02
$
$ SSMAT-19 Steel - Malleable cast iron, pearlitic
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - Malleable cast iron, pearlitic
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        19 7.1000E-9 1.7200E+5  0.330000   300.000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        19         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - Malleable cast iron, pearlitic (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        19         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      3.00000000e+02
      4.28334613e-04      3.51375227e+02
      8.41200012e-04      3.74545506e+02
      1.46781689e-03      3.95516829e+02
      2.01769449e-03      4.08029126e+02
      3.02502210e-03      4.17669955e+02
      4.03132608e-03      4.25020396e+02
      5.00617409e-03      4.30059386e+02
      6.08653998e-03      4.34381466e+02
$
$ SSMAT-20 Steel - AISI 8630 strength 862 MPa
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - AISI 8630 strength 862 MPa
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        20 7.8900E-9 2.1000E+5  0.330000   854.000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        20         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - AISI 8630 strength 862 MPa (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        20         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      8.54000000e+02
      2.84960492e-03      8.64036025e+02
      6.05372395e-03      8.76946199e+02
$
$ SSMAT-21 Steel - AISI 8630 strength 1034 MPa
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - AISI 8630 strength 1034 MPa
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        21 7.8900E-9 2.1000E+5  0.330000  1046.000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        21         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - AISI 8630 strength 1034 MPa (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        21         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      1.04600000e+03
      2.09851624e-03      1.05119538e+03
      5.04615331e-03      1.05683391e+03
$
$ SSMAT-22 Steel - AISI 8630 strength 1241 MPa
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - AISI 8630 strength 1241 MPa
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        22 7.8900E-9 2.1000E+5  0.330000  1267.000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        22         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - AISI 8630 strength 1241 MPa (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        22         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      1.26700000e+03
      1.86119857e-03      1.28220719e+03
      3.99621477e-03      1.30269593e+03
$
$ SSMAT-23 Steel - Stainless steel rivet 302HQ
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - Stainless steel rivet 302HQ
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        23 7.8900E-9 2.1000E+5  0.330000   252.000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        23         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - Stainless steel rivet 302HQ (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        23         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      2.52000000e+02
      2.58064000e-03      2.90312000e+02
      9.03223000e-03      3.11330000e+02
      4.00000300e-02      3.49425000e+02
      1.49677030e-01      4.59770000e+02
      2.58064030e-01      5.71429000e+02
      4.21935030e-01      7.11987000e+02
      4.94194030e-01      7.68473000e+02
$
$ SSMAT-24 Steel - SAE Grade 5 bolt
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - SAE Grade 5 bolt
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        24 7.8900E-9 2.1000E+5  0.300000 634.00000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        24         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - SAE Grade 5 bolt (MAT24 LC)
$#    lcid      sidr       sfa       sfo      offa      offo    dattyp
        24         0  1.000000  1.000000
      0.00000000e+00      6.34000000e+02
      1.00000000e-02      8.35000000e+02
$
$ SSMAT-25 Steel - SAE Grade 8 bolt
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - SAE Grade 8 bolt
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        25 7.8900E-9 2.1000E+5  0.300000 896.00000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        25         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - SAE Grade 8 bolt (MAT24 LC)
$#    lcid      sidr       sfa       sfo      offa      offo    dattyp
        25         0  1.000000  1.000000
      0.00000000e+00      8.96000000e+02
      1.00000000e-02      1.04400000e+03
$
$ SSMAT-26 Aluminum - A319 casting
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Aluminum - A319 casting
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        26 2.7000E-9 0.6900E+5  0.330000 120.00000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        26         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Aluminum - A319 casting (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        26         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      1.20000000e+02
      1.35978000e-03      1.49598000e+02
      5.77904000e-03      1.85791000e+02
      1.22379300e-02      2.11528000e+02
      2.37960300e-02      2.40483000e+02
      3.75637300e-02      2.63003000e+02
      5.09915300e-02      2.78284000e+02
      5.86402300e-02      2.85523000e+02
$
$ SSMAT-27 Steel - A148 casting grade 80-50
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - A148 casting grade 80-50
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        27 7.1000E-9 1.7200E+5  0.300000 345.00000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        27         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - A148 casting grade 80-50 (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        27         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      3.45000000e+02
      1.98850859e-01      6.71000000e+02
$
$ SSMAT-28 Aluminum - 3004-H39 (MAT24)
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Aluminum - 3004-H39 (MAT24)
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        28 2.7000E-9 0.6900E+5  0.330000 238.00000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        28         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Aluminum - 3004-H39 (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        28         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      2.38000000e+02
      6.34920000e-04      2.58144000e+02
      1.74604000e-03      2.71606000e+02
      3.01588000e-03      2.79524000e+02
      8.73017000e-03      2.91402000e+02
      1.34920700e-02      2.98529000e+02
      2.20634700e-02      3.08823000e+02
      2.68253700e-02      3.12782000e+02
      3.82539700e-02      3.23076000e+02
$
$ SSMAT-29 Aluminum - 3003-H14 (MAT24)
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Aluminum - 3003-H14 (MAT24)
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        29 2.7000E-9 0.6900E+5  0.330000 111.00000     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        29         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Aluminum - 3003-H14 (MAT24 LC)
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        29         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00      1.11000000e+02
      3.65430000e-04      1.26371000e+02
      8.35460000e-04      1.35842000e+02
      1.29967000e-03      1.41759000e+02
      1.98986000e-03      1.46881000e+02
      2.90796000e-03      1.52393000e+02
      4.50334000e-03      1.55127000e+02
      1.45165700e-02      1.63225000e+02
$
$ SSMAT-30 Aluminum - 2117-T4
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_POWER_LAW_PLASTICITY
$ Aluminum - 2117-T4
$#     MID        RO         E        PR         K         N       SRC       SRP
        30 2.7000E-9 0.7200E+5  0.330000 551.00000     0.150         0         0
$#    SIGY        VP
  0.000000         1
$
$ SSMAT-31 Rigid Steel       
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_RIGID
$ Rigid Steel
$#     mid        ro         e        pr         n    couple         m     alias
        31 7.8900E-9 2.0500E+5  0.300000     0.000     0.000     0.000
$#     cmo      con1      con2
  1.000000
$#lco or a1       a2        a3        v1        v2        v3
     0.000     0.000     0.000     0.000     0.000     0.000
$
$ SSMAT-32 Tire Rubber
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_ELASTIC
$ Tire Rubber
$#     mid        ro         e        pr        da        db  not used
        32 3.1000E-9 2461.0000  0.450000
$
$ SSMAT-33 Wheel Rim (Yield 270 MPa)
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Wheel Rim
$#     mid        ro         e        pr      sigy      etan      fail      tdel
        33 7.8900E-9 2.0000E+5  0.300000 270.00000     0.000 1.0000E+8
$#       c         p      lcss      lcsr        vp
 90.000000  4.500000        33         0  1.000000
$#    eps1      eps2      eps3      eps4      eps5      eps6      eps7      eps8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     es1       es2       es3       es4       es5       es6       es7       es8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
*DEFINE_CURVE
$#    lcid      sidr       sfa       sfo      offa      offo    dattyp
        33         0  1.000000  1.000000
$#                a1                  o1
               0.000         270.0000000
           0.0487900         320.2999878
           0.0953100         366.2999878
           0.1398000         402.5000000
           0.2231000         438.7999878
           0.2624000         439.7999878
           1.0000000         440.7999878
$
$ SSMAT-34 Low-Grade Plywood
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_ELASTIC
$ Low-Grade Plywood (Currently modeled with laminated oak properties with reduced 
$ density)
$#     MID        RO         E        PR
        34 6.815E-10 0.1240E+5  0.300000
$
$*MAT_ISOTROPIC_ELASTIC_FAILURE
$#     mid        ro         g      sigy      etan      bulk
$        346.1000E-10 4231.0000 40.000000 110.00000 9167.0000
$#     epf       prf       rem      trem
$ 1.000E+20 -90.00000
$
$ SSMAT-35 Shock Absorber
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_DAMPER_NONLINEAR_VISCOUS
$#     mid      lcdr
        35        35
*DEFINE_CURVE
$#    lcid      sidr       sfa       sfo      offa      offo    dattyp
        35         0  1.000000  1.000000
$#                a1                  o1
        -734.0599976       -2797.9179688
        -330.2000122       -2023.9310303
        -152.3999939       -1690.3160400
         -88.9000015       -1183.2209473
         -48.0060005        -667.2299805
               0.000               0.000
          40.6399994         916.3292236
         337.8200073        3327.2539063
         717.5499878        5320.0468750
$
$ SSMAT-36 Ballast Rigid
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_Elastic
$#     mid        ro         e        pr         n    couple         m     alias
        366.4268E-10 300.00000  0.300000 
$
$ SSMAT-37 Styrofoam (Elastic)
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_ELASTIC
$#     mid        ro         e        pr        da        db  not used
        379.8010E-11 100.00000  0.150000
$........+.........+.........+.........+.........+.........+.........+.........+
$
$ SSMAT-61 Steel -  Tested Properties of Kingpin box strength 480 MPa
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - Tested Properties of Kingpin box strength 480 MPa
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        61 7.8900E-9 2.1000E+5  0.330000    480.00     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        61         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - Tested Properties of Kingpin box strength 480 MPa
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        61         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00               480.0
      8.65024912e-03      4.88660036e+02
      1.74388393e-02      4.92934793e+02
      2.84970740e-02      4.98003364e+02
      4.17406332e-02      5.23180035e+02
      6.02728745e-02      5.49949297e+02
      8.38534282e-02      5.76153645e+02
      1.13065115e-01      6.01749771e+02
      1.52381386e-01      6.29173801e+02
      2.04239337e-01      6.57443518e+02
      2.69538993e-01      6.85883789e+02
      3.54854135e-01      7.15503373e+02
      4.64544244e-01      7.45955078e+02
      6.06891305e-01      7.77608840e+02
      7.81262724e-01      8.08732905e+02
      9.34636655e-01      8.31311208e+02
$........+.........+.........+.........+.........+.........+.........+.........+
$
$ SSMAT-62 Steel -  Tested Properties of Bogie Frame Cross-Member strength 226 MPa
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - Tested Properties of Bogie Frame Cross-Member strength 226 MPa
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        62 7.8900E-9 2.1000E+5  0.330000    226.00      0.00 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        62         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - Tested Properties of Bogie Frame Cross-Member strength 226 MPa
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        62         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00               226.0
      1.12793141e-02      2.26825194e+02
      2.83721935e-02      2.71425119e+02
      4.77065200e-02      3.02658811e+02
      7.12369898e-02      3.30793597e+02
      1.03652672e-01      3.59571223e+02
      1.47781796e-01      3.89558326e+02
      2.24600049e-01      4.29448987e+02
      3.39759255e-01      4.70592538e+02
      4.58568590e-01      5.03599369e+02
      6.24580668e-01      5.41025649e+02
      8.68159854e-01      5.83061665e+02
      1.09259029e+00      6.13783560e+02
      1.20983172e+00      6.28291495e+02
$........+.........+.........+.........+.........+.........+.........+.........+
$
$ SSMAT-63 Steel -  Tested Properties of Bogie Main Frame strength 315 MPa
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - Tested Properties of Bogie Main Frame strength 315 MPa
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        63 7.8900E-9 2.1000E+5  0.330000    315.00     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        63         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel - Tested Properties of Bogie Main Frame strength 315 MPa
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        63         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00               315.0
      3.32633017e-03      3.22243943e+02
      9.86064300e-03      3.28918323e+02
      1.60180760e-02      3.51158224e+02
      2.60289317e-02      3.75465883e+02
      3.86139049e-02      3.97349376e+02
      5.49598586e-02      4.18708926e+02
      7.77223244e-02      4.41146468e+02
      1.08980736e-01      4.64417583e+02
      1.50708824e-01      4.88022762e+02
      2.10183134e-01      5.13944065e+02
      2.97005736e-01      5.42120155e+02
      4.09486175e-01      5.69779900e+02
      5.56057685e-01      5.97522255e+02
      7.47528109e-01      6.25762819e+02
      9.94528732e-01      6.54190955e+02
      1.20714849e+00      6.73847769e+02
$........+.........+.........+.........+.........+.........+.........+.........+
$
$ SSMAT-64 Steel -  Tested Properties of Axle Tube strength 456 MPa
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel -  Tested Properties of Axle Tube strength 456 MPa
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        64 7.8900E-9 2.1000E+5  0.330000    456.00     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        64         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel -  Tested Properties of Axle Tube strength 456 MPa
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        64         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00               456.0
      5.59034176e-03      5.46718833e+02
      2.09017350e-02      6.39276596e+02
      3.73738431e-02      6.98867629e+02
      5.75373985e-02      7.51760904e+02
      8.56212745e-02      8.05300338e+02
      1.26224085e-01      8.63464376e+02
      1.89161960e-01      9.28866528e+02
      2.66366109e-01      9.87868323e+02
      3.69623803e-01      1.04996550e+03
      5.35399057e-01      1.12466088e+03
      7.55066946e-01      1.19808469e+03
      9.14854683e-01      1.24017059e+03
$........+.........+.........+.........+.........+.........+.........+.........+
$
$ SSMAT-65 Aluminum -  Tested Properties of Upper Rails strength 290 MPa
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Aluminum -  Tested Properties of Upper Rails strength 290 MPa
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        65  2.700E-9   69000.0  0.330000    290.00     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        65         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Aluminum -  Tested Properties of Upper Rails strength 290 MPa
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        65         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00               290.0
      3.38153217e-03      3.01916710e+02
      9.13234819e-03      3.10611147e+02
      1.38594189e-02      3.15075703e+02
      1.96088580e-02      3.19536915e+02
      2.80645623e-02      3.28210784e+02
      4.02084254e-02      3.37200212e+02
      5.51690847e-02      3.45460585e+02
      7.37716759e-02      3.53405141e+02
      1.21809297e-01      3.68350832e+02
      1.94993899e-01      3.82051255e+02
      2.74147560e-01      3.92501189e+02
      3.60019948e-01      4.01134842e+02
      4.02286356e-01      4.04642606e+02
$........+.........+.........+.........+.........+.........+.........+.........+
$
$ SSMAT-66 Aluminum -  Tested Properties of Lower Rails strength 260 MPa
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$  Aluminum -  Tested Properties of Lower Rails strength 260 MPa
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        66  2.70E-09   69000.0  0.330000    260.00     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        66         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Aluminum -  Tested Properties of Lower Rails strength 260 MPa
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        66         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00               260.0
      3.45318391e-03      2.64533476e+02
      8.17466858e-03      2.68107895e+02
      1.23315420e-02      2.70534738e+02
      1.69435590e-02      2.75810148e+02
      2.36776324e-02      2.81724604e+02
      3.32691423e-02      2.87992336e+02
      4.52593902e-02      2.93919007e+02
      5.99736711e-02      2.99518612e+02
      8.33457587e-02      3.06531792e+02
      1.26064618e-01      3.15381496e+02
      1.77378100e-01      3.22829312e+02
      2.31786228e-01      3.28848996e+02
      2.58528506e-01      3.31293345e+02
$........+.........+.........+.........+.........+.........+.........+.........+
$
$ SSMAT-67 Steel -  Tested Properties of Bumper strength 375 MPa
$........+.........+.........+.........+.........+.........+.........+.........+
*MAT_PIECEWISE_LINEAR_PLASTICITY
$  Steel -  Tested Properties of Bumper strength 375 MPa
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        67 7.8900E-9 2.1000E+5  0.330000    375.00     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000        67         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Steel -  Tested Properties of Bumper strength 375 MPa
$#    LCID      SIDR       SFA       SFO      OFFA      OFFO    DATTYP
        67         0  1.000000  1.000000
$#                A1                  O1
      0.00000000e+00               375.0
      4.28945072e-03      3.80709121e+02
      1.14081867e-02      3.84760153e+02
      2.21217140e-02      3.89142559e+02
      3.13915157e-02      4.07935697e+02
      4.49635227e-02      4.28660284e+02
      6.37512275e-02      4.50007155e+02
      8.75872094e-02      4.70539876e+02
      1.18230944e-01      4.91123120e+02
      1.63311912e-01      5.14605777e+02
      2.24653364e-01      5.38615574e+02
      3.00916193e-01      5.61816217e+02
      3.97959543e-01      5.85009439e+02
      5.21412396e-01      6.08398575e+02
      6.79794596e-01      6.32333048e+02
      8.87594532e-01      6.57406110e+02
      1.05625546e+00      6.73847769e+02
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - ASTM A653/A653M structural quality grade 80
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        68 7.8900E-9 2.1000E+5  0.330000     446.0     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000         6         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Lateral I beam, Bogie Frame rail
$ High Strength Structural Steel, 590 MPa tensile strength, HDGA-HFT 590
$#    lcid      sidr       sfa       sfo      offa      offo    dattyp
        68
$#                a1                  o1
      0.00000000e+00               446.0
      1.49812725e-03      4.60411238e+02
      2.09675028e-03      4.66254595e+02
      2.99401347e-03      4.70851628e+02
      3.89047229e-03      4.74062745e+02
      5.38278677e-03      4.77563717e+02
      7.17062948e-03      4.84014273e+02
      8.36075131e-03      4.88791629e+02
      9.84641456e-03      4.92323837e+02
      1.16263513e-02      4.97416652e+02
      1.36988410e-02      5.05488391e+02
      1.54718906e-02      5.13438730e+02
      1.75365322e-02      5.20153167e+02
      2.01847112e-02      5.30035359e+02
      2.42902878e-02      5.43601152e+02
      2.75043632e-02      5.53916513e+02
      3.01263111e-02      5.61095656e+02
      3.36116463e-02      5.71673555e+02
      3.76625768e-02      5.82646889e+02
      4.05460845e-02      5.88668808e+02
      4.28469190e-02      5.94373176e+02
      4.57155376e-02      6.00442572e+02
      4.82903250e-02      6.06363740e+02
      5.14282053e-02      6.12655280e+02
      5.62584924e-02      6.20029888e+02
      6.05011318e-02      6.27092931e+02
      6.44447980e-02      6.34014175e+02
      6.80929467e-02      6.39305129e+02
      7.22857773e-02      6.44977500e+02
      7.59054842e-02      6.50313435e+02
      7.86809501e-02      6.53623567e+02
      8.22775317e-02      6.57486726e+02
      8.55860534e-02      6.62690778e+02
      8.88836648e-02      6.66397794e+02
      9.35367901e-02      6.71031045e+02
      9.87116609e-02      6.76045650e+02
      1.05480109e-01      6.82180468e+02
      1.11399146e-01      6.86230294e+02
      1.14345133e-01      6.88254900e+02
      1.19148325e-01      6.91568672e+02
      1.23397467e-01      6.94513498e+02
      1.26837035e-01      6.96906437e+02
      1.32894065e-01      6.97967595e+02
      1.37869718e-01      7.01449095e+02
      1.43600652e-01      7.02273607e+02
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - CS 1095
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        69 7.8900E-9 2.1000E+5  0.330000     300.0     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000         8         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Pivot Support
$ High Strength Structural Steel, HF 40Y50T
$#    lcid      sidr       sfa       sfo      offa      offo    dattyp
        69
$#                a1                  o1
      0.00000000e+00               300.0
      6.97561374e-03      3.11899117e+02
      1.43958803e-02      3.27664224e+02
      2.51802985e-02      3.53298082e+02
      3.53671438e-02      3.70643504e+02
      4.40168854e-02      3.82518070e+02
      5.68528116e-02      3.99731940e+02
      6.81258290e-02      4.11355683e+02
      8.25012215e-02      4.22708124e+02
      9.48555310e-02      4.33426198e+02
      1.08405874e-01      4.43031582e+02
      1.23544186e-01      4.53536882e+02
      1.41499562e-01      4.63661568e+02
      1.59138221e-01      4.73855322e+02
      1.81904803e-01      4.84767130e+02
      2.03756838e-01      4.95476866e+02
      2.26338442e-01      5.06792814e+02
      2.39016900e-01      5.13259070e+02
      2.50369538e-01      5.16990698e+02
      2.60439336e-01      5.17925670e+02
      2.65052954e-01      5.18162106e+02
*MAT_PIECEWISE_LINEAR_PLASTICITY
$ Steel - CS 1095
$#     MID        RO         E        PR      SIGY      ETAN      FAIL      TDEL
        70 7.8900E-9 2.1000E+5  0.330000     400.0     0.000 1.0000E+8
$#       C         P      LCSS      LCSR        VP
  0.000000  0.000000         8         0         1
$#    EPS1      EPS2      EPS3      EPS4      EPS5      EPS6      EPS7      EPS8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$#     ES1       ES2       ES3       ES4       ES5       ES6       ES7       ES8
     0.000     0.000     0.000     0.000     0.000     0.000     0.000     0.000
$
*DEFINE_CURVE
$ Suspension Pivot Arm
$ High Strength Structural Steel, HFY 350
$#    lcid      sidr       sfa       sfo      offa      offo    dattyp
        70
$#                a1                  o1
      0.00000000e+00      4.00000000e+02
      2.24534246e-02      4.09082960e+02
      2.54378958e-02      4.19225725e+02
      3.05334727e-02      4.38017064e+02
      3.64456161e-02      4.54785533e+02
      4.14855503e-02      4.67442363e+02
      4.69168869e-02      4.80403478e+02
      5.19044526e-02      4.90656619e+02
      5.68672659e-02      4.99672147e+02
      6.38560070e-02      5.11120900e+02
      7.12029209e-02      5.21559256e+02
      8.17208066e-02      5.35162636e+02
      8.89381945e-02      5.43111651e+02
      9.53101798e-02      5.50683100e+02
      1.04792354e-01      5.58689151e+02
      1.14964846e-01      5.67188052e+02
      1.24263326e-01      5.73892969e+02
      1.29648363e-01      5.78406806e+02
      1.38051785e-01      5.84713742e+02
      1.48269132e-01      5.92159092e+02
      1.53901506e-01      5.95503764e+02
      1.59873132e-01      5.99070529e+02
      1.65810157e-01      6.02637805e+02
      1.70608223e-01      6.05536249e+02
      1.74650543e-01      6.07988974e+02
      1.79770806e-01      6.11110021e+02
      1.87403621e-01      6.15792358e+02
      1.97131348e-01      6.20299212e+02
      2.03564323e-01      6.22780044e+02
      2.09602686e-01      6.23487521e+02
*END
*MAT_WOOD_PINE
     111116.1000E-10
,,,,2



*END
