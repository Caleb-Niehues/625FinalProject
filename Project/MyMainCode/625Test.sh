#!/bin/bash
#filePath = "/home/salahatf/LS-DYNA/8-Paper1/SUT/Fixed/15.1/SUT_" - this passes as a command
#filePath=`/home/salahatf/LS-DYNA/8-Paper1/SUT/Fixed/15.1/SUT_` - this passes as a filepath
filePath='/home/salahatf/LS-DYNA/8-Paper1/SUT/Fixed/15.1/SUT_' # - this passes as a string
#commandPath="/home/ls-dyna/bin/ls-dyna_smp_s_r1010_x64_redhat5_ifort160"
fakeCommPath='/home/ls-dyna/bin/ls-dyna_smp_s_r1010_x64_redhat5_ifort160'
#echo "/home/salahatf/LS-DYNA/8-Paper1/SUT/Fixed/15.1/SUT_Fixed_${VERSION}.k"
echo "${fakeCommPath} ${filePath}Fixed_${VERSION}.k"