#region ENVIRONMENT SETTINGS
import os
from tkinter import *
from tkinter import filedialog
import subprocess
import time
from xlwt import Workbook
import csv
from Parameters import Parameters
from InputFileAndCommandFiles import Create
#endregion

class Postprocess():
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()
        self.parentPath = filedialog.askdirectory(parent = self.root, initialdir="/", title='Select the parent path of the simulations results')
        self.parameters = Parameters()
        self.create = Create()

    def runLsprepostPhase1(self):
        root = Tk()
        root.withdraw()
        lsprepost = filedialog.askopenfile(parent = root, initialdir="C:\Program Files\LSTC", title='Select lsprepost executable')
        output = Workbook()
        for i in range (len(self.parameters.vehicleType)):
            cwd_i = os.path.join(self.parentPath+"/"+self.parameters.phaseName[0],self.parameters.vehicleType[i])
            for j in range (len(self.parameters.barrierBoundary)):
                cwd_j = os.path.join(cwd_i,self.parameters.barrierBoundary[j])
                for k in range (len(self.parameters.barrierLength)):
                    cwd_k = os.path.join(cwd_j,str(self.parameters.barrierLength[k]))
                    for l in range (len(self.parameters.anglesOfAttack)):
                        cwd_l = os.path.join(cwd_k,str(self.parameters.anglesOfAttack[l]))
                        Name = self.parameters.vehicleType[i]+'_'+self.parameters.barrierBoundary[j]+'_'+str(self.parameters.barrierLength[k])+'_'+str(self.parameters.anglesOfAttack[l])
                        lsdynaCommandFilePath = os.path.join(cwd_l,Name+'.cfile')
                        process = subprocess.Popen([lsprepost.name, lsdynaCommandFilePath], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        if i==0:
                            time.sleep(10)
                        else:
                            time.sleep(20)

    def runLsprepostPhase2(self):
        root = Tk()
        root.withdraw()
        lsprepost = filedialog.askopenfile(parent = root, initialdir="C:\Program Files\LSTC", title='Select lsprepost executable')
        output = Workbook()
        for i in range (len(self.parameters.vehicleType)):
            cwd_i = os.path.join(self.parentPath+"/"+self.parameters.phaseName[1],self.parameters.vehicleType[i])
            for j in range (len(self.parameters.barrierBoundary)):
                cwd_j = os.path.join(cwd_i,self.parameters.barrierBoundary[j])
                for k in range (1,len(self.parameters.barrierLength)):
                    cwd_k = os.path.join(cwd_j,str(self.parameters.barrierLength[k]))
                    for l in range (len(self.parameters.anglesOfAttack)):
                        cwd_l = os.path.join(cwd_k,str(self.parameters.anglesOfAttack[l]))
                        for m in range (len(self.parameters.pierLocation[j])):
                            cwd_m = os.path.join(cwd_l,str(self.parameters.pierLocation[j][m]))
                            Name = self.parameters.vehicleType[i]+'_'+self.parameters.barrierBoundary[j]+'_'+str(self.parameters.barrierLength[k])+'_'+str(self.parameters.anglesOfAttack[l])+'_'+str(self.parameters.pierLocation[j][m])
                            lsdynaCommandFilePath = os.path.join(cwd_m,Name+'.cfile')
                            process = subprocess.Popen([lsprepost.name, lsdynaCommandFilePath], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                            if i==0:
                                time.sleep(3)
                            else:
                                time.sleep(10)

    def collectDataPhase1(self):
        sheet1 = output.add_sheet('ContactForce')
        sheet2 = output.add_sheet('Displacement')
        sheet3 = output.add_sheet('Velocity')
        sheet4 = output.add_sheet('Acceleration')
        sheet5 = output.add_sheet('IE')
        sheet6 = output.add_sheet('KE')
        sheet7 = output.add_sheet('HGE')
        sheet8 = output.add_sheet('DampingE')
        sheet9 = output.add_sheet('SlidingE')
        sheet10 = output.add_sheet('ExternalW')
        sheet11 = output.add_sheet('StoneW')

        rcforc_counter=0
        displacement_counter=0
        velocity_counter=0
        acceleration_counter=0
        IE_counter=0
        KE_counter=0
        HGE_counter=0
        DampingE_counter=0
        SlidingE_counter=0
        ExternalW_counter=0
        StoneW_counter=0

        for i in range (len(self.parameters.vehicleType)):
            cwd_i = os.path.join(self.parentPath+"/"+self.parameters.phaseName[0],self.parameters.vehicleType[i])
            for j in range (len(self.parameters.barrierBoundary)):
                cwd_j = os.path.join(cwd_i,self.parameters.barrierBoundary[j])
                for k in range (len(self.parameters.barrierLength)):
                    cwd_k = os.path.join(cwd_j,str(self.parameters.barrierLength[k]))
                    for l in range (len(self.parameters.anglesOfAttack)):
                        cwd_l = os.path.join(cwd_k,str(self.parameters.anglesOfAttack[l]))
                        Name = self.parameters.vehicleType[i]+'_'+self.parameters.barrierBoundary[j]+'_'+str(self.parameters.barrierLength[k])+'_'+str(self.parameters.anglesOfAttack[l])
                
                        rcforc=os.path.join(cwd_l,"RCFORC.csv")
                        displacement=os.path.join(cwd_l,"displacement.csv")
                        velocity=os.path.join(cwd_l,"XVelocity.csv")
                        acceleration=os.path.join(cwd_l,"XAcceleration.csv")
                        Energy=os.path.join(cwd_l,"AllEnergies.csv")

                        #reading contact force
                        with open(rcforc,'r') as file1:
                            reader = csv.reader(file1)
                            next(reader)
                            next(reader)
                            row=0
                            sheet1.write(row,2*rcforc_counter,Name)
                            for line in reader:
                                sheet1.write(row+1,2*rcforc_counter,float(line[0]))
                                sheet1.write(row+1,2*rcforc_counter+1,float(line[1]))
                                row+=1

                        #reading nodal displacement
                        with open(displacement,'r') as file2:
                            reader = csv.reader(file2)
                            next(reader)
                            next(reader)
                            sheet2.write(0,2*displacement_counter,Name)
                            disp=[[]]
                    
                            for line in reader:                        
                                for node in range (len(self.create.Nodes[k])):
                                    disp.append([])
                                    disp[node].append(float(line[node+1]))

                            for Node in range (len(self.create.Nodes[k])):
                                sheet2.write(Node+1,2*displacement_counter,100*Node)
                                sheet2.write(Node+1,2*displacement_counter+1,-min(disp[Node]))
                        

                        #reading CG velocity
                        with open(velocity,'r') as file3:
                            reader = csv.reader(file3)
                            next(reader)
                            next(reader)
                            row=0
                            sheet3.write(row,2*velocity_counter,Name)
                            for line in reader:
                                sheet3.write(row+1,2*velocity_counter,float(line[0]))
                                sheet3.write(row+1,2*velocity_counter+1,float(line[1]))
                                row+=1
                
                        #reading CG acceleration
                        with open(acceleration,'r') as file4:
                            reader = csv.reader(file4)
                            next(reader)
                            next(reader)
                            row=0
                            sheet4.write(row,2*acceleration_counter,Name)
                            for line in reader:
                                sheet4.write(row+1,2*acceleration_counter,float(line[0]))
                                sheet4.write(row+1,2*acceleration_counter+1,float(line[1]))
                                row+=1

                        #reading internal energy
                        with open(Energy,'r') as file5:
                            reader = csv.reader(file5)
                            next(reader)
                            next(reader)
                            sheet5.write(0,2*IE_counter,Name)
                            row=0
                            for line in reader:
                                sheet5.write(row+1,2*IE_counter,float(line[0]))
                                sheet5.write(row+1,2*IE_counter+1,float(line[2]))
                                row+=1

                        #reading kinetic energy
                        with open(Energy,'r') as file6:
                            reader = csv.reader(file6)
                            next(reader)
                            next(reader)
                            sheet6.write(0,2*KE_counter,Name)
                            row=0
                            for line in reader:
                                sheet6.write(row+1,2*KE_counter,float(line[0]))
                                sheet6.write(row+1,2*KE_counter+1,float(line[1]))
                                row+=1

                        #reading hourglass energy
                        with open(Energy,'r') as file7:
                            reader = csv.reader(file7)
                            next(reader)
                            next(reader)
                            sheet7.write(0,2*HGE_counter,Name)
                            row=0
                            for line in reader:
                                sheet7.write(row+1,2*HGE_counter,float(line[0]))
                                sheet7.write(row+1,2*HGE_counter+1,float(line[6]))
                                row+=1
                    
                        #reading damping energy
                        with open(Energy,'r') as file8:
                            reader = csv.reader(file8)
                            next(reader)
                            next(reader)
                            sheet8.write(0,2*DampingE_counter,Name)
                            row=0
                            for line in reader:
                                sheet8.write(row+1,2*DampingE_counter,float(line[0]))
                                sheet8.write(row+1,2*DampingE_counter+1,float(line[5]))
                                row+=1

                        #reading sliding energy
                        with open(Energy,'r') as file9:
                            reader = csv.reader(file9)
                            next(reader)
                            next(reader)
                            sheet9.write(0,2*SlidingE_counter,Name)
                            row=0
                            for line in reader:
                                sheet9.write(row+1,2*SlidingE_counter,float(line[0]))
                                sheet9.write(row+1,2*SlidingE_counter+1,float(line[8]))
                                row+=1

                        #reading external work energy
                        with open(Energy,'r') as file10:
                            reader = csv.reader(file10)
                            next(reader)
                            next(reader)
                            sheet10.write(0,2*ExternalW_counter,Name)
                            row=0
                            for line in reader:
                                sheet10.write(row+1,2*ExternalW_counter,float(line[0]))
                                sheet10.write(row+1,2*ExternalW_counter+1,float(line[9]))
                                row+=1
                        
                        #reading stoneWall energy
                        with open(Energy,'r') as file11:
                            reader = csv.reader(file11)
                            next(reader)
                            next(reader)
                            sheet11.write(0,2*StoneW_counter,Name)
                            row=0
                            for line in reader:
                                sheet11.write(row+1,2*StoneW_counter,float(line[0]))
                                sheet11.write(row+1,2*StoneW_counter+1,float(line[11]))
                                row+=1
               
                        rcforc_counter+=1
                        displacement_counter+=1
                        velocity_counter+=1
                        acceleration_counter+=1
                        IE_counter+=1
                        KE_counter+=1
                        HGE_counter+=1
                        DampingE_counter+=1
                        SlidingE_counter+=1
                        ExternalW_counter+=1
                        StoneW_counter+=1
        self.resultsPath = os.path.join(self.parentPath+"/"+self.parameters.phaseName[0],"results.xls")
        output.save(self.resultsPath)
               
    def collectDataPhase2(self): 
        output = Workbook()
        sheet1 = output.add_sheet('ContactForce')
        sheet2 = output.add_sheet('Displacement')

        rcforc_counter=0
        displacement_counter=0

        for i in range (len(self.parameters.vehicleType)):
            cwd_i = os.path.join(self.parentPath+"/"+self.parameters.phaseName[1],self.parameters.vehicleType[i])
            for j in range (len(self.parameters.barrierBoundary)):
                cwd_j = os.path.join(cwd_i,self.parameters.barrierBoundary[j])
                for k in range (1,len(self.parameters.barrierLength)):
                    cwd_k = os.path.join(cwd_j,str(self.parameters.barrierLength[k]))
                    for l in range (len(self.parameters.anglesOfAttack)):
                        cwd_l = os.path.join(cwd_k,str(self.parameters.anglesOfAttack[l]))
                        for m in range (len(self.parameters.pierLocation[j])):
                            cwd_m = os.path.join(cwd_l,str(self.parameters.pierLocation[j][m]))
                            Name = self.parameters.vehicleType[i]+'_'+self.parameters.barrierBoundary[j]+'_'+str(self.parameters.barrierLength[k])+'_'+str(self.parameters.anglesOfAttack[l])+'_'+str(self.parameters.pierLocation[j][m])

                            rcforc=os.path.join(cwd_m,"pi.csv")
                            displacement=os.path.join(cwd_m,"di.csv")

                            #reading contact force
                            with open(rcforc,'r') as file1:
                                reader = csv.reader(file1)
                                next(reader)
                                next(reader)
                                row=0
                                sheet1.write(row,2*rcforc_counter,Name)
                                for line in reader:
                                    sheet1.write(row+1,2*rcforc_counter,float(line[0]))
                                    sheet1.write(row+1,2*rcforc_counter+1,float(line[1]))
                                    row+=1

                            #reading nodal displacement
                            with open(displacement,'r') as file2:
                                reader = csv.reader(file2)
                                next(reader)
                                next(reader)
                                row=0
                                sheet2.write(row,2*displacement_counter,Name)
                                di=[] 
                                di_max=[]                   
                                for line in reader:  
                                    sheet2.write(row+1,2*displacement_counter,float(line[0]))
                                    sheet2.write(row+1,2*displacement_counter+1,float(line[1]))
                                    di.append(float(line[1]))
                                    row+=1
                                di_max.append(max(di))
               
                            rcforc_counter+=1
                            displacement_counter+=1
   
        self.resultsPath = os.path.join(self.parentPath+"/"+self.parameters.phaseName[1],"results.xls")
        output.save(self.resultsPath)
               
 