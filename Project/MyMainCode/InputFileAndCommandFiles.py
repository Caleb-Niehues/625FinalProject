#region ENVIRONMENT SETTING
import math
import numpy as num
import os
from tkinter import *
from tkinter import filedialog
from Parameters import Parameters
#endregion

class Vehicle():
    """This class writes the inputfile vehicle part"""
    def __init__(self,path,vehicleType,writeFile):
        self.writeFile = writeFile
        if vehicleType==0:
            self.path = path + "/3-SUT/2-Modified_Model/01F800Truck.k"
        else:
            self.path = path + "/4-TST/2-Modified_Model/TL5CMB2/0TractorSemi-Trailer.k"

    def write(self):
        line1 = '$----------------------- Vehicle -----------------'
        line2 = '*INCLUDE'
        line3 = self.path
        self.writeFile.write(line1+'\n'+line2+'\n'+line3+'\n')

class Barrier():
    """This class writes the inputfile barrier part"""
    def __init__(self,path,vehicleType,boundary,angle,writeFile):
        self.path = path
        self.writeFile = writeFile
        self.angle = angle

        if vehicleType == 0:
            self.truckWidth = 2350
            self.barrierContact = "04aSUT-Barrier_Contact.k"
        else:
            self.truckWidth = 2150
            self.barrierContact = "04bTST-Barrier_Contact.k"
        if boundary == 0:
            self.boundary = "1-Fixed"
        elif boundary == 1:
            self.boundary = "2-Free"
        else:
            self.boundary = "3-Segmented"

    def write(self):
        line1 = '$----------------------- Barrier -----------------'
        line2 = '*DEFINE_TRANSFORMATION'
        line3 = '3'
        line4 = 'ROTATE, 0.0, 0.0, 1.0, 0.00, 0.00, 0.00,'+str(self.angle)
        if self.angle == 90:
            line5 = 'TRANSL , 0, '+str(self.barrierLength*-1000/2)+',  0'
        else:
            line5 = 'TRANSL '+str(math.ceil((-7620*num.cos(num.pi*self.angle/180))))+','+str(math.ceil((-7620*num.sin(num.pi*self.angle/180)))-0.5*self.truckWidth)+', 0'
        line6 = "*INCLUDE_TRANSFORM"
        line7 = self.path+ '/1-Barriers/'+self.boundary+'/02JersyBarrier45m.k'
        line8 = '0, 0, 0, 0, 0, 0, 0'
        line9 = '0,'
        line10 = '0, 0,0, 0, 0'
        line11= '3'
        line12 ='*INCLUDE'
        line13 = self.path + '/5-Contact_and_Control/'+self.barrierContact
        self.writeFile.write(line1+'\n'+line2+'\n'+line3+'\n'+line4+'\n'+line5+'\n'+line6+'\n'+line7+'\n'+line8+'\n'+line9+'\n'+line10+'\n'+line11+'\n'+line12+'\n'+line13+'\n')

class Pier():
    """This class writes the inputfile pier part"""
    def __init__(self,path,vehicleType, boundary, angle, distance, pierType, writeFile):
        self.path = path
        self.writeFile = writeFile
        self.angle = angle
        self.pierType = pierType

        if vehicleType == 0:
            self.truckWidth = 2350
            self.pierContact1 = "05aSUT-Column_Contact.k"
            self.pierContact2 = "06Barrier-Column_Contact.k"
        else:
            self.truckWidth = 2150
            self.pierContact1 = "05bTST-Column_Contact.k"
            self.pierContact2 = "06Barrier-Column_Contact.k"
        if boundary == 0:
            self.boundary = "1-Fixed"
        elif boundary == 1:
            self.boundary = "2-Free"
        else:
            self.boundary = "2-Segmented"
     
        if self.pierType == 1:
            self.location = (935/2) + 375
        else:
            self.location = (1250/2) + 375
            
        self.distance = distance

        phi=(math.atan(self.location/(self.distance-7620)))*(180/num.pi)
        hypo=(self.distance-7620)/math.cos(num.pi*phi/180)
        diff=abs(phi-self.angle)
        self.Xtrans = hypo*math.cos(num.pi*diff/180)
        down=hypo*math.sin(num.pi*diff/180)
        if phi-self.angle>0:
            self.Ytrans = -0.5*self.truckWidth-down
        else:
            self.Ytrans = -0.5*self.truckWidth+down

    def write(self):
        line1 = '$----------------------- Pier -----------------'
        line2 = '*DEFINE_TRANSFORMATION'
        line3 = '4'
        line4 = 'ROTATE, 0.0, 0.0, 1, 0, 0, 0.00, '+ str(self.angle)
        line5 = 'TRANSL '+str(math.ceil(self.Xtrans)) +','+str(math.ceil(self.Ytrans))+', 0'
        line6 = "*INCLUDE_TRANSFORM"
        if self.pierType == 1:
            line7 = self.path + '/2-Column/03Column.k'
        else:
            line7 = self.path + '/2-Column/03PierSystem.k'
        line8 = '0, 0, 0, 0, 0, 0, 0'
        line9 = '0,'
        line10 = '0, 0,0, 0, 0'
        line11 = '4'
        line12 = '*INCLUDE'
        line13 = self.path + '/5-Contact_and_Control/' +self.pierContact1
        line14 = '*INCLUDE'
        line15 = self.path + '/5-Contact_and_Control/' +self.pierContact2
        self.writeFile.write(line1+'\n'+line2+'\n'+line3+'\n'+line4+'\n'+line5+'\n'+line6+'\n'+line7+'\n'+line8+'\n'+line9+'\n'+line10+'\n'+line11+'\n'+line12+'\n'+line13+'\n'+line14+'\n'+line15+'\n')

class Control():
    """This class writes the inputfile controls part"""
    def __init__(self,path,vehicleType,writeFile):
        self.path = path
        self.writeFile = writeFile
        if vehicleType == 0:
            self.control = self.path + "/5-Contact_and_Control/07Control.k"
        else:
            self.control = self.path + "/5-Contact_and_Control/08Control.k"
    def write(self):
        line1 = '$----------------------- Controls -----------------'
        line2 = '*INCLUDE'
        line3 = self.control
        self.writeFile.write(line1+'\n'+line2+'\n'+line3+'\n')

class Create():
    def __init__(self):
        self.parameters = Parameters()
        self.operatingSystem = int(input("If running on Windows input 1, if not input 0: "))
        self.Nodes = [4000080  , 4000302  , 4000303  , 4000304 ,  4000305  , 4000306 ,  4000307, 4000308,
           4000309  , 4000310  , 4000311  , 4000312  , 4000313 ,  4000314  , 4000315  , 4000316,
           4000317  , 4000318  , 4000319  , 4000320  , 4000321 ,  4000322  , 4000323  , 4000324,
           4000325  , 4000326  , 4000327  , 4000328  , 4000329 ,  4000330  , 4000331  , 4000332,
           4000333  , 4000334  , 4000335  , 4000336  , 4000337  , 4000338  , 4000339  , 4000340,
           4000341  , 4000342  , 4000343  , 4000344  , 4000345  , 4000346  , 4000347  , 4000348,
           4000349  , 4000350  , 4000351  , 4000352  , 4000353  , 4000354  , 4000355  , 4000356,
           4000357  , 4000358  , 4000359  , 4000360  , 4000361  , 4000362  , 4000363  , 4000364,
           4000365  , 4000366  , 4000367  , 4000368  , 4000369  , 4000370  , 4000371  , 4000372,
           4000373  , 4000374  , 4000375  , 4000376  , 4000377  , 4000378  , 4000379  , 4000380,
           4000381  , 4000382  , 4000383  , 4000384  , 4000385  , 4000386  , 4000387  , 4000388,
           4000389  , 4000390  , 4000391  , 4000392  , 4000393  , 4000394  , 4000395  , 4000396,
           4000397  , 4000398  , 4000399  , 4000400  , 4000401  , 4000402  , 4000403  , 4000404,
           4000405  , 4000406  , 4000407  , 4000408  , 4006734  , 4006735  , 4006736  , 4006737,
           4006738  , 4006739  , 4006740  , 4006741  , 4006742  , 4006743  , 4006744  , 4006745,
           4006746  , 4006747  , 4006748  , 4006749  , 4006750  , 4006751  , 4006752  , 4006753,
           4006754  , 4006755  , 4006756  , 4006757  , 4006758  , 4006759  , 4006760  , 4006761,
           4006762  , 4006763  , 4006764  , 4006765  , 4006766  , 4006767  , 4006768  , 4006769,
           4006770  , 4006771  , 4006772  , 4006773  , 4006774  , 4006775  , 4006776  , 4006777,
           4006778  , 4006779  , 4006780  , 4006781  , 4006782  , 4006783  , 4006784  , 4006785,
           4006786  , 4006787  , 4006788  , 4006789  , 4006790  , 4006791  , 4006792  , 4006793,
           4006794  , 4006795  , 4006796  , 4006797  , 4006798  , 4006799  , 4006800  , 4006801,
           4006802  , 4006803  , 4006804  , 4006805  , 4006806  , 4006807  , 4006808  , 4006809,
           4006810  , 4006811  , 4006812  , 4006813  , 4006814  , 4006815  , 4006816  , 4006817,
           4006818  , 4006819  , 4006820  , 4006821  , 4006822  , 4006823  , 4006824  , 4012233,
           4012234  , 4012235  , 4012236  , 4012237  , 4012238  , 4012239  , 4012240  , 4012241,
           4012242  , 4012243  , 4012244  , 4012245  , 4012246  , 4012247  , 4012248  , 4012249,
           4012250  , 4012251  , 4012252  , 4012253  , 4012254  , 4012255  , 4012256  , 4012257,
           4012258  , 4012259  , 4012260  , 4012261  , 4012262  , 4012263  , 4012264  , 4012265,
           4012266  , 4012267  , 4012268  , 4012269  , 4012270  , 4012271  , 4012272  , 4012273,
           4012274  , 4012275  , 4012276  , 4012277  , 4012278  , 4012279  , 4012280  , 4012281,
           4012282  , 4012283  , 4012284  , 4012285  , 4012286  , 4012287  , 4012288  , 4012289,
           4012290  , 4012291  , 4012292  , 4012293  , 4012294  , 4012295  , 4012296  , 4012297,
           4012298  , 4012299  , 4012300  , 4012301  , 4012302  , 4012303  , 4012304  , 4012305,
           4012306  , 4012307  , 4012308  , 4012309  , 4012310  , 4012311  , 4012312  , 4012313,
           4012314  , 4012315  , 4012316  , 4012317  , 4012318  , 4012319  , 4012320  , 4012321,
           4012322  , 4012323  , 4012324]
        self.Parts = [[2000001,2000002,2000003,2000004,2000005,2000006,2000007,2000008,2000009,2000010,
               2000011,2000012,2000013,2000014,2000015,2000016,2000017,2000018,2000019,2000020,
               2000021,2000022,2000023,2000024,2000025,2000026,2000027,2000028,2000029,2000030,
               2000031,2000032,2000033,2000034,2000035,2000036,2000037,2000038,2000039,2000040,
               2000041,2000042,2000043,2000044,2000045,2000046,2000047,2000048,2000049,2000050,
               2000051,2000052,2000053,2000054,2000055,2000056,2000057,2000058,2000059,2000060,
               2000061,2000062,2000063,2000064,2000065,2000066,2000067,2000068,2000069,2000070,
               2000071,2000072,2000073,2000074,2000075,2000076,2000077,2000078,2000079,2000080,
               2000081,2000082,2000083,2000084,2000085,2000086,2000087,2000088,2000089,2000090,
               2000091,2000092,2000093,2000094,2000095,2000096,2000097,2000098,2000099,2000100,
               2000101,2000102,2000103,2000104,2000105,2000106,2000107,2000108,2000109,2000110,
               2000111,2000112,2000113,2000114,2000115,2000116,2000117,2000118,2000119,2000120,
               2000121,2000122,2000123,2000124,2000125,2000126,2000127,2000128,2000129,2000130,
               2000131,2000132,2000133,2000134,2000135,2000136,2000137,2000138,2000144,2000145,
               2000150,2000151,2000152,2000153,2000154,2000155,2000156,2000157,2000158,2000159,
               2000160,2000161,2000162,2100000,4000000,4000001,4000002,4000003],[
            2000001,2000002,2000003,2000004,2000005,2000006,2000007,2000008,2000009,2000010,
            2000011,2000012,2000013,2000014,2000015,2000016,2000017,2000018,2000019,2000020,
            2000021,2000022,2000023,2000024,2000025,2000026,2000027,2000028,2000029,2000030,
            2000031,2000032,2000033,2000034,2000035,2000036,2000037,2000038,2000039,2000040,
            2000041,2000042,2000043,2000044,2000045,2000046,2000047,2000048,2000049,2000050,
            2000051,2000052,2000053,2000054,2000055,2000056,2000057,2000058,2000059,2000060,
            2000061,2000062,2000063,2000064,2000065,2000066,2000067,2000068,2000069,2000070,
            2000071,2000072,2000073,2000074,2000075,2000076,2000077,2000078,2000079,2000080,
            2000081,2000082,2000083,2000084,2000085,2000086,2000087,2000088,2000089,2000090,
            2000091,2000092,2000093,2000094,2000095,2000096,2000097,2000098,2000099,2000100,
            2000101,2000102,2000103,2000104,2000105,2000106,2000107,2000108,2000109,2000110,
            2000111,2000112,2000113,2000114,2000115,2000116,2000117,2000118,2000119,2000120,
            2000121,2000122,2000123,2000124,2000125,2000126,2000127,2000128,2000129,2000130,
            2000131,2000132,2000133,2000134,2000135,2000136,2000137,2000138,2000139,2000140,
            2000141,2000142,2000143,2000144,2000145,2000146,2000147,2000148,2000149,2000150,
            2000151,2000152,2000153,2000154,2000155,2000156,2000157,2000158,2000159,2000160,
            2000161,2000162,2000163,2000164,2000165,2000166,2000167,2000168,2000169,2000170,
            2000171,2000172,2000173,2000174,2000175,2000176,2000177,2000178,2000179,2000180,
            2000181,2000182,2000183,2000184,2000185,2000186,2000187,2000188,2000189,2000190,
            2000191,2000192,2000193,2000194,2000195,2000196,2000197,2000198,2000199,2000200,
            2000201,2000202,2000203,2000204,2000205,2000206,2000207,2000208,2000209,2000210,
            2000211,2000212,2000213,2000214,2000215,2000216,2000217,2000218,2000219,2000220,
            2000221,2000222,2000223,2000224,2000225,2000226,2000227,2000228,2000229,2000230,
            2000231,2000232,2000233,2000234,2000235,2000236,2000237,2000238,2000239,2000240,
            2000241,2000242,2000243,2000244,2000245,2000246,2000247,2000248,2000249,2000250,
            2000251,2000252,2000253,2000254,2000255,2000256,2000257,2000258,2000259,2000260,
            2000261,2000262,2000263,2000264,2000265,2000266,2000267,2000268,2000269,2000270,
            2000271,2000272,2000273,2000274,2000275,2000276,2000277,2000278,2000279,2000280,
            2000282,2000283,2000284,2000285,2000286,2000287,2000288,2000289,2000290,2000291,
            2000293,2000295,2000296,2000297,2000299,2000300,2000301,2000302,2000303,2000304,
            2000305,2000307,2000308,2000309,2000310,2000311,2000312,2000313,2000314,2000315,
            2000316,2000317,2000318,2000320,2000321,2000322,2000323,2000324,2000325,2000326,
            2000327,2000328,2000329,2000330,2000334,2000335,2000336,2000337,2000338,2000339,
            2000340,2000341,2000342,2000343,2000344,2000345,2000346,2000347,2000348,2000349,
            2000350,2000351,2000352,2000353,2000359,2000365,2000366,2000367,2000368,2000369,
            2000370,2000371,2000372,2000373,2000374,2000375,2000376,2000377,2000378,2000379,
            2000380,2000381,2000382,2000383,2000384,2000385,2000386,2000387,2000390,2000391,
            2000392,2000393,2100002,2100004,2100005,2100006,2100007,2100008,2100009,2100010,
            2100011,2100012,2100013,2100014,2100015,2100016,2100017,2100018,2100019,2100020,
            2100021,2100022,2100023,2100024,2100025,2100026,2100027,2100028,2100029,2100030,
            2100031,2100032,2100033,2100034,2100035,2100036,2200004,2200005,2200006,2200007,
            2200008,2200009,2200010,2200011,2200012,2200013,2200014,2200015,2200016,2200017,
            2200018,2200019,2200020,2200021,2200022,2200023,2200024,2200025,2200026,2200027,
            2200028,2200029,2200030,2200031,2200032,2200033,2200034,2200035,2200036,2200037,
            2200050,2200051,2200052,2200060,2200061,2200062,2200063,2200064,2200070,2200071,
            2200099,2200100,2200101,3000000,3000001,3000002,3000089,3000092,3000101,3000102,
            1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
            31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,52,53,54,55,56,57,58,59,60,
            61,62,63,64,65,66,67,68,69,71,72,75,76,78,80,82,91,92,101,350,351,352,353,354,355,
            356,357,358,400,500,501,502,503,504,505,1091,1780,2930,2992,3806,7675,7803,9192,73,
            74,1000001,1000005,1000009,1000013,1000017,1000021,1000025,1000029,1000033,1000034,
            1000039,1000043,1000047,1000091,1000092,1000094,1000095,1000096,1000097,129]]
        self.Accel = [2000144,2000368] 
        self.offset = [0,-0.3]

    def createInputFiles(self,purpose):
        if purpose ==1:
            self.parameters.paper1()
        else:
            self.parameters.paper2()
        root = Tk()
        root.withdraw()
        parentPath = filedialog.askdirectory(parent = root, initialdir="/", title='Select the parent path to locate the input files for Phase1')
        dataPath = filedialog.askdirectory(parent = root, initialdir="/", title='Select the folder that contains the LS-DYNA Models')
        for i in range (len(self.parameters.vehicleType)):
            cwd_i = os.path.join(parentPath+"/"+self.parameters.phaseName[0],self.parameters.vehicleType[i])
            for j in range (len(self.parameters.barrierBoundary)):
                cwd_j = os.path.join(cwd_i,self.parameters.barrierBoundary[j])
                for l in range (len(self.parameters.anglesOfAttack)):
                    cwd_l = os.path.join(cwd_j,str(self.parameters.anglesOfAttack[l]))
                    ext=".k"
                    Name = self.parameters.vehicleType[i]+'_'+self.parameters.barrierBoundary[j]+'_'+str(self.parameters.anglesOfAttack[l])
                    lsdynaInputFilePath = os.path.join(cwd_l,Name+ext)
                    lsdynaInputFile = open(lsdynaInputFilePath,'w')
                    lsdynaInputFile.write('*KEYWORD'+'\n')
                    vehicle = Vehicle(dataPath,i,lsdynaInputFile)
                    vehicle.write()
                    barrier = Barrier(dataPath,i,j,self.parameters.anglesOfAttack[l],lsdynaInputFile)
                    barrier.write()
                    control = Control(dataPath,i,lsdynaInputFile)
                    control.write()
                    lsdynaInputFile. close()
       
    def createPhase2InputFiles(self):
        root = Tk()
        root.withdraw()
        parentPath = filedialog.askdirectory(parent = root, initialdir="/", title='Select the parent path to locate the input files for Phase2')
        dataPath = filedialog.askdirectory(parent = root, initialdir="/", title='Select the folder that contains the LS-DYNA Models')
        for i in range (len(self.parameters.vehicleType)):
            cwd_i = os.path.join(parentPath+"/"+self.parameters.phaseName[1],self.parameters.vehicleType[i])
            for j in range (len(self.parameters.barrierBoundary)):
                cwd_j = os.path.join(cwd_i,self.parameters.barrierBoundary[j])
                for l in range (len(self.parameters.anglesOfAttack)):
                    cwd_l = os.path.join(cwd_j,str(self.parameters.anglesOfAttack[l]))
                    for m in range (len(self.parameters.pierLocation)):
                        cwd_m = os.path.join(cwd_l,str(self.parameters.pierLocation[m]))
                        ext=".k"
                        Name = self.parameters.vehicleType[i]+'_'+self.parameters.barrierBoundary[j]+'_'+str(self.parameters.anglesOfAttack[l])+'_'+str(self.parameters.pierLocation[m])
                        lsdynaInputFilePath = os.path.join(cwd_m,Name+ext)
                        lsdynaInputFile = open(lsdynaInputFilePath,'w')
                        lsdynaInputFile.write('*KEYWORD'+'\n')
                        vehicle = Vehicle(dataPath,i,lsdynaInputFile)
                        vehicle.write()
                        barrier = Barrier(dataPath,i,j,self.parameters.anglesOfAttack[l],lsdynaInputFile)
                        barrier.write()
                        pier = Pier(dataPath,i,j,self.parameters.anglesOfAttack[l],self.parameters.pierLocation[m],1,lsdynaInputFile)
                        pier.write()
                        control = Control(dataPath,i,lsdynaInputFile)
                        control.write()
                        lsdynaInputFile. close()

    def createCaseStudyInputFiles(self):
        root = Tk()
        root.withdraw()
        parentPath = filedialog.askdirectory(parent = root, initialdir="/", title='Select the parent path to locate the input files for CaseStudy')
        dataPath = filedialog.askdirectory(parent = root, initialdir="/", title='Select the folder that contains the LS-DYNA Models')
        for i in range (len(self.parameters.vehicleType)):
            cwd_i = os.path.join(parentPath+"/"+self.parameters.phaseName[2],self.parameters.vehicleType[i])
            for j in range (len(self.parameters.barrierBoundary)):
                cwd_j = os.path.join(cwd_i,self.parameters.barrierBoundary[j])
                for l in range (len(self.parameters.anglesOfAttack)):
                    cwd_l = os.path.join(cwd_j,str(self.parameters.anglesOfAttack[l]))
                    for m in range (1):
                        cwd_m = os.path.join(cwd_l,str(self.parameters.pierLocationCaseStudy[m]))
                        ext=".k"
                        Name = self.parameters.vehicleType[i]+'_'+self.parameters.barrierBoundary[j]+'_'+str(self.parameters.anglesOfAttack[l])+'_'+str(self.parameters.pierLocationCaseStudy[m])
                        lsdynaInputFilePath = os.path.join(cwd_m,Name+ext)
                        lsdynaInputFile = open(lsdynaInputFilePath,'w')
                        lsdynaInputFile.write('*KEYWORD'+'\n')
                        vehicle = Vehicle(dataPath,i,lsdynaInputFile)
                        vehicle.write()
                        barrier = Barrier(dataPath,i,j,self.parameters.anglesOfAttack[l],lsdynaInputFile)
                        barrier.write()
                        pier = Pier(dataPath,i,j,self.parameters.anglesOfAttack[l],self.parameters.pierLocationCaseStudy[m],2,lsdynaInputFile)
                        pier.write()
                        control = Control(dataPath,i,lsdynaInputFile)
                        control.write()
                        lsdynaInputFile. close() 

    def createLsdynaCommandFile(self,purpose):
        if purpose ==1:
            self.parameters.paper1()
        else:
            self.parameters.paper2()
        root = Tk()
        root.withdraw()
        parentPath = filedialog.askdirectory(parent = root, initialdir="/", title='Select the parent path to locate LS-DYNA command files for Phase1')
        for i in range (len(self.parameters.vehicleType)):
            cwd_i = os.path.join(parentPath+"/"+self.parameters.phaseName[0],self.parameters.vehicleType[i])
            masterFilePath = os.path.join(cwd_i,'lsdynaMasterFile.sh')
            lsdynaMasterFile = open (masterFilePath,'w')
            lsdynaMasterFile.write('#!/bin/bash'+'\n')
            for j in range (len(self.parameters.barrierBoundary)):
                cwd_j = os.path.join(cwd_i,self.parameters.barrierBoundary[j])
                for l in range (len(self.parameters.anglesOfAttack)):
                    cwd_l = os.path.join(cwd_j,str(self.parameters.anglesOfAttack[l]))
                    ext=".sh"
                    Name = self.parameters.vehicleType[i]+'_'+self.parameters.barrierBoundary[j]+'_'+str(self.parameters.anglesOfAttack[l])
                    lsdynaCommandFilePath = os.path.join(cwd_l,Name+ext)
                    if self.operatingSystem ==1:
                        cwd_l = cwd_l.replace(parentPath+'/',"\home\salahatf\LS-DYNA\\")
                    lsdynaMasterFile.write('cd '+cwd_l+'\n'+'chmod +x '+Name+ext+'\n'+'./'+Name+ext+ ' &' + '\n')
                    lsdynaCommandFile = open (lsdynaCommandFilePath,'w')
                    line1="#!/bin/bash"
                    line2="/home/ls-dyna/bin/ls-dyna_smp_s_r1010_x64_redhat5_ifort160 " + 'I=\"'+ cwd_l+"/"+Name+'.k\"'+ " NCPU=-4 MEMORY=200000000 jobid="+Name
                    lsdynaCommandFile.write(line1+'\n'+line2)
                    lsdynaCommandFile.close()
            lsdynaMasterFile.close()

    def createLsdynaPhase2CommandFile(self):
        root = Tk()
        root.withdraw()
        parentPath = filedialog.askdirectory(parent = root, initialdir="/", title='Select the parent path to locate LS-DYNA command files for Phase2')
        for i in range (len(self.parameters.vehicleType)):
            cwd_i = os.path.join(parentPath+"/"+self.parameters.phaseName[1],self.parameters.vehicleType[i])
            masterFilePath = os.path.join(cwd_i,'lsdynaMasterFile.sh')
            lsdynaMasterFile = open (masterFilePath,'w')
            lsdynaMasterFile.write('#!/bin/bash'+'\n')
            for j in range (len(self.parameters.barrierBoundary)):
                cwd_j = os.path.join(cwd_i,self.parameters.barrierBoundary[j])         
                for l in range (len(self.parameters.anglesOfAttack)):
                    cwd_l = os.path.join(cwd_j,str(self.parameters.anglesOfAttack[l]))
                    for m in range (len(self.parameters.pierLocation)):
                        cwd_m = os.path.join(cwd_l,str(self.parameters.pierLocation[m]))  
                        ext=".sh"
                        Name = self.parameters.vehicleType[i]+'_'+self.parameters.barrierBoundary[j]+'_'+str(self.parameters.anglesOfAttack[l])+'_'+str(self.parameters.pierLocation[m])
                        lsdynaCommandFilePath = os.path.join(cwd_m,Name+ext)
                        if self.operatingSystem ==1:
                            cwd_m = cwd_m.replace(parentPath +'/' , "\home\salahatf\LS-DYNA\\")
                        lsdynaMasterFile.write('cd '+cwd_m+'\n'+'chmod +x '+Name+ext+'\n'+'./'+Name+ext+ ' &' + '\n')
                        lsdynaCommandFile = open (lsdynaCommandFilePath,'w')
                        line1="#!/bin/bash"
                        line2="/home/ls-dyna/bin/ls-dyna_smp_s_r1010_x64_redhat5_ifort160 " + 'I=\"'+ cwd_m + "/" + Name+'.k\"'+ " NCPU=-4 MEMORY=200000000 jobid="+Name
                        lsdynaCommandFile.write(line1+'\n'+line2)
                        lsdynaCommandFile.close()
            lsdynaMasterFile.close()
   
    def createLsdynaCaseStudyCommandFile(self):
        root = Tk()
        root.withdraw()
        parentPath = filedialog.askdirectory(parent = root, initialdir="/", title='Select the parent path to locate LS-DYNA command files for CaseStudy')
        for i in range (len(self.parameters.vehicleType)):
            cwd_i = os.path.join(parentPath+"/"+self.parameters.phaseName[2],self.parameters.vehicleType[i])
            masterFilePath = os.path.join(cwd_i,'lsdynaMasterFile.sh')
            lsdynaMasterFile = open (masterFilePath,'w')
            lsdynaMasterFile.write('#!/bin/bash'+'\n')
            for j in range (len(self.parameters.barrierBoundary)):
                cwd_j = os.path.join(cwd_i,self.parameters.barrierBoundary[j])
                for l in range (len(self.parameters.anglesOfAttack)):
                    cwd_l = os.path.join(cwd_j,str(self.parameters.anglesOfAttack[l]))
                    for m in range (1):
                        cwd_m = os.path.join(cwd_l,str(self.parameters.pierLocationCaseStudy[m]))  
                        ext=".sh"
                        Name = self.parameters.vehicleType[i]+'_'+self.parameters.barrierBoundary[j]+'_'+str(self.parameters.anglesOfAttack[l])+'_'+str(self.parameters.pierLocationCaseStudy[m])
                        lsdynaCommandFilePath = os.path.join(cwd_m,Name+ext)
                        if self.operatingSystem ==1:
                            cwd_m = cwd_m.replace(parentPath +'/',"\home\salahatf\LS-DYNA\\")
                        lsdynaMasterFile.write('cd '+cwd_m+'\n'+'chmod +x '+Name+ext+'\n'+'./'+Name+ext+ ' &' + '\n')
                        lsdynaCommandFile = open (lsdynaCommandFilePath,'w')
                        line1="#!/bin/bash"
                        line2="/home/ls-dyna/bin/ls-dyna_smp_s_r1010_x64_redhat5_ifort160 " + 'I=\"'+ cwd_m + "/" +Name+'.k\"'+ " NCPU=-4 MEMORY=200000000 jobid="+Name
                        lsdynaCommandFile.write(line1+'\n'+line2)
                        lsdynaCommandFile.close()
            lsdynaMasterFile.close()        

    def createLsPrePostCommandFile(self,purpose):
        if purpose ==1:
            self.parameters.paper1()
        else:
            self.parameters.paper2()
        root = Tk()
        root.withdraw()
        parentPath = filedialog.askdirectory(parent = root, initialdir="/", title='Select the parent path to locate LS-PrePost Phase1 command files for Phase 1')
        for i in range (len(self.parameters.vehicleType)):
            cwd_i = os.path.join(parentPath+"/"+self.parameters.phaseName[0],self.parameters.vehicleType[i])
            masterFilePath = os.path.join(cwd_i,'lsprepostMasterFile.sh')
            lsprepostMasterFile = open (masterFilePath,'w')
            lsprepostMasterFile.write('#!/bin/bash'+'\n')
            for j in range (len(self.parameters.barrierBoundary)):
                cwd_j = os.path.join(cwd_i,self.parameters.barrierBoundary[j])                
                for l in range (len(self.parameters.anglesOfAttack)):
                    cwd_l = os.path.join(cwd_j,str(self.parameters.anglesOfAttack[l]))
                    ext='.cfile'
                    ext1='.rcforc'
                    ext2='.nodout'
                    ext3='.matsum'
                    ext4='.sleout'
                    ext5 = '.glstat'
                    Name = self.parameters.vehicleType[i]+'_'+self.parameters.barrierBoundary[j]+'_'+str(self.parameters.anglesOfAttack[l])
                    lsprepostCommandFilePath = os.path.join(cwd_l,Name+ext)
                    lsprepostMasterFile.write('cd ' + cwd_l + '\n')
                    lsprepostMasterFile.write('/home/ls-dyna/lsprepost4.8_common/lspp48 c='+'/"'+Name+ext+'/"'+' -nographics'+'\n')
                    lsprepostCommandFile = open (lsprepostCommandFilePath,'w')
                    lsprepostCommandFile.write("openc keyword "+cwd_l+"/"+Name+".k")
                    #rcforcContactForces    
                    rcforcFileName=Name+ext1   
                    rcforcFilePath=os.path.join(cwd_l,rcforcFileName)
                    line1='ascii rcforc open '+"\""+rcforcFileName+"\""
                    line2='ascii rcforc plot 2 Ma-4000000'
                    line3='xyplot 1 xoffset '+ str(self.offset[i])+' yoffset 0 xscale 1 yscale 0.001'
                    line4='xyplot 1 filter sae  60.00 sec 0'
                    line5='xyplot 1 savefile ms_csv '+ cwd_l + "/RCFORC.csv\" 1 all"
                    line6='Writing XY data to file: '+ cwd_l + "/RCFORC.csv"
                    lsprepostCommandFile.write(line1+"\n"+line2+"\n"+line3+"\n"+line4+"\n"+line5+"\n"+line6+"\n")
               
                    #nodoutDisplacements
                    nodoutFileName=Name+ext2
                    nodoutFilePath=os.path.join(cwd_l,nodoutFileName)
                    line1='ascii nodout open '+"\""+nodoutFileName+"\""
                    line2='ascii nodout plot 2 all'
                    line3='xyplot 1 savefile ms_csv '+ cwd_l + "/displacement.csv\" 1 all"
                    line4='Writing XY data to file: '+ cwd_l + "/displacement.csv"
                    lsprepostCommandFile.write(line1+"\n"+line2+"\n"+line3+"\n"+line4+"\n") 

                    #matsumX-acceleration
                    matsumFileName=Name+ext3
                    matsumFilePath=os.path.join(cwd_l,matsumFileName)
                    line1='ascii matsum open '+"\""+matsumFileName+"\""
                    line2='ascii matsum plot 12 '+str(self.Accel[i])
                    line3='xyplot 1 xoffset '+ str(self.offset[i])+' yoffset 0 xscale 1 yscale 0.0001020304'
                    line4='xyplot 1 filter sae  60.00 sec 0'
                    line5='xyplot 1 savefile ms_csv '+ cwd_l + "/XAcceleration.csv\" 1 all"
                    line6='Writing XY data to file: '+ cwd_l + "/XAcceleration.csv"
                    lsprepostCommandFile.write(line1+"\n"+line2+"\n"+line3+"\n"+line4+"\n"+line5+"\n"+line6+"\n")         

                    #matsumX-Velocity
                    matsumFileName=Name+ext3
                    matsumFilePath=os.path.join(cwd_l,matsumFileName)
                    line1='ascii matsum open '+"\""+matsumFileName+"\""
                    line2='ascii matsum plot 8 '+str(self.Accel[i])
                    line3='xyplot 1 xoffset '+ str(self.offset[i])+' yoffset 0 xscale 1 yscale 0.0036'
                    line4='xyplot 1 filter sae  60.00 sec 0'
                    line5='xyplot 1 savefile ms_csv '+ cwd_l + "/XVelocity.csv\" 1 all"
                    line6='Writing XY data to file: '+ cwd_l + "/XVelocity.csv"
                    lsprepostCommandFile.write(line1+"\n"+line2+"\n"+line3+"\n"+line4+"\n"+line5+"\n"+line6+"\n")         
                
                    #matsum-IE
                    matsumFileName=Name+ext3
                    matsumFilePath=os.path.join(cwd_l,matsumFileName)
                    line1='ascii matsum open '+"\""+matsumFileName+"\""
                    line2='ascii matsum plot 1 '
                    for part in range (len(self.Parts[i])):
                        line2=line2+str(self.Parts[i][part])+'/'
                    line3='xyplot 1 select all'
                    lne4='xyplot 1 operation sum_curves all'
                    line5='xyplot 1 xoffset '+ str(self.offset[i])+' yoffset 0 xscale 1 yscale 1 '
                    line6='xyplot 1 savefile ms_csv '+ cwd_l + "/IE.csv\" 1 all"
                    line7='Writing XY data to file: '+ cwd_l + "/IE.csv"              
                    lsprepostCommandFile.write(line1+"\n"+line2+"\n"+line3+"\n"+line4+"\n"+line5+"\n"+line6+"\n"+line7+"\n") 

                    #matsum-KE
                    matsumFileName = Name+ext3
                    matsumFilePath=os.path.join(cwd_l,matsumFileName)
                    line1='ascii matsum open '+"\""+matsumFileName+"\""
                    line2='ascii matsum plot 2 '
                    for part in range (len(self.Parts[i])):
                        line2=line2+str(self.Parts[i][part])+'/'
                    line3='xyplot 1 select all'
                    lne4='xyplot 1 operation sum_curves all'
                    line5='xyplot 1 xoffset '+ str(self.offset[i])+' yoffset 0 xscale 1 yscale 1 '
                    line6='xyplot 1 savefile ms_csv '+ cwd_l + "/KE.csv\" 1 all"
                    line7='Writing XY data to file: '+ cwd_l + "/KE.csv"               
                    lsprepostCommandFile.write(line1+"\n"+line2+"\n"+line3+"\n"+line4+"\n"+line5+"\n"+line6+"\n"+line7+"\n") 

                    #matsum-HG
                    matsumFileName = Name+ext3
                    matsumFilePath=os.path.join(cwd_l,matsumFileName)
                    line1='ascii matsum open '+"\""+matsumFileName+"\""
                    line2='ascii matsum plot 3 '
                    for part in range (len(self.Parts[i])):
                        line2=line2+str(self.Parts[i][part])+'/'
                    line3='xyplot 1 select all'
                    lne4='xyplot 1 operation sum_curves all'
                    line5='xyplot 1 xoffset '+ str(self.offset[i])+' yoffset 0 xscale 1 yscale 1 '
                    line6='xyplot 1 savefile ms_csv '+ cwd_l + "/HGE.csv\" 1 all"
                    line7='Writing XY data to file: '+ cwd_l + "/HGE.csv"                
                    lsprepostCommandFile.write(line1+"\n"+line2+"\n"+line3+"\n"+line4+"\n"+line5+"\n"+line6+"\n"+line7+"\n") 
                        
                    #sleout-FE
                    sleoutFileName = Name+ext4
                    sleoutFilePath = os.path.join(cwd_l,sleoutFileName)
                    line1 = 'ascii sleout open '+"\""+sleoutFileName+"\""
                    line2 = 'ascii sleout plot 3 all'
                    line3 = 'xyplot 1 operation sum_curves all'
                    line4='xyplot 1 xoffset '+ str(self.offset[i])+' yoffset 0 xscale 1 yscale 1 '
                    line5='xyplot 1 savefile ms_csv '+ cwd_l + "/FE.csv\" 1 all"
                    line6='Writing XY data to file: '+ cwd_l + "/FE.csv"                
                    lsprepostCommandFile.write(line1+"\n"+line2+"\n"+line3+"\n"+line4+"\n"+line5+"\n"+line6+"\n") 
                         
                    #sleout-sum of S/M
                    sleoutFileName = Name+ext4
                    sleoutFilePath = os.path.join(cwd_l,sleoutFileName)
                    line1 = 'ascii sleout open '+"\""+sleoutFileName+"\""
                    line2 = 'ascii sleout plot 4 all'
                    line3 = 'xyplot 1 operation sum_curves all'
                    line4='xyplot 1 xoffset '+ str(self.offset[i])+' yoffset 0 xscale 1 yscale 1 '
                    line5='xyplot 1 savefile ms_csv '+ cwd_l + "/SM.csv\" 1 all"
                    line6='Writing XY data to file: '+ cwd_l + "/SM.csv"                
                    lsprepostCommandFile.write(line1+"\n"+line2+"\n"+line3+"\n"+line4+"\n"+line5+"\n"+line6+"\n")

                    #glstat
                    glstatFileName = Name+ext5
                    glstatFilePath = os.path.join(cwd_l,glstatFileName)
                    line1 = 'ascii glstat open '+"\""+glstatFileName+"\""+" 0"
                    line2 = 'ascii glstat plot 1 Wall-1'
                    line3 = 'ascii glstat addplot 2 Wall-1'
                    line4 = 'ascii glstat addplot 3 Wall-1'
                    line5 = 'ascii glstat addplot 4 Wall-1'
                    line6 = 'ascii glstat addplot 5 Wall-1'
                    line7 = 'ascii glstat addplot 6 Wall-1'
                    line8 = 'ascii glstat addplot 7 Wall-1'
                    line9 = 'ascii glstat addplot 8 Wall-1'
                    line10 = 'ascii glstat addplot 9 Wall-1'
                    line11 = 'ascii glstat addplot 17 Wall-1'
                    line12 = 'ascii glstat addplot 14 Wall-1'
                    line13 = 'xyplot 1 select all'
                    line14='xyplot 1 xoffset '+ str(self.offset[i])+' yoffset 0 xscale 1 yscale 1 '
                    line15='xyplot 1 savefile ms_csv '+ cwd_l + "/AllEnergies.csv\" 1 all"
                    line16='Writing XY data to file: '+ cwd_l + "/AllEnergies.csv"
                    line17='exit'                
                    lsprepostCommandFile.write(line1+"\n"+line2+"\n"+line3+"\n"+line4+"\n"+line5+"\n"+line6+"\n"+line7+"\n"+line8+"\n"+line9+"\n"+line10+"\n"+line11+"\n"+line12+"\n"+line13+"\n"+line14+"\n"+line15+"\n"+line16+"\n"+line17)                       
                    lsprepostCommandFile.close()
                        
            lsprepostMasterFile.close()

    def createLsPrePostPhase2CommandFile(self):
        root = Tk()
        root.withdraw()
        parentPath = filedialog.askdirectory(parent = root, initialdir="/", title='Select the parent path to locate LS-PrePost Phase2 command files for Phase 2')
        for i in range (len(self.parameters.vehicleType)):
            cwd_i = os.path.join(parentPath+"/"+self.parameters.phaseName[1],self.parameters.vehicleType[i])
            masterFilePath = os.path.join(cwd_i,'lsprepostMasterFile.sh')
            lsprepostMasterFile = open (masterFilePath,'w')
            lsprepostMasterFile.write('#!/bin/bash'+'\n')
            for j in range (len(self.parameters.barrierBoundary)):
                cwd_j = os.path.join(cwd_i,self.parameters.barrierBoundary[j])
                for l in range (len(self.parameters.anglesOfAttack)):
                    cwd_l = os.path.join(cwd_j,str(self.parameters.anglesOfAttack[l]))
                    for m in range (len(self.parameters.pierLocation)):
                        cwd_m = os.path.join(cwd_l,str(self.parameters.pierLocation[m])) 
                        ext='.cfile'
                        ext1='.rcforc'
                        ext2='.matsum'
                        Name = self.parameters.vehicleType[i]+'_'+self.parameters.barrierBoundary[j]+'_'+str(self.parameters.anglesOfAttack[l])+'_'+str(self.parameters.pierLocation[m])
                        lsprepostCommandFilePath = os.path.join(cwd_m,Name+ext)
                        lsprepostMasterFile.write('cd ' + cwd_m + '\n')
                        lsprepostMasterFile.write('/home/ls-dyna/lsprepost4.8_common/lspp48 c='+'/"'+Name+ext+'/"'+' -nographics'+'\n')
                        lsprepostCommandFile = open (lsprepostCommandFilePath,'w')
                        #rcforcContactForces    
                        rcforcFileName=Name+ext1   
                        rcforcFilePath=os.path.join(cwd_m,rcforcFileName)
                        line1='ascii rcforc open '+"\""+rcforcFileName+"\""
                        if i==0:
                            line2='ascii rcforc plot 4 Sl-26'
                            line3='xyplot 1 xoffset 0 yoffset 0 xscale 1 yscale 0.001'
                            line4='xyplot 1 savefile ms_csv '+ cwd_m + "/pi.csv\" 1 all"
                            line5='Writing XY data to file: '+ cwd_m + "/pi.csv"
                            lsprepostCommandFile.write(line1+"\n"+line2+"\n"+line3+"\n"+line4+"\n"+line5+"\n")
                        if i==1:
                            line2='ascii rcforc addplot 4 Sl-3/Sl-38'
                            line3='xyplot 1 operation sum_curves all'
                            line4='xyplot 1 xoffset 0 yoffset 0 xscale 1 yscale 0.001'
                            line5='xyplot 1 savefile ms_csv '+ cwd_m + "/pi.csv\" 1 all"
                            line6='Writing XY data to file: '+ cwd_m + "/pi.csv"
                            lsprepostCommandFile.write(line1+"\n"+line2+"\n"+line3+"\n"+line4+"\n"+line5+"\n"+line6+"\n")

                        #matsumX-Displacement
                        matsumFileName=Name+ext2
                        matsumFilePath=os.path.join(cwd_m,matsumFileName)
                        line1='ascii matsum open '+"\""+matsumFileName+"\""
                        line2='ascii matsum plot 7 5000002'
                        line3='xyplot 1 savefile ms_csv '+ cwd_m + "/di.csv\" 1 all"
                        line4='Writing XY data to file: '+ cwd_m + "/di.csv"
                        line5='exit'
                        lsprepostCommandFile.write(line1+"\n"+line2+"\n"+line3+"\n"+line4+"\n"+line5+"\n")         

                        lsprepostCommandFile.close()
                        
            lsprepostMasterFile.close()