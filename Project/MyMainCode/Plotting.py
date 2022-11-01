#region ENVIRONMENT SETTING
from matplotlib import pyplot as plt
import matplotlib.font_manager as font_manager
import pandas as pd
import numpy as np
from numpy import nan
from tkinter import *
from tkinter import filedialog
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage, AnnotationBbox)
from matplotlib.cbook import get_sample_data
import matplotlib.image as mpimg
import os
from xlwt import Workbook
from scipy import integrate
from PIL import Image
import cv2
#endregion


class plottingPhase1Results():
    def __init__(self):
        root = Tk()
        root.withdraw()
        self.parentPath = filedialog.askopenfile(parent = root, initialdir="/", title='Select the results file')
        self.dirName = filedialog.askdirectory(parent = root, initialdir="/", title='Select the destination of the figures')
        self.fonts = [font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=14),font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=12),font_manager.FontProperties(family='Times New Roman', weight='normal', style='normal', size=10)]
        self.legends=['20m', '30m']
        self. analysis_file = Workbook() 
        
    def readingPhase1Results(self):
        #reading contact force
        contactforce = pd.read_excel(self.parentPath.name, sheet_name=0, header=0)
        self.contactforce_header=[]
        self.contactforce_arrays=[[]]
        counter=0
        for col in contactforce.columns:
            self.contactforce_header.append(col)
            my_array=np.array(contactforce[self.contactforce_header[counter]])
            new_array = my_array[np.logical_not(np.isnan(my_array))]
            self.contactforce_arrays.append(new_array)
            counter+=1 
        #reading displacement
        displacement = pd.read_excel(self.parentPath.name, sheet_name=1, header=0)
        self.displacement_header=[]
        self.displacement_arrays=[[]]
        counter=0
        for col in displacement.columns:
            self.displacement_header.append(col)
            my_array=np.array(displacement[self.displacement_header[counter]])
            new_array = my_array[np.logical_not(np.isnan(my_array))]
            self.displacement_arrays.append(new_array)
            counter+=1
        #reading velocity
        velocity = pd.read_excel(self.parentPath.name, sheet_name=2, header=0)
        self.velocity_header=[]
        self.velocity_arrays=[[]]
        counter=0
        for col in velocity.columns:
            self.velocity_header.append(col)
            my_array=np.array(velocity[self.velocity_header[counter]])
            new_array = my_array[np.logical_not(np.isnan(my_array))]
            self.velocity_arrays.append(new_array)
            counter+=1
        #reading acceleration    
        acceleration = pd.read_excel(self.parentPath.name, sheet_name=3, header=0)
        self.acceleration_header=[]
        self.acceleration_arrays=[[]]
        counter=0
        for col in acceleration.columns:
            self.acceleration_header.append(col)
            my_array=np.array(acceleration[self.acceleration_header[counter]])
            new_array = my_array[np.logical_not(np.isnan(my_array))]
            self.acceleration_arrays.append(new_array)
            counter+=1      
        #reading IE
        IE = pd.read_excel(self.parentPath.name, sheet_name=4, header=0)
        self.IE_header=[]
        self.IE_arrays=[[]]
        counter=0
        for col in IE.columns:
            self.IE_header.append(col)
            my_array=np.array(IE[self.IE_header[counter]])
            new_array = my_array[np.logical_not(np.isnan(my_array))]
            self.IE_arrays.append(new_array)
            counter+=1
        #reading KE
        KE = pd.read_excel(self.parentPath.name, sheet_name=5, header=0)
        self.KE_header=[]
        self.KE_arrays=[[]]
        counter=0
        for col in KE.columns:
            self.KE_header.append(col)
            my_array=np.array(KE[self.KE_header[counter]])
            new_array = my_array[np.logical_not(np.isnan(my_array))]
            self.KE_arrays.append(new_array)
            counter+=1
        #redaing HGE
        HGE = pd.read_excel(self.parentPath.name, sheet_name=6, header=0)
        self.HGE_header=[]
        self.HGE_arrays=[[]]
        counter=0
        for col in HGE.columns:
            self.HGE_header.append(col)
            my_array=np.array(HGE[self.HGE_header[counter]])
            new_array = my_array[np.logical_not(np.isnan(my_array))]
            self.HGE_arrays.append(new_array)
            counter+=1
        #reading Damping E
        DampingE = pd.read_excel(self.parentPath.name, sheet_name=7, header=0)
        self.DampingE_header=[]
        self.DampingE_arrays=[[]]
        counter=0
        for col in DampingE.columns:
            self.DampingE_header.append(col)
            my_array=np.array(DampingE[self.DampingE_header[counter]])
            new_array = my_array[np.logical_not(np.isnan(my_array))]
            self.DampingE_arrays.append(new_array)
            counter+=1
        #reading Sliding E
        SlidingE = pd.read_excel(self.parentPath.name, sheet_name=8, header=0)
        self.SlidingE_header=[]
        self.SlidingE_arrays=[[]]
        counter=0
        for col in SlidingE.columns:
            self.SlidingE_header.append(col)
            my_array=np.array(SlidingE[self.SlidingE_header[counter]])
            new_array = my_array[np.logical_not(np.isnan(my_array))]
            self.SlidingE_arrays.append(new_array)
            counter+=1
        #reading External W
        ExternalW = pd.read_excel(self.parentPath.name, sheet_name=9, header=0)
        self.ExternalW_header=[]
        self.ExternalW_arrays=[[]]
        counter=0
        for col in ExternalW.columns:
            self.ExternalW_header.append(col)
            my_array=np.array(ExternalW[self.ExternalW_header[counter]])
            new_array = my_array[np.logical_not(np.isnan(my_array))]
            self.ExternalW_arrays.append(new_array)
            counter+=1
        #reading stone W
        StoneW = pd.read_excel(self.parentPath.name, sheet_name=10, header=0)
        self.StoneW_header=[]
        self.StoneW_arrays=[[]]
        counter=0
        for col in StoneW.columns:
            self.StoneW_header.append(col)
            my_array=np.array(StoneW[self.StoneW_header[counter]])
            new_array = my_array[np.logical_not(np.isnan(my_array))]
            self.StoneW_arrays.append(new_array)
            counter+=1
        #reading Validation
        Validation = pd.read_excel(self.parentPath.name, sheet_name=11, header=0)
        self.Validation_header=[]
        self.Validation_arrays=[[]]
        counter=0
        for col in Validation.columns:
            self.Validation_header.append(col)
            my_array=np.array(Validation[self.Validation_header[counter]])
            new_array = my_array[np.logical_not(np.isnan(my_array))]
            self.Validation_arrays.append(new_array)
            counter+=1
        #reading LengthEffect
        Length = pd.read_excel(self.parentPath.name, sheet_name=12, header=0)
        self.Length_header=[]
        self.Length_arrays=[[]]
        counter=0
        for col in Length.columns:
            self.Length_header.append(col)
            my_array=np.array(Length[self.Length_header[counter]])
            new_array = my_array[np.logical_not(np.isnan(my_array))]
            self.Length_arrays.append(new_array)
            counter+=1

    def analyzingPhase1Results(self):
        root = Tk()
        root.withdraw()
        dirName = filedialog.askdirectory(parent = root, initialdir="/", title='Select the destination of the analysis results file')
        sheet1 = self.analysis_file.add_sheet('Contact force')
        sheet1.write(0,0,'Simulation')
        sheet1.write(1,0,'Max contact force (kN)')
        sheet1.write(2,0,'Time of occurance (s)')
        sheet2 = analysis_file.add_sheet('Displacement')
        sheet2.write(0,0,'Simulation')
        sheet2.write(1,0,'Max displacement (mm)')
        sheet2.write(2,0,'Position along the barrier (m)')
        sheet3 = analysis_file.add_sheet('Velocity')
        sheet3.write(0,0,'Simulation')
        sheet3.write(1,0,'Initial velocity (kmph)')
        sheet3.write(2,0,'Final velocity (kmph)')
        sheet3.write(3,0,'Reduction %')
        sheet4 = analysis_file.add_sheet('Acceleration')
        sheet4.write(0,0,'Simulation')
        sheet4.write(1,0,'Initial acceleration (xg)')
        sheet4.write(2,0,'Final acceleration (xg)')
        sheet4.write(3,0,'Reduction %')
        sheet5 = analysis_file.add_sheet('KE')
        sheet5.write(0,0,'Simulation')
        sheet5.write(1,0,'Initial KE (MJ)')
        sheet5.write(2,0,'Final KE (MJ)')
        sheet5.write(3,0,'Reduction %')
        for index in range (16):
            sheet1.write(0,index+1,self.contactforce_header[2*index])
            max_value=max(self.contactforce_arrays[2*index+2])
            sheet1.write(1,index+1,float(max_value))
            max_index=np.argmax(self.contactforce_arrays[2*index+2])
            sheet1.write(2,index+1,float(self.contactforce_arrays[2*index+1][max_index]))

            sheet2.write(0,index+1,self.displacement_header[2*index])
            max_value=max(self.displacement_arrays[2*index+2])
            sheet2.write(1,index+1,float(max_value))
            max_index=np.argmax(self.displacement_arrays[2*index+2])
            sheet2.write(2,index+1,float(self.displacement_arrays[2*index+1][max_index]))

            sheet3.write(0,index+1,self.velocity_header[2*index])
            max_value=max(self.velocity_arrays[2*index+2])
            min_value=min(self.velocity_arrays[2*index+2])
            sheet3.write(1,index+1,float(max_value))
            sheet3.write(2,index+1,float(min_value))
            sheet3.write(3,index+1,float((1-min_value/max_value)*100))

            sheet4.write(0,index+1,self.acceleration_header[2*index])
            max_value=max(self.acceleration_arrays[2*index+2])
            min_value=min(self.acceleration_arrays[2*index+2])
            sheet4.write(1,index+1,float(max_value))
            sheet4.write(2,index+1,float(min_value))
            sheet4.write(3,index+1,float((1-min_value/max_value)*100))

            sheet5.write(0,index+1,self.KE_header[2*index])
            max_value=max(self.KE_arrays[2*index+2])/1000000000
            min_value=min(self.KE_arrays[2*index+2])/1000000000
            sheet5.write(1,index+1,float(max_value))
            sheet5.write(2,index+1,float(min_value))
            sheet5.write(3,index+1,float((1-min_value/max_value)*100))

        analysis_file.save(dirName+"/analysis.xls")
    
    def validation(self):
    #FIGURE FOR MODEL VALIDATION CONTACT FORCE 
        plt.plot(self.Validation_arrays[1],self.Validation_arrays[2],"b--",label='Cao et al. simulation', markersize=5)
        plt.plot(self.Validation_arrays[3],self.Validation_arrays[4],"k-",label='This study', markersize=5, markevery=15)
        plt.title('Contact force of TL-4 simulation',fontproperties=self.fonts[0])
        plt.xlabel('Time (s)',fontproperties=self.fonts[1])
        plt.ylabel('Force (kN)',fontproperties=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        plt.yticks()
        plt.xlim(0,0.45)
        plt.ylim(ymin=0)
        plt.legend(prop=self.fonts[1])
        plt.savefig(self.dirName+"/validationForceSUT.png", dpi=1080)
        plt.show()
        plt.clf()

        plt.plot(self.Validation_arrays[5],self.Validation_arrays[6],"b--",label='Cao et al. simulation', markersize=5)
        plt.plot(self.Validation_arrays[7],self.Validation_arrays[8],"k-",label='This study', markersize=5, markevery=15)
        plt.title('Contact force of TL-5 simulation',fontproperties=self.fonts[0])
        plt.xlabel('Time (s)',fontproperties=self.fonts[1])
        plt.ylabel('Force (kN)',fontproperties=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        plt.yticks()
        plt.xlim(0,1.0)
        plt.ylim(ymin=0)
        plt.legend(prop=self.fonts[1])
        plt.savefig(self.dirName+'/validationForceTST.png', dpi=1080)
        plt.show()
        plt.clf()
        
        #FIGURE FOR MODEL VALIDATION ENERGY 
        plt.plot(self.KE_arrays[1],(self.KE_arrays[6][0]+self.ExternalW_arrays[6])/1000000000,"k-",label='Total energy', markersize=3, markevery=15)
        plt.plot(self.KE_arrays[1],self.KE_arrays[6]/1000000000,"r-x",label='Kinetic energy', markersize=3, markevery=15)
        plt.plot(self.IE_arrays[1],self.IE_arrays[6]/1000000000,"b--",label='Internal energy', markersize=3, markevery=15)
        plt.plot(self.HGE_arrays[1],self.HGE_arrays[6]/1000000000,"y-d",label='Hourglass energy', markersize=3, markevery=15)
        plt.plot(self.DampingE_arrays[1],self.DampingE_arrays[6]/1000000000,"m-^",label='Damping energy', markersize=3, markevery=15)
        plt.plot(self.SlidingE_arrays[1],self.SlidingE_arrays[6]/1000000000,"c-o",label='Sliding energy', markersize=3, markevery=15) 
        plt.plot(self.StoneW_arrays[1],self.StoneW_arrays[6]/1000000000,"g-*",label='Rigid wall energy', markersize=3, markevery=15)
        plt.title('Energy balance in TL-4 simulation',fontproperties=self.fonts[0])
        plt.xlabel('Time (s)',fontproperties=self.fonts[1])
        plt.ylabel('Energy (MJ)',fontproperties=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        plt.yticks()
        plt.xlim(0,0.5)
        plt.ylim(ymin=0)
        plt.legend(prop=self.fonts[1])
        plt.savefig(self.dirName+'/EnergyComponentsSUT.png', dpi=1080)
        plt.show()
        plt.clf()

        plt.plot(self.KE_arrays[1],((self.KE_arrays[6]+self.IE_arrays[6]+self.HGE_arrays[6]+self.DampingE_arrays[6]+self.SlidingE_arrays[6]+self.StoneW_arrays[6])/(self.KE_arrays[6][0]+self.ExternalW_arrays[6])),"k-", markersize=3, markevery=15)    
        plt.title('Energy ratio in TL-4 simulation',fontproperties=self.fonts[0])
        plt.xlabel('Time (s)',fontproperties=self.fonts[1])
        plt.ylabel('Energy ratio',fontproperties=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        plt.yticks()
        plt.xlim(0,0.5)
        plt.ylim(ymin=0.9, ymax=1.1)
        #plt.legend(prop=self.fonts[1])
        plt.savefig(self.dirName+'/EnergyRatioSUT.png', dpi=1080)
        plt.show()
        plt.clf()

        plt.plot(self.KE_arrays[21],(self.KE_arrays[22][0]+self.ExternalW_arrays[22])/1000000000,"k-",label='Total energy', markersize=3, markevery=15)
        plt.plot(self.KE_arrays[21],self.KE_arrays[22]/1000000000,"r-x",label='Kinetic energy', markersize=3, markevery=15)
        plt.plot(self.IE_arrays[21],self.IE_arrays[22]/1000000000,"b--",label='Internal energy', markersize=3, markevery=15)
        plt.plot(self.HGE_arrays[21],self.HGE_arrays[22]/1000000000,"y-d",label='Hourglass energy', markersize=3, markevery=15)
        plt.plot(self.DampingE_arrays[21],self.DampingE_arrays[22]/1000000000,"m-^",label='Damping energy', markersize=3, markevery=15)
        plt.plot(self.SlidingE_arrays[21],self.SlidingE_arrays[22]/1000000000,"c-o",label='Sliding energy', markersize=3, markevery=15)
        plt.plot(self.StoneW_arrays[21],self.StoneW_arrays[22]/1000000000,"g-*",label='Rigid wall energy', markersize=3, markevery=15)
        plt.title('Energy balance in TL-5 simulation',fontproperties=self.fonts[0])
        plt.xlabel('Time (s)',fontproperties=self.fonts[1])
        plt.ylabel('Energy (MJ)',fontproperties=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        plt.yticks()
        plt.xlim(0,1.0)
        plt.ylim(ymin=0)
        plt.legend(prop=self.fonts[1])
        plt.savefig(self.dirName+'/EnergyComponentsTST.png', dpi=1080)
        plt.show()
        plt.clf()

        plt.plot(self.KE_arrays[21],((self.KE_arrays[22]+self.IE_arrays[22]+self.HGE_arrays[22]+self.DampingE_arrays[22]+self.SlidingE_arrays[22]+self.StoneW_arrays[22])/(self.KE_arrays[22][0]+self.ExternalW_arrays[22])),"k-", markersize=3, markevery=15)    
        plt.title('Energy ratio in TL-5 simulation',fontproperties=self.fonts[0])
        plt.xlabel('Time (s)',fontproperties=self.fonts[1])
        plt.ylabel('Energy ratio',fontproperties=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        plt.yticks()
        plt.xlim(0,1.0)
        plt.ylim(ymin=0.9, ymax=1.1)
        #plt.legend(prop=self.fonts[1])
        plt.savefig(self.dirName+'/EnergyRatioTST.png', dpi=1080)
        plt.show()
        plt.clf()        

    def contactForce(self):
        root = Tk()
        root.withdraw()
        dirName1 = filedialog.askdirectory(parent = root, initialdir="/", title='Select the location of the annotaion figures')
        #FIGURES FOR CONTACT FORCE
        max_values=[]
        for arr in range(1,len(self.contactforce_arrays),2):
            max_value=max(self.contactforce_arrays[arr+1])
            max_index=np.argmax(self.contactforce_arrays[arr+1])
            max_values.append([self.contactforce_arrays[arr][max_index],max_value])

        #SUT
        titles=['','Fixed barriers - angle of attack = 15°','Free barriers - angle of attack = 15°','Fixed barriers - angle of attack = 25°','Free barriers - angle of attack = 25°']
        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot(self.contactforce_arrays[1], self.contactforce_arrays[2],"k-", label= self.legends[0], markersize=3, markevery=15)
        L2 = ax.plot(self.contactforce_arrays[5], self.contactforce_arrays[6],"b--", label= self.legends[1], markersize=3, markevery=15)
        P1 = ax.plot(max_values[2][0], max_values[2][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title(titles[1], fontproperties=self.fonts[0])
        ax.set_xlabel('Time (s)', fontproperties=self.fonts[1])
        ax.set_ylabel('Force (kN)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(0,0.5)
        ax.set_ylim(ymin=0)
        pic1 = get_sample_data(dirName1+"\Annotate\SUTFixed1530.PNG", asfileobj=False)
        arr_img1 = plt.imread(pic1, format='png')
        imagebox1 = OffsetImage(arr_img1, zoom=0.115)
        imagebox1.image.axes = ax        
        box1 = AnnotationBbox(imagebox1, (max_values[2][0], max_values[2][1]), xybox=(0.25, max_values[2][1]-120), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=200",facecolor='red'))
        ax.add_artist(box1)
        plt.savefig(self.dirName+'/CF_TL4'+titles[1]+'.png', dpi=1080)
        plt.show()
        plt.clf()

        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot(self.contactforce_arrays[9], self.contactforce_arrays[10],"k-", label= self.legends[0], markersize=3, markevery=15)
        L2 = ax.plot(self.contactforce_arrays[13], self.contactforce_arrays[14],"b--", label= self.legends[1], markersize=3, markevery=15)
        P1 = ax.plot(max_values[6][0], max_values[6][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title(titles[2], fontproperties=self.fonts[0])
        ax.set_xlabel('Time (s)', fontproperties=self.fonts[1])
        ax.set_ylabel('Force (kN)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(0,0.5)
        ax.set_ylim(ymin=0) 
        pic1 = get_sample_data(dirName1+"\Annotate\SUTFree1530.PNG", asfileobj=False)
        arr_img1 = plt.imread(pic1, format='png')
        imagebox1 = OffsetImage(arr_img1, zoom=0.115)
        imagebox1.image.axes = ax        
        box1 = AnnotationBbox(imagebox1, (max_values[6][0], max_values[6][1]), xybox=(0.13, max_values[6][1]-30), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=200",facecolor='red'))
        ax.add_artist(box1)
        plt.savefig(self.dirName+'/CF_TL4'+titles[2]+'.png', dpi=1080)
        plt.show()
        plt.clf()

        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot(self.contactforce_arrays[3], self.contactforce_arrays[4],"k-", label= self.legends[0], markersize=3, markevery=15)
        L2 = ax.plot(self.contactforce_arrays[7], self.contactforce_arrays[8],"b--", label= self.legends[1], markersize=3, markevery=15)
        P1 = ax.plot(max_values[1][0], max_values[1][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title(titles[3], fontproperties=self.fonts[0])
        ax.set_xlabel('Time (s)', fontproperties=self.fonts[1])
        ax.set_ylabel('Force (kN)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(0,0.5)
        ax.set_ylim(ymin=0)
        pic1 = get_sample_data(dirName1+"\Annotate\SUTFixed2520.PNG", asfileobj=False)
        arr_img1 = plt.imread(pic1, format='png')
        imagebox1 = OffsetImage(arr_img1, zoom=0.115)
        imagebox1.image.axes = ax        
        box1 = AnnotationBbox(imagebox1, (max_values[1][0], max_values[1][1]), xybox=(0.25, max_values[1][1]-150), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=200",facecolor='red'))
        ax.add_artist(box1)
        plt.savefig(self.dirName+'/CF_TL4'+titles[3]+'.png', dpi=1080)
        plt.show()
        plt.clf()

        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot(self.contactforce_arrays[11], self.contactforce_arrays[12],"k-", label= self.legends[0], markersize=3, markevery=15)
        L2 = ax.plot(self.contactforce_arrays[15], self.contactforce_arrays[16],"b--", label= self.legends[1], markersize=3, markevery=15)
        P1 = ax.plot(max_values[7][0], max_values[7][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title(titles[4], fontproperties=self.fonts[0])
        ax.set_xlabel('Time (s)', fontproperties=self.fonts[1])
        ax.set_ylabel('Force (kN)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(0,0.5)
        ax.set_ylim(ymin=0)
        pic1 = get_sample_data(dirName1+"\Annotate\SUTFree2530.PNG", asfileobj=False)
        arr_img1 = plt.imread(pic1, format='png')
        imagebox1 = OffsetImage(arr_img1, zoom=0.115)
        imagebox1.image.axes = ax        
        box1 = AnnotationBbox(imagebox1, (max_values[7][0], max_values[7][1]), xybox=(0.18, max_values[7][1]-70), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=200",facecolor='red'))
        ax.add_artist(box1)
        plt.savefig(self.dirName+'/CF_TL4'+titles[4]+'.png', dpi=1080)
        plt.show()
        plt.clf()
        
        #TST
        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot(self.contactforce_arrays[17], self.contactforce_arrays[18],"k-", label= self.legends[0], markersize=3, markevery=15)
        L2 = ax.plot(self.contactforce_arrays[21], self.contactforce_arrays[22],"b--", label= self.legends[1], markersize=3, markevery=15)
        P1 = ax.plot(max_values[10][0], max_values[10][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title(titles[1], fontproperties=self.fonts[0])
        ax.set_xlabel('Time (s)', fontproperties=self.fonts[1])
        ax.set_ylabel('Force (kN)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(0,1.0)
        ax.set_ylim(ymin=0)
        pic1 = get_sample_data(dirName1+"\Annotate\TSTFixed1530.PNG", asfileobj=False)
        arr_img1 = plt.imread(pic1, format='png')
        imagebox1 = OffsetImage(arr_img1, zoom=0.115)
        imagebox1.image.axes = ax        
        box1 = AnnotationBbox(imagebox1, (max_values[10][0], max_values[10][1]), xybox=(0.6, max_values[10][1]-250), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=200",facecolor='red'))
        ax.add_artist(box1)
        plt.savefig(self.dirName+'/CF_TL5'+titles[1]+'.png', dpi=1080)
        plt.show()
        plt.clf()

        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot(self.contactforce_arrays[25], self.contactforce_arrays[26],"k-", label= self.legends[0], markersize=3, markevery=15)
        L2 = ax.plot(self.contactforce_arrays[29], self.contactforce_arrays[30],"b--", label= self.legends[1], markersize=3, markevery=15)
        P1 = ax.plot(max_values[12][0], max_values[12][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title(titles[2], fontproperties=self.fonts[0])
        ax.set_xlabel('Time (s)', fontproperties=self.fonts[1])
        ax.set_ylabel('Force (kN)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(0,1.0)
        ax.set_ylim(ymin=0) 
        pic1 = get_sample_data(dirName1+"\Annotate\TSTFree1520.PNG", asfileobj=False)
        arr_img1 = plt.imread(pic1, format='png')
        imagebox1 = OffsetImage(arr_img1, zoom=0.115)
        imagebox1.image.axes = ax        
        box1 = AnnotationBbox(imagebox1, (max_values[12][0], max_values[12][1]), xybox=(0.45, max_values[12][1]-100), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=200",facecolor='red'))
        ax.add_artist(box1)
        plt.savefig(self.dirName+'/CF_TL5'+titles[2]+'.png', dpi=1080)
        plt.show()
        plt.clf()

        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot(self.contactforce_arrays[19], self.contactforce_arrays[20],"k-", label= self.legends[0], markersize=3, markevery=15)
        L2 = ax.plot(self.contactforce_arrays[23], self.contactforce_arrays[24],"b--", label= self.legends[1], markersize=3, markevery=15)
        P1 = ax.plot(max_values[9][0], max_values[9][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title(titles[3], fontproperties=self.fonts[0])
        ax.set_xlabel('Time (s)', fontproperties=self.fonts[1])
        ax.set_ylabel('Force (kN)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(0,1.0)
        ax.set_ylim(ymin=0)
        pic1 = get_sample_data(dirName1+"\Annotate\TSTFixed2520.PNG", asfileobj=False)
        arr_img1 = plt.imread(pic1, format='png')
        imagebox1 = OffsetImage(arr_img1, zoom=0.115)
        imagebox1.image.axes = ax        
        box1 = AnnotationBbox(imagebox1, (max_values[9][0], max_values[9][1]), xybox=(0.4, max_values[9][1]-250), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=200",facecolor='red'))
        ax.add_artist(box1)
        plt.savefig(self.dirName+'/CF_TL5'+titles[3]+'.png', dpi=1080)
        plt.show()
        plt.clf()

        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot(self.contactforce_arrays[27], self.contactforce_arrays[28],"k-", label= self.legends[0], markersize=3, markevery=15)
        L2 = ax.plot(self.contactforce_arrays[31], self.contactforce_arrays[32],"b--", label= self.legends[1], markersize=3, markevery=15)
        P1 = ax.plot(max_values[15][0], max_values[15][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title(titles[4], fontproperties=self.fonts[0])
        ax.set_xlabel('Time (s)', fontproperties=self.fonts[1])
        ax.set_ylabel('Force (kN)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(0,1.0)
        ax.set_ylim(ymin=0) 
        pic1 = get_sample_data(dirName1+"\Annotate\TSTFree2530.PNG", asfileobj=False)
        arr_img1 = plt.imread(pic1, format='png')
        imagebox1 = OffsetImage(arr_img1, zoom=0.115)
        imagebox1.image.axes = ax        
        box1 = AnnotationBbox(imagebox1, (max_values[15][0], max_values[15][1]), xybox=(0.81, max_values[15][1]-200), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=200",facecolor='red'))
        ax.add_artist(box1)
        plt.savefig(self.dirName+'/CF_TL5'+titles[4]+'.png', dpi=1080)
        plt.show()
        plt.clf()

    def displacement(self):
        root = Tk()
        root.withdraw()
        dirName1 = filedialog.askdirectory(parent = root, initialdir="/", title='Select the location of the annotaion figures')
        #FIGURES FOR DISPLACEMENT
        max_values=[]
        for arr in range(1,len(self.displacement_arrays),2):
            max_value=max(self.displacement_arrays[arr+1])
            max_index=np.argmax(self.displacement_arrays[arr+1])
            max_values.append([self.displacement_arrays[arr][max_index]/1000,max_value])
        titles=['','Fixed barriers - angle of attack = 15°','Fixed barriers - angle of attack = 25°','Free barriers - angle of attack = 15°','Free barriers - angle of attack = 25°']
        #SUT
        plt.plot(self.displacement_arrays[1]/1000, self.displacement_arrays[2],"k-", label= self.legends[0], markersize=2)
        plt.plot(self.displacement_arrays[5]/1000, self.displacement_arrays[6],"b--", label= self.legends[1], markersize=2)
        plt.title(titles[1], fontproperties=self.fonts[0])
        plt.xlabel('Position along the barrier (m)', fontproperties=self.fonts[1])
        plt.ylabel('Maximum lateral displacement (mm)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        plt.xlim(0,29)
        plt.ylim(ymin=0)
        plt.annotate('at '+str(max_values[0][0])+' m', xy=(max_values[0][0], max_values[0][1]),  xycoords='data', xytext=(max_values[0][0]+4.3, max_values[0][1]), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center')
        plt.annotate('at '+str(max_values[2][0])+' m', xy=(max_values[2][0], max_values[2][1]),  xycoords='data', xytext=(max_values[2][0]+4.6, max_values[2][1]), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center')
        plt.savefig(self.dirName+'/DTL4_'+titles[1]+'.png', dpi=1080)
        plt.show()
        plt.clf() 
    
        plt.plot(self.displacement_arrays[3]/1000, self.displacement_arrays[4],"k-", label= self.legends[0], markersize=2)
        plt.plot(self.displacement_arrays[7]/1000, self.displacement_arrays[8],"b--", label= self.legends[1], markersize=2)
        plt.title(titles[2], fontproperties=self.fonts[0])
        plt.xlabel('Position along the barrier (m)', fontproperties=self.fonts[1])
        plt.ylabel('Maximum lateral displacement (mm)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        plt.xlim(0,29)
        plt.ylim(ymin=0)
        plt.annotate('at '+str(max_values[1][0])+' m', xy=(max_values[1][0], max_values[1][1]),  xycoords='data', xytext=(max_values[1][0]+4.3, max_values[1][1]), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center')
        plt.annotate('at '+str(max_values[3][0])+' m', xy=(max_values[3][0], max_values[3][1]),  xycoords='data', xytext=(max_values[3][0]+4.6, max_values[3][1]), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center')
        plt.savefig(self.dirName+'/DTL4_'+titles[2]+'.png', dpi=1080)
        plt.show()
        plt.clf() 

        plt.plot(self.displacement_arrays[9]/1000, self.displacement_arrays[10],"k-", label= self.legends[0], markersize=2)
        plt.plot(self.displacement_arrays[13]/1000, self.displacement_arrays[14],"b--", label= self.legends[1], markersize=2)
        plt.title(titles[3], fontproperties=self.fonts[0])
        plt.xlabel('Position along the barrier (m)', fontproperties=self.fonts[1])
        plt.ylabel('Maximum lateral displacement (mm)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        plt.xlim(0,29)
        plt.ylim(ymin=0)
        plt.annotate('at '+str(max_values[4][0])+' m', xy=(max_values[4][0], max_values[4][1]),  xycoords='data', xytext=(max_values[4][0]-4.3, max_values[4][1]), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center')
        plt.annotate('at '+str(max_values[6][0])+' m', xy=(max_values[6][0], max_values[6][1]),  xycoords='data', xytext=(max_values[6][0]+4.6, max_values[6][1]), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center')
        plt.savefig(self.dirName+'/DTL4_'+titles[3]+'.png', dpi=1080)
        plt.show()
        plt.clf() 
     
        plt.plot(self.displacement_arrays[11]/1000, self.displacement_arrays[12],"k-", label= self.legends[0], markersize=2)
        plt.plot(self.displacement_arrays[15]/1000, self.displacement_arrays[16],"b--", label= self.legends[1], markersize=2)
        plt.title(titles[4], fontproperties=self.fonts[0])
        plt.xlabel('Position along the barrier (m)', fontproperties=self.fonts[1])
        plt.ylabel('Maximum lateral displacement (mm)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        plt.xlim(0,29)
        plt.ylim(ymin=0)
        plt.annotate('at '+str(max_values[5][0])+' m', xy=(max_values[5][0], max_values[5][1]),  xycoords='data', xytext=(max_values[5][0]-4.3, max_values[5][1]), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center')
        plt.annotate('at '+str(max_values[7][0])+' m', xy=(max_values[7][0], max_values[7][1]),  xycoords='data', xytext=(max_values[7][0]+4.6, max_values[7][1]), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center')
        plt.savefig(self.dirName+'/DTL4_'+titles[4]+'.png', dpi=1080)
        plt.show()
        plt.clf()
        
        #TST
        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot(self.displacement_arrays[17]/1000, self.displacement_arrays[18],"k-", label= self.legends[0], markersize=2)
        L2 = ax.plot(self.displacement_arrays[21]/1000, self.displacement_arrays[22],"b--", label= self.legends[1], markersize=2)
        P1 = ax.plot(max_values[8][0], max_values[8][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        P2 = ax.plot(0.2,64, marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title(titles[1], fontproperties=self.fonts[0])
        ax.set_xlabel('Position along the barrier (m)', fontproperties=self.fonts[1])
        ax.set_ylabel('Maximum lateral displacement (mm)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(0,29)
        ax.set_ylim(ymin=0)
        ax.annotate('at '+str(max_values[8][0])+' m', xy=(max_values[8][0], max_values[8][1]),  xycoords='data', xytext=(max_values[8][0]-4, max_values[8][1]), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center')
        ax.annotate('at '+str(max_values[10][0])+' m', xy=(max_values[10][0], max_values[10][1]),  xycoords='data', xytext=(max_values[10][0]+3.6, max_values[10][1]), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center')        
        pic1 = get_sample_data(dirName1+"\Annotate\TL5FIXED2015START.PNG", asfileobj=False)
        pic2 = get_sample_data(dirName1+"\Annotate\TL5FIXED2015END.PNG", asfileobj=False)
        arr_img1 = plt.imread(pic1, format='png')
        arr_img2 = plt.imread(pic2, format='png')
        imagebox1 = OffsetImage(arr_img1, zoom=0.115)
        imagebox2 = OffsetImage(arr_img2, zoom=0.115)
        imagebox1.image.axes = ax
        imagebox2.image.axes = ax        
        box1 = AnnotationBbox(imagebox1, (0.2, 64), xybox=(5, 66.5), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=0,angleB=90,rad=50",facecolor='red'))
        box2 = AnnotationBbox(imagebox2, (max_values[8][0], max_values[8][1]), xybox=(max_values[8][0]+3.3, max_values[8][1]-20), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=0,rad=200.0",facecolor='red'))
        ax.add_artist(box1)
        ax.add_artist(box2)
        plt.savefig(self.dirName+'/DTL5_'+titles[1]+'.png', dpi=1080)
        plt.show()
        plt.clf() 

        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot(self.displacement_arrays[19]/1000, self.displacement_arrays[20],"k-", label= self.legends[0], markersize=2)
        L2 = ax.plot(self.displacement_arrays[23]/1000, self.displacement_arrays[24],"b--", label= self.legends[1], markersize=2)
        P1 = ax.plot(max_values[11][0], max_values[11][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title(titles[2], fontproperties=self.fonts[0])
        ax.set_xlabel('Position along the barrier (m)', fontproperties=self.fonts[1])
        ax.set_ylabel('Maximum lateral displacement (mm)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(0,29)
        ax.set_ylim(ymin=0)
        ax.annotate('at '+str(max_values[9][0])+' m', xy=(max_values[9][0], max_values[9][1]),  xycoords='data', xytext=(max_values[9][0]+4.3, max_values[9][1]), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center')
        ax.annotate('at '+str(max_values[11][0])+' m', xy=(max_values[11][0], max_values[11][1]),  xycoords='data', xytext=(max_values[11][0]+4.3, max_values[11][1]), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center')
        pic1 = get_sample_data(dirName1+"\Annotate\TL5FIXED3025.PNG", asfileobj=False)
        arr_img1 = plt.imread(pic1, format='png')
        imagebox1 = OffsetImage(arr_img1, zoom=0.115)
        imagebox1.image.axes = ax        
        box1 = AnnotationBbox(imagebox1, (max_values[11][0], max_values[11][1]), xybox=(13, max_values[11][1]-20), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=0,angleB=90,rad=500",facecolor='red'))
        ax.add_artist(box1)
        plt.savefig(self.dirName+'/DTL5_'+titles[2]+'.png', dpi=1080)
        plt.show()
        plt.clf() 

        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot(self.displacement_arrays[25]/1000, self.displacement_arrays[26],"k-", label= self.legends[0], markersize=2)
        L2 = ax.plot(self.displacement_arrays[29]/1000, self.displacement_arrays[30],"b--", label= self.legends[1], markersize=2)
        P1 = ax.plot(max_values[14][0], max_values[14][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title(titles[3], fontproperties=self.fonts[0])
        ax.set_xlabel('Position along the barrier (m)', fontproperties=self.fonts[1])
        ax.set_ylabel('Maximum lateral displacement (mm)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(0,29)
        ax.set_ylim(ymin=0)
        ax.annotate('at '+str(max_values[12][0])+' m', xy=(max_values[12][0], max_values[12][1]),  xycoords='data', xytext=(max_values[12][0]-4.3, max_values[12][1]), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center')
        ax.annotate('at '+str(max_values[14][0])+' m', xy=(max_values[14][0], max_values[14][1]),  xycoords='data', xytext=(max_values[14][0]-4.3, max_values[14][1]), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center')
        pic1 = get_sample_data(dirName1+"\Annotate\TL5FREE3015.PNG", asfileobj=False)
        arr_img1 = plt.imread(pic1, format='png')
        imagebox1 = OffsetImage(arr_img1, zoom=0.115)
        imagebox1.image.axes = ax        
        box1 = AnnotationBbox(imagebox1, (max_values[14][0], max_values[14][1]), xybox=(13, max_values[14][1]-50), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=0,angleB=90,rad=200.0",facecolor='red'))
        ax.add_artist(box1)
        plt.savefig(self.dirName+'/DTL5_'+titles[3]+'.png', dpi=1080)
        plt.show()
        plt.clf() 
     
        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot(self.displacement_arrays[27]/1000, self.displacement_arrays[28],"k-", label= self.legends[0], markersize=2)
        L1 = ax.plot(self.displacement_arrays[31]/1000, self.displacement_arrays[32],"b--", label= self.legends[1], markersize=2)
        P1 = ax.plot(max_values[15][0], max_values[15][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title(titles[4], fontproperties=self.fonts[0])
        ax.set_xlabel('Position along the barrier (m)', fontproperties=self.fonts[1])
        ax.set_ylabel('Maximum lateral displacement (mm)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(0,29)
        ax.set_ylim(ymin=0)
        ax.annotate('at '+str(max_values[13][0])+' m', xy=(max_values[13][0], max_values[13][1]),  xycoords='data', xytext=(max_values[13][0]-4.3, max_values[13][1]), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center')
        ax.annotate('at '+str(max_values[15][0])+' m', xy=(max_values[15][0], max_values[15][1]),  xycoords='data', xytext=(max_values[15][0]+4.6, max_values[15][1]), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center')
        pic1 = get_sample_data(dirName1+"\Annotate\TL5FREE3025.PNG", asfileobj=False)
        arr_img1 = plt.imread(pic1, format='png')
        imagebox1 = OffsetImage(arr_img1, zoom=0.115)
        imagebox1.image.axes = ax        
        box1 = AnnotationBbox(imagebox1, (max_values[15][0], max_values[15][1]), xybox=(8, 400), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',facecolor='red'))
        ax.add_artist(box1)
        plt.savefig(self.dirName+'/DTL5_'+titles[4]+'.png', dpi=1080)
        plt.show()
        plt.clf()     

    def velocity(self):
        #FIGURES FOR VELOCITY
        titles=['','Fixed barriers - angle of attack = 15°','Free barriers - angle of attack = 15°','Fixed barriers - angle of attack = 25°','Free barriers - angle of attack = 25°']
        for i in range (1,3):
            plt.plot(self.velocity_arrays[2*i-1], self.velocity_arrays[2*i],"k-", label= 'TL-4: '+self.legends[0], markersize=3, markevery=15)
            plt.plot(self.velocity_arrays[2*i+3], self.velocity_arrays[2*i+4],"b--", label= 'TL-4: '+self.legends[1], markersize=3, markevery=15)
            plt.plot(self.velocity_arrays[2*i+15], self.velocity_arrays[2*i+16],"r-x", label= 'TL-5: '+self.legends[0], markersize=3, markevery=15)
            plt.plot(self.velocity_arrays[2*i+19], self.velocity_arrays[2*i+20],"g-.", label= 'TL-5: '+self.legends[1], markersize=3, markevery=15)
            plt.title(titles[2*i-1], fontproperties=self.fonts[0])
            plt.xlabel('Time (s)', fontproperties=self.fonts[1])
            plt.ylabel('Longitudinal velocity (km/h)', fontproperties=self.fonts[1])
            plt.legend(prop=self.fonts[1], loc='lower left')
            plt.xticks(fontproperties=self.fonts[2])
            plt.yticks(fontproperties=self.fonts[2])
            plt.xlim(0,1.0)
            plt.ylim(ymin=40, ymax=95)
            plt.savefig(dirName+'/V_'+titles[2*i-1]+'.png', dpi=1080)
            plt.show()
            plt.clf()
            plt.plot(self.velocity_arrays[2*i+7], self.velocity_arrays[2*i+8],"k-", label= 'TL-4: '+self.legends[0], markersize=3, markevery=15)
            plt.plot(self.velocity_arrays[2*i+11], self.velocity_arrays[2*i+12],"b--", label= 'TL-4: '+self.legends[1], markersize=3, markevery=15)
            plt.plot(self.velocity_arrays[2*i+23], self.velocity_arrays[2*i+24],"r-x", label= 'TL-5: '+self.legends[0], markersize=3, markevery=15)
            plt.plot(self.velocity_arrays[2*i+27], self.velocity_arrays[2*i+28],"g-.", label= 'TL-5: '+self.legends[1], markersize=3, markevery=15)
            plt.title(titles[2*i], fontproperties=self.fonts[0])
            plt.xlabel('Time (s)', fontproperties=self.fonts[1])
            plt.ylabel('Longitudinal velocity (km/h)', fontproperties=self.fonts[1])
            plt.legend(prop=self.fonts[1],loc='lower left')
            plt.xticks(fontproperties=self.fonts[2])
            plt.yticks(fontproperties=self.fonts[2])
            plt.xlim(0,1.0)
            plt.ylim(ymin=40, ymax=95) 
            plt.savefig(self.dirName+'/V_'+titles[2*i]+'.png', dpi=1080)
            plt.show()
            plt.clf()

    def lengthEffects(self):
        #FIGURES FOR lengthEffects
        titles=['','Fixed barriers - angle of attack = 15°','Free barriers - angle of attack = 15°','Fixed barriers - angle of attack = 25°','Free barriers - angle of attack = 25°']
        for i in range (1,3):
            plt.plot(self.Length_arrays[2*i-1], self.Length_arrays[2*i],"r-x", label= '10m', markersize=3, markevery=15)
            plt.plot(self.Length_arrays[2*i+3], self.Length_arrays[2*i+4],"k-", label=self.legends[0], markersize=3, markevery=15)
            plt.plot(self.Length_arrays[2*i+7], self.Length_arrays[2*i+8],"b--", label= self.legends[1], markersize=3, markevery=15) 
            plt.title(titles[2*i-1], fontproperties=self.fonts[0])
            plt.xlabel('Time (s)', fontproperties=self.fonts[1])
            plt.ylabel('Longitudinal velocity (km/h)', fontproperties=self.fonts[1])
            plt.legend(prop=self.fonts[1], loc='lower left')
            plt.xticks(fontproperties=self.fonts[2])
            plt.yticks(fontproperties=self.fonts[2])
            plt.xlim(0,0.5)
            plt.ylim(ymin=40, ymax=95)
            plt.savefig(self.dirName+'/VLE_'+titles[2*i-1]+'.png', dpi=1080)
            plt.show()
            plt.clf()
            plt.plot(self.Length_arrays[2*i+11], self.Length_arrays[2*i+12],"r-x", label= '10m', markersize=3, markevery=15)
            plt.plot(self.Length_arrays[2*i+15], self.Length_arrays[2*i+16],"k-", label= self.legends[0], markersize=3, markevery=15)
            plt.plot(self.Length_arrays[2*i+19], self.Length_arrays[2*i+20],"b--", label=self.legends[1], markersize=3, markevery=15)
            plt.title(titles[2*i], fontproperties=self.fonts[0])
            plt.xlabel('Time (s)', fontproperties=self.fonts[1])
            plt.ylabel('Longitudinal velocity (km/h)', fontproperties=self.fonts[1])
            plt.legend(prop=self.fonts[1],loc='lower left')
            plt.xticks(fontproperties=self.fonts[2])
            plt.yticks(fontproperties=self.fonts[2])
            plt.xlim(0,0.5)
            plt.ylim(ymin=40, ymax=95) 
            plt.savefig(self.dirName+'/VLE_'+titles[2*i]+'.png', dpi=1080)
            plt.show()
            plt.clf()

    def energy(self):
        #FIGURES FOR KINETIC AND INTERNAL ENERGY
        titles=['','Fixed barriers - angle of attack = 15°','Free barriers - angle of attack = 15°','Fixed barriers - angle of attack = 25°','Free barriers - angle of attack = 25°']
        titles1=['','Fixed barriers - angle of attack = 15°','Free barriers - angle of attack = 15°','Fixed barriers - angle of attack = 25°','Free barriers - angle of attack = 25°']
        for i in range (1,3):
            plt.plot(self.KE_arrays[2*i-1], self.KE_arrays[2*i]/1000000000,"k-", label= 'Kinetic energy_'+ self.legends[0], markersize=3, markevery=15)
            plt.plot(self.KE_arrays[2*i+3], self.KE_arrays[2*i+4]/1000000000,"b--", label= 'Kinetic energy_'+self.legends[1], markersize=3, markevery=15)
            plt.plot(self.IE_arrays[2*i-1], self.IE_arrays[2*i]/1000000000,"r-x", label= 'Internal energy_'+self.legends[0], markersize=5, markevery=15)
            plt.plot(self.IE_arrays[2*i+3], self.IE_arrays[2*i+4]/1000000000,"g-.", label= 'Internal energy_'+self.legends[1], markersize=5, markevery=15)
            plt.title(titles[2*i-1], fontproperties=self.fonts[0])
            plt.xlabel('Time (s)', fontproperties=self.fonts[1])
            plt.ylabel('Energy (MJ)', fontproperties=self.fonts[1])
            plt.legend(prop=self.fonts[1], loc='center left')
            plt.xticks(fontproperties=self.fonts[2])
            plt.yticks(fontproperties=self.fonts[2])
            plt.xlim(0,0.5)
            plt.ylim(ymin=0) 
            plt.savefig(self.dirName+'/E_TL4'+titles[2*i-1]+'.png', dpi=1080)
            plt.show()
            plt.clf()

            plt.plot(self.KE_arrays[2*i+7], self.KE_arrays[2*i+8]/1000000000,"k-", label= 'Kinetic energy_'+ self.legends[0], markersize=3, markevery=15)
            plt.plot(self.KE_arrays[2*i+11], self.KE_arrays[2*i+12]/1000000000,"b--", label= 'Kinetic energy_'+self.legends[1], markersize=3, markevery=15)
            plt.plot(self.IE_arrays[2*i+7], self.IE_arrays[2*i+8]/1000000000,"r-x", label= 'Internal energy_'+self.legends[0], markersize=5, markevery=15)
            plt.plot(self.IE_arrays[2*i+11], self.IE_arrays[2*i+12]/1000000000,"g-.", label= 'Internal energy_'+self.legends[1], markersize=5, markevery=15)
            plt.title(titles[2*i], fontproperties=self.fonts[0])
            plt.xlabel('Time (s)', fontproperties=self.fonts[1])
            plt.ylabel('Energy (MJ)', fontproperties=self.fonts[1])
            plt.legend(prop=self.fonts[1],loc='center left')
            plt.xticks(fontproperties=self.fonts[2])
            plt.yticks(fontproperties=self.fonts[2])
            plt.xlim(0,0.5)
            plt.ylim(ymin=0) 
            plt.savefig(self.dirName+'/E_TL4'+titles[2*i]+'.png', dpi=1080)
            plt.show()
            plt.clf()

        for i in range (1,3):
            plt.plot(self.KE_arrays[2*i+15], self.KE_arrays[2*i+16]/1000000000,"k-", label= 'Kinetic energy_'+ self.legends[0], markersize=3, markevery=15)
            plt.plot(self.KE_arrays[2*i+19], self.KE_arrays[2*i+20]/1000000000,"b--", label= 'Kinetic energy_'+self.legends[1], markersize=3, markevery=15)
            plt.plot(self.IE_arrays[2*i+15], self.IE_arrays[2*i+16]/1000000000,"r-x", label= 'Internal energy_'+self.legends[0], markersize=5, markevery=15)
            plt.plot(self.IE_arrays[2*i+19], self.IE_arrays[2*i+20]/1000000000,"g-.", label= 'Internal energy_'+self.legends[1], markersize=5, markevery=15)
            plt.title(titles1[2*i-1], fontproperties=self.fonts[0])
            plt.xlabel('Time (s)', fontproperties=self.fonts[1])
            plt.ylabel('Energy (MJ)', fontproperties=self.fonts[1])
            plt.legend(prop=self.fonts[1], loc='center left')
            plt.xticks(fontproperties=self.fonts[2])
            plt.yticks(fontproperties=self.fonts[2])
            plt.xlim(0,1.0)
            plt.ylim(ymin=0) 
            plt.savefig(self.dirName+'/E_TL5'+titles1[2*i-1]+'.png', dpi=1080)
            plt.show()
            plt.clf()

            plt.plot(self.KE_arrays[2*i+23], self.KE_arrays[2*i+24]/1000000000,"k-", label= 'Kinetic energy_'+ self.legends[0], markersize=3, markevery=15)
            plt.plot(self.KE_arrays[2*i+27], self.KE_arrays[2*i+28]/1000000000,"b--", label= 'Kinetic energy_'+self.legends[1], markersize=3, markevery=15)
            plt.plot(self.IE_arrays[2*i+23], self.IE_arrays[2*i+24]/1000000000,"r-x", label= 'Internal energy_'+self.legends[0], markersize=5, markevery=15)
            plt.plot(self.IE_arrays[2*i+27], self.IE_arrays[2*i+28]/1000000000,"g-.", label= 'Internal energy_'+self.legends[1], markersize=5, markevery=15)
            plt.title(titles1[2*i], fontproperties=self.fonts[0])
            plt.xlabel('Time (s)', fontproperties=self.fonts[1])
            plt.ylabel('Energy (MJ)', fontproperties=self.fonts[1])
            plt.legend(prop=self.fonts[1],loc='center left')
            plt.xticks(fontproperties=self.fonts[2])
            plt.yticks(fontproperties=self.fonts[2])
            plt.xlim(0,1.0)
            plt.ylim(ymin=0) 
            plt.savefig(self.dirName+'/E_TL5'+titles1[2*i]+'.png', dpi=1080)
            plt.show()
            plt.clf()

class plottingPhase2Results():
    def __init__(self):
        root = Tk()
        root.withdraw()
        self.parentPath = 'D:\LS-DYNA\6.2-Phase2\results.xls'
        #self.parentPath = filedialog.askopenfile(parent = root, initialdir="C:\\Users\salahatf\Desktop\LS-DYNA\6.2-Phase2", title='Select the results file')
        self.dirName = 'G:\Other computers\My PC\Papers\LS-DYNA_paper 2\Journals\TRR\Figures'
        #self.dirName = filedialog.askdirectory(parent = root, initialdir="G:\Other computers\My PC\Papers\LS-DYNA_paper 2\Journals\TRR", title='Select the destination of the figures')
        self.fonts = [font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=14),font_manager.FontProperties(family='Times New Roman', weight='bold', style='normal', size=12),font_manager.FontProperties(family='Times New Roman', weight='normal', style='normal', size=10)]
        self.legends=['3.1 m','3.6 m','4.1 m']
        self. analysis_file = Workbook() 

    def readingPhase2Results(self):
        #reading contact force 
        sheet1 = self.analysis_file.add_sheet('MaxForceValues')    
        contactforce = pd.read_excel(self.parentPath.name, sheet_name=0, header=0)
        self.contactforce_header=[]
        self.contactforce_arrays=[]
        counter=0
        for col in contactforce.columns:
            self.contactforce_header.append(col)
            my_array=np.array(contactforce[self.contactforce_header[counter]])
            new_array = my_array[np.logical_not(np.isnan(my_array))]
            self.contactforce_arrays.append(new_array)
            counter+=1 
        self.max_force_values=[]

        for arr in range(int(len(self.contactforce_arrays)/2)):
            sheet1.write(0, 2*arr,self.contactforce_header[2*arr])
            max_value=max(self.contactforce_arrays[2*arr+1])
            max_index=np.argmax(self.contactforce_arrays[2*arr+1])
            self.max_force_values.append([self.contactforce_arrays[2*arr][max_index],max_value])
            sheet1.write(1, 2*arr,self.max_force_values[arr][0])
            sheet1.write(1, 2*arr+1,self.max_force_values[arr][1])

        #reading displacement 
        sheet2 = self.analysis_file.add_sheet('MaxDisplacementValues')   
        displacement = pd.read_excel(self.parentPath.name, sheet_name=1, header=0)
        self.displacement_header=[]
        self.displacement_arrays=[]
        counter=0
        for col in displacement.columns:
            self.displacement_header.append(col)
            my_array=np.array(displacement[self.displacement_header[counter]])
            new_array = my_array[np.logical_not(np.isnan(my_array))]   
            self.displacement_arrays.append(new_array)
            counter+=1 
        self.max_displacment_values=[]

        for arr in range(int(len(self.displacement_arrays)/2)):
            sheet2.write(0, 2*arr,self.displacement_header[2*arr])
            max_value=max(self.displacement_arrays[2*arr+1])
            max_index=np.argmax(self.displacement_arrays[2*arr+1])
            self.max_displacment_values.append([self.displacement_arrays[2*arr][max_index],max_value])
            sheet2.write(1, 2*arr,self.max_displacment_values[arr][0])
            sheet2.write(1, 2*arr+1,self.max_displacment_values[arr][1])
        
        self.analysis_file.save(self.dirName+"/analysis.xls")

    def analyzingPhase2Results(self):  
        sheet3 = self.analysis_file.add_sheet('ESF')
        sheet3.write(0, 0,'Model and simulation')
        sheet3.write(1, 0,'PIF')
        sheet3.write(2, 0,'Model 1')
        sheet3.write(3, 0,'Model 2')
        sheet3.write(4, 0,'Model 3')
        

        #Model 1: Global with non-zero
        for i in range(int(len(self.contactforce_arrays)/2)):
            sheet3.write(0, i+1,self.contactforce_header[2*i])
            sheet3.write(1, i+1,max(self.contactforce_arrays[2*i+1]))
            filteredTime = [0]#Starting time = 0
            filteredForce = [0]#Starting force = 0
            step = 0.001
            for j in range (len(self.contactforce_arrays[2*i+1])):
                if self.contactforce_arrays[2*i+1][j] != 0:
                    filteredTime.append(step)
                    filteredForce.append(self.contactforce_arrays[2*i+1][j])
                    step+=0.001
            integ = integrate.simpson (filteredForce,filteredTime)
            ESF = integ/step
            sheet3.write(2, i+1,ESF)
            if i ==0:
                fig = plt.figure()
                ax = fig.add_subplot()
                L1 = ax.plot(filteredTime, filteredForce,"k-", label= 'Modified', markersize=3, markevery=15)
                L2 = ax.plot(self.contactforce_arrays[0], self.contactforce_arrays[1],"b--", label= 'Original', markersize=3, markevery=15)
                L3 = ax.plot([0,filteredTime[-1]], [820,820],"r-", markersize=3, markevery=15)
                P1 = ax.plot(0, 820, marker="o", markersize=5,markeredgecolor="red", markerfacecolor="k")
                P2 = ax.plot(filteredTime[-1], 820, marker="o", markersize=5,markeredgecolor="red", markerfacecolor="k")
                ax.set_title('The modified GESF model', fontproperties=self.fonts[0])
                ax.set_xlabel('Time (s)', fontproperties=self.fonts[1])
                ax.set_ylabel('Contact Force (kN)', fontproperties=self.fonts[1])
                plt.legend(prop=self.fonts[1])
                plt.xticks(fontproperties=self.fonts[2])
                plt.yticks(fontproperties=self.fonts[2])
                ax.set_xlim(0,0.5)
                ax.set_ylim(ymin=0)
                plt.annotate('Effective impact time', xy=(filteredTime[-1]/2,820),  xycoords='data', xytext=(0.08,780), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(arrowstyle='<|-,head_length=0.2, head_width=0.2',connectionstyle="angle,angleA=0,angleB=90,rad=50",facecolor='red'))
                plt.fill_between(filteredTime, filteredForce, color= "r",alpha= 0.7)
                plt.savefig(self.dirName+'/ESF1.png', dpi=1080)
                plt.show()
                plt.clf()
        
        #Model 2: 50 ms local PIF
        for i in range(int(len(self.contactforce_arrays)/2)):
            max_force=max(self.contactforce_arrays[2*i+1])
            max_index=np.argmax(self.contactforce_arrays[2*i+1])
            max_time= self.contactforce_arrays[2*i][max_index]
            lower_time = max_time - 0.025
            upper_time = max_time + 0.025
            filteredForce = []
            filteredTime = []
            counter = 0
            step=0.001
            for j in range (len(self.contactforce_arrays[2*i+1])):
                if self.contactforce_arrays[2*i][j] >= lower_time and self.contactforce_arrays[2*i][j] <= upper_time:
                    filteredForce.append(self.contactforce_arrays[2*i+1][j])
                    filteredTime.append(lower_time+counter*step)
                    counter+=1
            integ = integrate.simpson (filteredForce,filteredTime)
            ESF = integ/0.05
            sheet3.write(3, i+1,ESF)
            if i ==0:
                fig = plt.figure()
                ax = fig.add_subplot()
                L2 = ax.plot(self.contactforce_arrays[0], self.contactforce_arrays[1],"b--", markersize=3, markevery=15)
                L3 = ax.plot([filteredTime[0],filteredTime[-1]], [780,780],"r-", markersize=3, markevery=15)
                P1 = ax.plot(filteredTime[0], 780, marker="o", markersize=5,markeredgecolor="red", markerfacecolor="k")
                P2 = ax.plot(filteredTime[-1], 780, marker="o", markersize=5,markeredgecolor="red", markerfacecolor="k")
                ax.set_title('The LESF model', fontproperties=self.fonts[0])
                ax.set_xlabel('Time (s)', fontproperties=self.fonts[1])
                ax.set_ylabel('Contact Force (kN)', fontproperties=self.fonts[1])
                #plt.legend(prop=self.fonts[1])
                plt.xticks(fontproperties=self.fonts[2])
                plt.yticks(fontproperties=self.fonts[2])
                ax.set_xlim(0,0.5)
                ax.set_ylim(0,850)
                plt.annotate('50 ms window', xy=(max_time,780),  xycoords='data', xytext=(0.22,800), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(arrowstyle='<|-,head_length=0.2, head_width=0.2',connectionstyle="angle,angleA=0,angleB=90,rad=50",facecolor='red'))
                plt.annotate('tp-25 ms', xy=(filteredTime[0],780),  xycoords='data', xytext=(filteredTime[0]-0.085,700), textcoords='data',fontproperties=self.fonts[1],arrowprops=dict(arrowstyle='<|-,head_length=0.2, head_width=0.2',connectionstyle="angle,angleA=0,angleB=90,rad=50",facecolor='red'))
                plt.annotate('tp+25 ms', xy=(filteredTime[-1],780),  xycoords='data', xytext=(filteredTime[-1]+0.02,700), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(arrowstyle='<|-,head_length=0.2, head_width=0.2',connectionstyle="angle,angleA=0,angleB=90,rad=50",facecolor='red'))
                plt.fill_between(filteredTime, filteredForce, where= (filteredTime[0] < filteredTime)&(filteredTime < filteredTime[-1]),color= "r",alpha= 0.7)
                plt.savefig(self.dirName+'/ESF2.png', dpi=1080)
                plt.show()
                plt.clf()

        #Model 3: Peak of 50 ms Moving Average
        for i in range(int(len(self.contactforce_arrays)/2)):
            window_size = 50
            j = 0
            # Initialize an empty list to store moving averages
            moving_averages_time = []
            moving_averages = []
            # Loop through the array to consider
            # every window of size 3
            while j < len(self.contactforce_arrays[2*i+1]) - window_size + 1:
    
                # Store elements from i to i+window_size
                # in list to get the current window
                window = self.contactforce_arrays[2*i+1][j : j + window_size]
  
                # Calculate the average of current window
                window_average = round(sum(window) / window_size, 3)
      
                # Store the average of current
                # window in moving average list
                moving_averages.append(window_average)
                moving_averages_time.append(self.contactforce_arrays[2*i][j])
      
                # Shift window to right by one position
                j += 1
            ESF = max(moving_averages)
            sheet3.write(4, i+1,ESF)
            if i ==0:
                fig = plt.figure()
                ax = fig.add_subplot()
                L1 = ax.plot(moving_averages_time, moving_averages,"k-", label= 'FMSA', markersize=3, markevery=15)
                L2 = ax.plot(self.contactforce_arrays[0], self.contactforce_arrays[1],"b--", label= 'Original', markersize=3, markevery=15)
                P1 = ax.plot(moving_averages_time[np.argmax(moving_averages)],max(moving_averages), marker="o", markersize=5,markeredgecolor="red", markerfacecolor="g")
                ax.set_title('The PFMSA model', fontproperties=self.fonts[0])
                ax.set_xlabel('Time (s)', fontproperties=self.fonts[1])
                ax.set_ylabel('Contact Force (kN)', fontproperties=self.fonts[1])
                plt.legend(prop=self.fonts[1])
                plt.xticks(fontproperties=self.fonts[2])
                plt.yticks(fontproperties=self.fonts[2])
                ax.set_xlim(0,0.5)
                ax.set_ylim(ymin=0)
                plt.annotate('PFMSA', xy=(moving_averages_time[np.argmax(moving_averages)],max(moving_averages)),  xycoords='data', xytext=(moving_averages_time[np.argmax(moving_averages)]-0.1,max(moving_averages)+100), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(arrowstyle='<|-,head_length=0.2, head_width=0.2',connectionstyle="angle,angleA=0,angleB=90,rad=50",facecolor='red'))
                #plt.fill_between(moving_averages_time, moving_averages, color= "r",alpha= 0.7)
                plt.savefig(self.dirName+'/ESF3.png', dpi=1080)
                plt.show()
                plt.clf()      
        self.analysis_file.save(self.dirName+"/analysis.xls")
              
    def contactForce(self):
        root = Tk()
        root.withdraw()
        dirName1 = filedialog.askdirectory(parent = root, initialdir="G:\Other computers\My PC\Papers\LS-DYNA_paper 2\Journals\TRR", title='Select the location of the annotaion figures')
        #FIGURES FOR CONTACT FORCE
        max_values=[]
        for arr in range(0,len(self.contactforce_arrays),2):
            max_value=max(self.contactforce_arrays[arr+1])
            max_index=np.argmax(self.contactforce_arrays[arr+1])
            max_values.append([self.contactforce_arrays[arr][max_index],max_value])

        #region SUT
        titles=['SUT_Fixed_30m_15°','SUT_Fixed_30m_25°','SUT_Free_30m_15°','SUT_Free_30m_25°','TST_Fixed_30m_15°','TST_Fixed_30m_25°','TST_Free_30m_15°','TST_Free_30m_25°',]
        
        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot(self.contactforce_arrays[0], self.contactforce_arrays[1],"k-", label= self.legends[0], markersize=3, markevery=15)
        L2 = ax.plot(self.contactforce_arrays[2], self.contactforce_arrays[3],"b--", label= self.legends[1], markersize=3, markevery=15)
        L3 = ax.plot(self.contactforce_arrays[4], self.contactforce_arrays[5],"r-x", label= self.legends[2], markersize=3, markevery=15)
        P1 = ax.plot(max_values[0][0], max_values[0][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        P2 = ax.plot(max_values[1][0], max_values[1][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        P3 = ax.plot(max_values[2][0], max_values[2][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title(titles[0], fontproperties=self.fonts[0])
        ax.set_xlabel('Time (s)', fontproperties=self.fonts[1])
        ax.set_ylabel('Contact Force (kN)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(0,0.5)
        ax.set_ylim(ymin=0)
        pic1 = get_sample_data(dirName1+"\SUT_Fixed_30_15_3100.PNG", asfileobj=False)
        arr_img1 = plt.imread(pic1, format='png')
        imagebox1 = OffsetImage(arr_img1, zoom=0.115)
        imagebox1.image.axes = ax  
        
        pic2 = get_sample_data(dirName1+"\SUT_Fixed_30_15_3600.PNG", asfileobj=False)
        arr_img2 = plt.imread(pic2, format='png')
        imagebox2 = OffsetImage(arr_img2, zoom=0.115)
        imagebox2.image.axes = ax 

        pic3 = get_sample_data(dirName1+"\SUT_Fixed_30_15_4100.PNG", asfileobj=False)
        arr_img3 = plt.imread(pic3, format='png')
        imagebox3 = OffsetImage(arr_img3, zoom=0.115)
        imagebox3.image.axes = ax 

        box1 = AnnotationBbox(imagebox1, (max_values[0][0], max_values[0][1]), xybox=(0.13, max_values[0][1]+1000), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        box2 = AnnotationBbox(imagebox2, (max_values[1][0], max_values[1][1]), xybox=(0.13, max_values[1][1]), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        box3 = AnnotationBbox(imagebox3, (max_values[2][0], max_values[2][1]), xybox=(0.27, max_values[2][1]-1000), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        ax.add_artist(box1)
        ax.add_artist(box2)
        ax.add_artist(box3)
        plt.savefig(self.dirName+'/CF_'+titles[0]+'.png', dpi=1080)
        plt.show()
        plt.clf()

        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot(self.contactforce_arrays[6], self.contactforce_arrays[7],"k-", label= self.legends[0], markersize=3, markevery=15)
        L2 = ax.plot(self.contactforce_arrays[8], self.contactforce_arrays[9],"b--", label= self.legends[1], markersize=3, markevery=15)
        L3 = ax.plot(self.contactforce_arrays[10], self.contactforce_arrays[11],"r-x", label= self.legends[2], markersize=3, markevery=15)
        P1 = ax.plot(max_values[3][0], max_values[3][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        P2 = ax.plot(max_values[4][0], max_values[4][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        P3 = ax.plot(max_values[5][0], max_values[5][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title(titles[1], fontproperties=self.fonts[0])
        ax.set_xlabel('Time (s)', fontproperties=self.fonts[1])
        ax.set_ylabel('Contact Force (kN)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(0,0.5)
        ax.set_ylim(ymin=0)
        pic1 = get_sample_data(dirName1+"\SUT_Fixed_30_25_3100.PNG", asfileobj=False)
        arr_img1 = plt.imread(pic1, format='png')
        imagebox1 = OffsetImage(arr_img1, zoom=0.115)
        imagebox1.image.axes = ax  
        
        pic2 = get_sample_data(dirName1+"\SUT_Fixed_30_25_3600.PNG", asfileobj=False)
        arr_img2 = plt.imread(pic2, format='png')
        imagebox2 = OffsetImage(arr_img2, zoom=0.115)
        imagebox2.image.axes = ax 

        pic3 = get_sample_data(dirName1+"\SUT_Fixed_30_25_4100.PNG", asfileobj=False)
        arr_img3 = plt.imread(pic3, format='png')
        imagebox3 = OffsetImage(arr_img3, zoom=0.115)
        imagebox3.image.axes = ax 

        box1 = AnnotationBbox(imagebox1, (max_values[3][0], max_values[3][1]), xybox=(0.07, max_values[3][1]-1000), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        box2 = AnnotationBbox(imagebox2, (max_values[4][0], max_values[4][1]), xybox=(0.13, max_values[4][1]-2500), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        box3 = AnnotationBbox(imagebox3, (max_values[5][0], max_values[5][1]), xybox=(0.3, max_values[5][1]-1000), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        ax.add_artist(box1)
        ax.add_artist(box2)
        ax.add_artist(box3)
        plt.savefig(self.dirName+'/CF_'+titles[1]+'.png', dpi=1080)
        plt.show()
        plt.clf()

        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot(self.contactforce_arrays[12], self.contactforce_arrays[13],"k-", label= self.legends[0], markersize=3, markevery=15)
        L2 = ax.plot(self.contactforce_arrays[14], self.contactforce_arrays[15],"b--", label= self.legends[1], markersize=3, markevery=15)
        L3 = ax.plot(self.contactforce_arrays[16], self.contactforce_arrays[17],"r-x", label= self.legends[2], markersize=3, markevery=15)
        P1 = ax.plot(max_values[6][0], max_values[6][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        P2 = ax.plot(max_values[7][0], max_values[7][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        P3 = ax.plot(max_values[8][0], max_values[8][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title(titles[2], fontproperties=self.fonts[0])
        ax.set_xlabel('Time (s)', fontproperties=self.fonts[1])
        ax.set_ylabel('Contact Force (kN)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(0,0.5)
        ax.set_ylim(ymin=0)
        pic1 = get_sample_data(dirName1+"\SUT_Free_30_15_3100.PNG", asfileobj=False)
        arr_img1 = plt.imread(pic1, format='png')
        imagebox1 = OffsetImage(arr_img1, zoom=0.115)
        imagebox1.image.axes = ax  
        
        pic2 = get_sample_data(dirName1+"\SUT_Free_30_15_3600.PNG", asfileobj=False)
        arr_img2 = plt.imread(pic2, format='png')
        imagebox2 = OffsetImage(arr_img2, zoom=0.115)
        imagebox2.image.axes = ax 

        pic3 = get_sample_data(dirName1+"\SUT_Free_30_15_4100.PNG", asfileobj=False)
        arr_img3 = plt.imread(pic3, format='png')
        imagebox3 = OffsetImage(arr_img3, zoom=0.115)
        imagebox3.image.axes = ax 

        box1 = AnnotationBbox(imagebox1, (max_values[6][0], max_values[6][1]), xybox=(0.13, max_values[6][1]+1000), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        box2 = AnnotationBbox(imagebox2, (max_values[7][0], max_values[7][1]), xybox=(0.13, max_values[7][1]), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        box3 = AnnotationBbox(imagebox3, (max_values[8][0], max_values[8][1]), xybox=(0.3, max_values[8][1]-1000), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        ax.add_artist(box1)
        ax.add_artist(box2)
        ax.add_artist(box3)
        plt.savefig(self.dirName+'/CF_'+titles[2]+'.png', dpi=1080)
        plt.show()
        plt.clf()

        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot(self.contactforce_arrays[18], self.contactforce_arrays[19],"k-", label= self.legends[0], markersize=3, markevery=15)
        L2 = ax.plot(self.contactforce_arrays[20], self.contactforce_arrays[21],"b--", label= self.legends[1], markersize=3, markevery=15)
        L3 = ax.plot(self.contactforce_arrays[22], self.contactforce_arrays[23],"r-x", label= self.legends[2], markersize=3, markevery=15)
        P1 = ax.plot(max_values[9][0], max_values[9][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        P2 = ax.plot(max_values[10][0], max_values[10][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        P3 = ax.plot(max_values[11][0], max_values[11][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title(titles[3], fontproperties=self.fonts[0])
        ax.set_xlabel('Time (s)', fontproperties=self.fonts[1])
        ax.set_ylabel('Contact Force (kN)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(0,0.5)
        ax.set_ylim(ymin=0)
        pic1 = get_sample_data(dirName1+"\SUT_Free_30_25_3100.PNG", asfileobj=False)
        arr_img1 = plt.imread(pic1, format='png')
        imagebox1 = OffsetImage(arr_img1, zoom=0.115)
        imagebox1.image.axes = ax  
        
        pic2 = get_sample_data(dirName1+"\SUT_Free_30_25_3600.PNG", asfileobj=False)
        arr_img2 = plt.imread(pic2, format='png')
        imagebox2 = OffsetImage(arr_img2, zoom=0.115)
        imagebox2.image.axes = ax 

        pic3 = get_sample_data(dirName1+"\SUT_Free_30_25_4100.PNG", asfileobj=False)
        arr_img3 = plt.imread(pic3, format='png')
        imagebox3 = OffsetImage(arr_img3, zoom=0.115)
        imagebox3.image.axes = ax 

        box1 = AnnotationBbox(imagebox1, (max_values[9][0], max_values[9][1]), xybox=(0.06, max_values[9][1]-1500), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        box2 = AnnotationBbox(imagebox2, (max_values[10][0], max_values[10][1]), xybox=(0.12, max_values[10][1]-3300), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        box3 = AnnotationBbox(imagebox3, (max_values[11][0], max_values[11][1]), xybox=(0.29, max_values[11][1]-1500), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        ax.add_artist(box1)
        ax.add_artist(box2)
        ax.add_artist(box3)
        plt.savefig(self.dirName+'/CF_'+titles[3]+'.png', dpi=1080)
        plt.show()
        plt.clf()
        #endregion

        #region TST       
        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot(self.contactforce_arrays[24], self.contactforce_arrays[25],"k-", label= self.legends[0], markersize=3, markevery=15)
        L2 = ax.plot(self.contactforce_arrays[26], self.contactforce_arrays[27],"b--", label= self.legends[1], markersize=3, markevery=15)
        L3 = ax.plot(self.contactforce_arrays[28], self.contactforce_arrays[29],"r-x", label= self.legends[2], markersize=3, markevery=15)
        P1 = ax.plot(max_values[12][0], max_values[12][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        P2 = ax.plot(max_values[13][0], max_values[13][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        P3 = ax.plot(max_values[14][0], max_values[14][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title(titles[4], fontproperties=self.fonts[0])
        ax.set_xlabel('Time (s)', fontproperties=self.fonts[1])
        ax.set_ylabel('Contact Force (kN)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(0.3,1.3)
        ax.set_ylim(ymin=0)
        pic1 = get_sample_data(dirName1+"\TST_Fixed_30_15_3100.PNG", asfileobj=False)
        arr_img1 = plt.imread(pic1, format='png')
        imagebox1 = OffsetImage(arr_img1, zoom=0.09)
        imagebox1.image.axes = ax  
        
        pic2 = get_sample_data(dirName1+"\TST_Fixed_30_15_3600.PNG", asfileobj=False)
        arr_img2 = plt.imread(pic2, format='png')
        imagebox2 = OffsetImage(arr_img2, zoom=0.09)
        imagebox2.image.axes = ax 

        pic3 = get_sample_data(dirName1+"\TST_Fixed_30_15_4100.PNG", asfileobj=False)
        arr_img3 = plt.imread(pic3, format='png')
        imagebox3 = OffsetImage(arr_img3, zoom=0.09)
        imagebox3.image.axes = ax 

        box1 = AnnotationBbox(imagebox1, (max_values[12][0], max_values[12][1]), xybox=(0.41, max_values[12][1]-1000), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        box2 = AnnotationBbox(imagebox2, (max_values[13][0], max_values[13][1]), xybox=(0.90, max_values[13][1]-800), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        box3 = AnnotationBbox(imagebox3, (max_values[14][0], max_values[14][1]), xybox=(0.72, max_values[14][1]-1500), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        ax.add_artist(box1)
        ax.add_artist(box2)
        ax.add_artist(box3)
        plt.savefig(self.dirName+'/CF_'+titles[4]+'.png', dpi=1080)
        plt.show()
        plt.clf()

        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot(self.contactforce_arrays[30], self.contactforce_arrays[31],"k-", label= self.legends[0], markersize=3, markevery=15)
        L2 = ax.plot(self.contactforce_arrays[32], self.contactforce_arrays[33],"b--", label= self.legends[1], markersize=3, markevery=15)
        L3 = ax.plot(self.contactforce_arrays[34], self.contactforce_arrays[35],"r-x", label= self.legends[2], markersize=3, markevery=15)
        P1 = ax.plot(max_values[15][0], max_values[15][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        P2 = ax.plot(max_values[16][0], max_values[16][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        P3 = ax.plot(max_values[17][0], max_values[17][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title(titles[5], fontproperties=self.fonts[0])
        ax.set_xlabel('Time (s)', fontproperties=self.fonts[1])
        ax.set_ylabel('Contact Force (kN)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(0.3,1.3)
        ax.set_ylim(ymin=0)
        pic1 = get_sample_data(dirName1+"\TST_Fixed_30_25_3100.PNG", asfileobj=False)
        arr_img1 = plt.imread(pic1, format='png')
        imagebox1 = OffsetImage(arr_img1, zoom=0.09)
        imagebox1.image.axes = ax  
        
        pic2 = get_sample_data(dirName1+"\TST_Fixed_30_25_3600.PNG", asfileobj=False)
        arr_img2 = plt.imread(pic2, format='png')
        imagebox2 = OffsetImage(arr_img2, zoom=0.09)
        imagebox2.image.axes = ax 

        pic3 = get_sample_data(dirName1+"\TST_Fixed_30_25_4100.PNG", asfileobj=False)
        arr_img3 = plt.imread(pic3, format='png')
        imagebox3 = OffsetImage(arr_img3, zoom=0.09)
        imagebox3.image.axes = ax 

        box1 = AnnotationBbox(imagebox1, (max_values[15][0], max_values[15][1]), xybox=(0.41, max_values[15][1]-1000), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        box2 = AnnotationBbox(imagebox2, (max_values[16][0], max_values[16][1]), xybox=(0.85, max_values[16][1]-2700), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        box3 = AnnotationBbox(imagebox3, (max_values[17][0], max_values[17][1]), xybox=(0.72, max_values[17][1]-1000), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        ax.add_artist(box1)
        ax.add_artist(box2)
        ax.add_artist(box3)
        plt.savefig(self.dirName+'/CF_'+titles[5]+'.png', dpi=1080)
        plt.show()
        plt.clf()

        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot(self.contactforce_arrays[36], self.contactforce_arrays[37],"k-", label= self.legends[0], markersize=3, markevery=15)
        L2 = ax.plot(self.contactforce_arrays[38], self.contactforce_arrays[39],"b--", label= self.legends[1], markersize=3, markevery=15)
        L3 = ax.plot(self.contactforce_arrays[40], self.contactforce_arrays[41],"r-x", label= self.legends[2], markersize=3, markevery=15)
        P1 = ax.plot(max_values[18][0], max_values[18][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        P2 = ax.plot(max_values[19][0], max_values[19][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        P3 = ax.plot(max_values[20][0], max_values[20][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title(titles[6], fontproperties=self.fonts[0])
        ax.set_xlabel('Time (s)', fontproperties=self.fonts[1])
        ax.set_ylabel('Contact Force (kN)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(0.3,1.3)
        ax.set_ylim(ymin=0)
        pic1 = get_sample_data(dirName1+"\TST_Free_30_15_3100.PNG", asfileobj=False)
        arr_img1 = plt.imread(pic1, format='png')
        imagebox1 = OffsetImage(arr_img1, zoom=0.08)
        imagebox1.image.axes = ax  
        
        pic2 = get_sample_data(dirName1+"\TST_Free_30_15_3600.PNG", asfileobj=False)
        arr_img2 = plt.imread(pic2, format='png')
        imagebox2 = OffsetImage(arr_img2, zoom=0.08)
        imagebox2.image.axes = ax 

        pic3 = get_sample_data(dirName1+"\TST_Free_30_15_4100.PNG", asfileobj=False)
        arr_img3 = plt.imread(pic3, format='png')
        imagebox3 = OffsetImage(arr_img3, zoom=0.1)
        imagebox3.image.axes = ax 

        box1 = AnnotationBbox(imagebox1, (max_values[18][0], max_values[18][1]), xybox=(0.42, max_values[18][1]-800), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        box2 = AnnotationBbox(imagebox2, (max_values[19][0], max_values[19][1]), xybox=(0.82, max_values[19][1]-1700), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        box3 = AnnotationBbox(imagebox3, (max_values[20][0], max_values[20][1]), xybox=(0.70, max_values[20][1]-800), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        ax.add_artist(box1)
        ax.add_artist(box2)
        ax.add_artist(box3)
        plt.savefig(self.dirName+'/CF_'+titles[6]+'.png', dpi=1080)
        plt.show()
        plt.clf()

        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot(self.contactforce_arrays[42], self.contactforce_arrays[43],"k-", label= self.legends[0], markersize=3, markevery=15)
        L2 = ax.plot(self.contactforce_arrays[44], self.contactforce_arrays[45],"b--", label= self.legends[1], markersize=3, markevery=15)
        L3 = ax.plot(self.contactforce_arrays[46], self.contactforce_arrays[47],"r-x", label= self.legends[2], markersize=3, markevery=15)
        P1 = ax.plot(max_values[21][0], max_values[21][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        P2 = ax.plot(max_values[22][0], max_values[22][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        P3 = ax.plot(max_values[23][0], max_values[23][1], marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title(titles[7], fontproperties=self.fonts[0])
        ax.set_xlabel('Time (s)', fontproperties=self.fonts[1])
        ax.set_ylabel('Contact Force (kN)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(0.3,1.3)
        ax.set_ylim(ymin=0)
        pic1 = get_sample_data(dirName1+"\TSt_Free_30_25_3100.PNG", asfileobj=False)
        arr_img1 = plt.imread(pic1, format='png')
        imagebox1 = OffsetImage(arr_img1, zoom=0.09)
        imagebox1.image.axes = ax  
        
        pic2 = get_sample_data(dirName1+"\TST_Free_30_25_3600.PNG", asfileobj=False)
        arr_img2 = plt.imread(pic2, format='png')
        imagebox2 = OffsetImage(arr_img2, zoom=0.09)
        imagebox2.image.axes = ax 

        pic3 = get_sample_data(dirName1+"\TST_Free_30_25_4100.PNG", asfileobj=False)
        arr_img3 = plt.imread(pic3, format='png')
        imagebox3 = OffsetImage(arr_img3, zoom=0.09)
        imagebox3.image.axes = ax 

        box1 = AnnotationBbox(imagebox1, (max_values[21][0], max_values[21][1]), xybox=(0.42, max_values[21][1]-1200), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        box2 = AnnotationBbox(imagebox2, (max_values[22][0], max_values[22][1]), xybox=(0.8, max_values[22][1]), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',facecolor='red'))
        box3 = AnnotationBbox(imagebox3, (max_values[23][0], max_values[23][1]), xybox=(0.45, max_values[23][1]-1300), xycoords='data', boxcoords='data', pad=0.0, arrowprops=dict(arrowstyle='<|-,head_length=0.02, head_width=0.02',connectionstyle="angle,angleA=90,angleB=00,rad=50",facecolor='red'))
        ax.add_artist(box1)
        ax.add_artist(box2)
        ax.add_artist(box3)
        plt.savefig(self.dirName+'/CF_'+titles[7]+'.png', dpi=1080)
        plt.show()
        plt.clf()
        #endregion

    def interactionDiagram(self):
        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot([0,901.2,976.6,1501.1,1501.1],[1238.83,1238.83,1212.59,642.77,0],"k-",  markersize=3, markevery=15)
        P1 = ax.plot(1294.8,2583.13, marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        P2 = ax.plot(2166, 2189.5, marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title('Capacity Interaction Diagram (2000 kN axial DL)', fontproperties=self.fonts[0])
        ax.set_xlabel('Moment (kN.m)', fontproperties=self.fonts[1])
        ax.set_ylabel('Shear force (kN)', fontproperties=self.fonts[1])
        #plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(xmin=0)
        ax.set_ylim(ymin=0)
        
        plt.annotate('a = 0.6 m', xy=(1294.8,2583.13),  xycoords='data', xytext=(1094.8,2183.13), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center')
        plt.annotate('a = 1.5 m', xy=(2166, 2189.5),  xycoords='data', xytext=(1966, 1789.5), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center')
        plt.savefig(self.dirName+'/Interaction.png', dpi=1080)
        plt.show()
        plt.clf()
         
        ##
        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot([0,901.2,976.6,1501.1,1501.1],[1238.83,1238.83,1212.59,642.77,0],"k-",  markersize=3, markevery=15)
        P1 = ax.plot(1488,1767, marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        P2 = ax.plot(611, 613, marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title('Capacity Interaction Diagram (2000 kN axial DL)', fontproperties=self.fonts[0])
        ax.set_xlabel('Moment (kN.m)', fontproperties=self.fonts[1])
        ax.set_ylabel('Shear force (kN)', fontproperties=self.fonts[1])
        #plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(xmin=0)
        ax.set_ylim(ymin=0)
        
        plt.annotate('SUT', xy=(1488,1767),  xycoords='data', xytext=(1388,1567), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center')
        plt.annotate('TST', xy=(611, 613),  xycoords='data', xytext=(511, 413), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center')
        plt.savefig(self.dirName+'/Interaction1.png', dpi=1080)
        plt.show()
        plt.clf()

        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot([0,901.2,976.6,1501.1,1501.1],[1238.83,1238.83,1212.59,642.77,0],"k-",  markersize=3, markevery=15)
        P1 = ax.plot(1617,1817, marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        P2 = ax.plot(2726, 2738, marker="o", markersize=5,markeredgecolor="k", markerfacecolor="red")
        ax.set_title('Capacity Interaction Diagram (2000 kN axial DL)', fontproperties=self.fonts[0])
        ax.set_xlabel('Moment (kN.m)', fontproperties=self.fonts[1])
        ax.set_ylabel('Shear force (kN)', fontproperties=self.fonts[1])
        #plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(xmin=0)
        ax.set_ylim(ymin=0)
        
        plt.annotate('SUT', xy=(1617,1817),  xycoords='data', xytext=(1417,1417), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center')
        plt.annotate('TST', xy=(2726, 2738),  xycoords='data', xytext=(2526, 2338), textcoords='data',fontproperties=self.fonts[1], arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center')
        plt.savefig(self.dirName+'/Interaction2.png', dpi=1080)
        plt.show()
        plt.clf()

    def annotate(self):
        root = Tk()
        root.withdraw()
        dirName1 = filedialog.askdirectory(parent = root, initialdir="\\", title='Select the location of the annotaion figures')
        
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.set_xlim(0,200)

        def trans(image,image1):       
            img = Image.open(image)
            img = img.convert("RGBA")
            datas = img.getdata()
            newData = []
            for item in datas:
                if item[0] == 255 and item[1] == 255 and item[2] == 255:
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)
            img.putdata(newData)
            img.save(image1, "PNG")
        
        arr_img1 = mpimg.imread(dirName1+"/Pier.PNG")
        plt.imshow(arr_img1)
        plt.annotate("1780 kN", xy=(62.5, 250), xytext=(140, 250), arrowprops=dict(facecolor='green', shrink=0.05), horizontalalignment='center', verticalalignment='center',fontproperties=self.fonts[2])
        plt.annotate("", xy=(60, 345), xytext=(125, 345), arrowprops=dict(arrowstyle="-"))
        plt.annotate("", xy=(100, 345), xytext=(100, 250), arrowprops=dict(arrowstyle="<->"))
        t = ax.text(100, 297, "1.2 m", ha="center", va="center", rotation=0, size=10,bbox=dict(boxstyle="round,pad=0.3", fc="w", ec="w", lw=1),fontproperties=self.fonts[2])

        #plt.annotate("", xy=(54, 357.5), xytext=(84, 357.5), arrowprops=dict(arrowstyle="-"))
        #plt.annotate("", xy=(54, 285.3), xytext=(97, 285.3), arrowprops=dict(arrowstyle="-"))
        #plt.annotate("", xy=(75.5, 357.5), xytext=(75.5, 285.3), arrowprops=dict(arrowstyle="<->"))
        #t = ax.text(45.5, 321.4, "1067 mm", ha="center", va="center", rotation=0, size=10,bbox=dict(boxstyle="round,pad=0.3", fc="none", ec="none", lw=1),fontproperties=self.fonts[2])
        plt.axis("off")
        plt.savefig(dirName1+"\PierAnnot400.PNG", dpi=1080)
        plt.show()
        #plt.savefig(dirName1+"\SysAnnot.PNG", dpi=1080)
        #img = trans(dirName1+"\SUT_Fixed_30_15_31001.PNG",dirName1+"\SUT_Fixed_30_15_31001.PNG")

    def pieChart(self):
        root = Tk()
        root.withdraw()
        dirName1 = filedialog.askdirectory(parent = root, initialdir="\\", title='Select the location of the annotaion figures')
        y = np.array([(54971/72356), (16836/72356), (549/72356)])
        mylabels = ["Good", "Fair", "Poor"]
        myexp = [0.2,0.2,0]
        plt.pie(y, labels = mylabels,  autopct='%1.1f%%', radius= 0.8, labeldistance=1.1,textprops=dict(rotation_mode = 'anchor',font=self.fonts[1]),rotatelabels =True, startangle=180,counterclock=False)
        plt.savefig(dirName1+"\PieChartCondition1.PNG", dpi=1080)
        plt.show() 
    
    def Acceleration(self):
        root = Tk()
        root.withdraw()
        dirName = filedialog.askdirectory(parent = root, initialdir="\\", title='Select the location to save the figures')
        dirName1 = filedialog.askopenfile(parent = root, initialdir="\\", title='Select the results file')
        #FIGURES FOR Experimental Acceleration
        Acceleration = pd.read_excel(dirName1.name, sheet_name=2, header=0)
        Accel_header=[]
        Accel_arrays=[]
        counter=0
        for col in Acceleration.columns:
            Accel_header.append(col)
            my_array=np.array(Acceleration[Accel_header[counter]])
            new_array = my_array[np.logical_not(np.isnan(my_array))]
            Accel_arrays.append(new_array)
            counter+=1 
        
        titles=['TL-4 Acceleration Time History','TL-5 Acceleration Time History']
        
        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot(Accel_arrays[0], Accel_arrays[1],"k-", label= "Sheikh et al.", markersize=3)
        L2 = ax.plot(Accel_arrays[2], Accel_arrays[3],"b--", label= "This study", markersize=3, markevery=15)
      
        ax.set_title(titles[0], fontproperties=self.fonts[0])
        ax.set_xlabel('Time (s)', fontproperties=self.fonts[1])
        ax.set_ylabel('Longitudinal acceleration (g)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(0,0.5)
        #ax.set_ylim(ymin=0)
        
        plt.savefig(dirName+'/Accel_'+titles[0]+'.png', dpi=1080)
        plt.show()
        plt.clf()

        fig = plt.figure()
        ax = fig.add_subplot()
        L1 = ax.plot(Accel_arrays[4], Accel_arrays[5],"k-", label= "Miele et al.", markersize=3)
        L2 = ax.plot(Accel_arrays[6], Accel_arrays[7],"b--", label= "This study", markersize=3, markevery=15)
      
        ax.set_title(titles[1], fontproperties=self.fonts[0])
        ax.set_xlabel('Time (s)', fontproperties=self.fonts[1])
        ax.set_ylabel('Longitudinal acceleration (g)', fontproperties=self.fonts[1])
        plt.legend(prop=self.fonts[1])
        plt.xticks(fontproperties=self.fonts[2])
        plt.yticks(fontproperties=self.fonts[2])
        ax.set_xlim(0,1.0)
        ax.set_ylim(ymax=1)
        
        plt.savefig(dirName+'/Accel_'+titles[1]+'.png', dpi=1080)
        plt.show()
        plt.clf()