#!/bin/bash
#/mnt/c/Users/Chenr/source/repos/625FinalProject/project/mymaincode

#We make VERSION an environemnt variable
#This means it can be accessed and ALTERED anywhere - be careful when altering
VERSION=15
export VERSION
temp="./625Test.sh"
#This evals with or without the brackets
${temp}