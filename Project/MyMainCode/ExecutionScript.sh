#!/bin/bash
#commandPath="/home/ls-dyna/bin/ls-dyna_smp_s_r1010_x64_redhat5_ifort160"
fakeCommPath='/home/ls-dyna/bin/ls-dyna_smp_s_r1010_x64_redhat5_ifort160'

#does the # on 15.X always the # 8-PaperX 
NeedToAskHowHeWantsThisSplit="8-Paper1"
InputStart='/home/salahatf/LS-DYNA/'${NeedToAskHowHeWantsThisSplit}
subversion=1 #Might need declared alongside VERSION

for TYPE in "Fixed" "Free" "Segmented"
do
    echo "${fakeCommPath} I=\"${InputStart}/SUT/${TYPE}/${VERSION}.${subversion}/SUT_${TYPE}_${VERSION}.k\" NCPU=-8 MEMORY=200000000 jobid=SUT_${TYPE}_${VERSION} &"
    #The code below should theoretically work, not 100%
    #${commandPath} I=${InputStart}${InputFixed} NCPU=-8 MEMORY=200000000 jobid=SUT_fixed_15 &
done