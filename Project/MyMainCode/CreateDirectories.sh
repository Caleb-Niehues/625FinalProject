#!/bin/bash
#This script creates the directories that will contain the simulation matrices

#he uses tkinter to grab a specific file path
#This might be useful - probably not if he needs another install
#https://help.gnome.org/users/zenity/stable/file-selection.html.en

#He has created a parameters object, and then uses the paper1/2 call to set fields

mkdir $parentPath
for TYPE in $vehicleType
do
    #mkdir
    for X in $barrierBoundary
    do
        #mkdir 
        #not sure how he wants this last round - I don't believe 0 is possible
        for Z in {1..$anglesOfAttack} #does he want this run just once or as is?
        do
            echo ${Z}
            #mkdir
        done
    done
done