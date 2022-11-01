#region ENVIRONMENT SETTING
import os
from tkinter import *
from tkinter import filedialog
from Parameters import Parameters
#endregion

class Directories(object):
    """This class creates the directories that will contain the simulation matrices"""
    def __init__(self):
        root = Tk()
        root.withdraw()
        self.parentPath = filedialog.askdirectory(parent = root, initialdir="/", title='Select the parent path for the created directories')
        self.parameters = Parameters()

    def mkdir (self,name,path):

        finalPath = os.path.join(path,name)
        os.mkdir(finalPath)
        return (finalPath)
    
    def createDirectories(self,purpose):
        if purpose ==1:
            self.parameters.paper1()
        else:
            self.parameters.paper2()
        dir = self.mkdir(self.parameters.phaseName[0],self.parentPath)
        for i in range (len(self.parameters.vehicleType)):
            dir1 = self.mkdir(self.parameters.vehicleType[i], dir)
            for j in range (len(self.parameters.barrierBoundary)):
                dir2 = self.mkdir(self.parameters.barrierBoundary[j],dir1)
                for k in range (len(self.parameters.anglesOfAttack)):
                    dir3 = self.mkdir(str(self.parameters.anglesOfAttack[k]),dir2)
                        
