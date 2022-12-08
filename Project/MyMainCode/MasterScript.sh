#!/bin/bash
#cd /mnt/c/Users/Chenr/source/repos/625FinalProject/project/MyMainCode

#The following lines replace the Parameters.py class - the use of the export command exposes the variables defined to all child processes
#This means they are accessible, but if you set them in any of those files, it will be changed in all following processes
export phaseName = "8-Paper1"
#export phaseName = "8-Paper2"
export vehicleType = ("SUT" "TST")
export vehicleModel = ("01F800Truck.k" "0TractorSemi-Trailer.k")
export barrierBoundary = ("Fixed" "Free" "Segmented")
export barrierShape = ("TL3" "TL4" "TL5") #this is only used in phase 2
export angleOfAttack = 15

./ExecutionScript.sh