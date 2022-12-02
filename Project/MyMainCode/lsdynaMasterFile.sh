#!/bin/bash
cd /home/salahatf/LS-DYNA/8-Paper1/SUT/Fixed/15
chmod +x SUT_Fixed_15.sh
./SUT_Fixed_15.sh &
cd /home/salahatf/LS-DYNA/8-Paper1/SUT/Free/15
chmod +x SUT_Free_15.sh &
./SUT_Free_15.sh &
cd /home/salahatf/LS-DYNA/8-Paper1/SUT/Segmented/15
chmod +x SUT_Segmented_15.sh
./SUT_Segmented_15.sh
#He navigates to the file
#Makes it executable through bash
#Executes it