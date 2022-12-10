#!/bin/bash
#This script creates the directories that will contain the simulation matrices

#he uses tkinter to grab a specific file path
#This might be useful - probably not if he needs another install
#https://help.gnome.org/users/zenity/stable/file-selection.html.en

#He has created a parameters object, and then uses the paper1/2 call to set fields
source Parameters.sh

for Type in "${vehicleType[@]}"
do
    for Barrier in "${barrierBoundary[@]}"
    do
        for Angle in $(seq 1 $anglesOfAttack)
        do
            mkdir -p $parentPath/$Type/$Barrier/$Angle
        done
    done
done