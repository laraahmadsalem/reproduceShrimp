#                                                                               
# Author : Lara Ahmad Salem                                                     
# ID : 19491787                                                                 
#                                                                               
# shrimp_sweep.sh - Bash Script that simulates a different                   
#                                                                               
# Reference: Retrieved from Topic 8 (Scripts and Automation) Practical 6, 
#             
#            Date: October 28 2019                                                               # Revisions: 
# 28/10/2019 - modifications to practical 6 worksheet, added 3 for loops 
#              and changed variables                                                                                  
#!/bin/bash 

shrimp_dir=shrimp`date "+%Y-%m-%d_%H:%M:%S"`

mkdir $shrimp_dir 
cp shrimpSimBase.py $shrimp_dir 
cp shrimp_sweep.sh $shrimp_dir
cp shrimp.py $shrimp_dir
cp check.py $shrimp_dir
cp userInput.py $shrimp_dir 
cp fileIO.py $shrimp_dir 
 
cd $shrimp_dir 


low_y=$1 
hi_y=$2 
step_y=$3 
low_x=$4
hi_x=$5 
step_x=$6
low_pop=$7 
hi_pop=$8
step_pop=$9


echo "Y Coordinates " $low_y $hi_y $step_y 
echo "X coordinates " $low_x $hi_x $step_x  
echo "Population of Shrimps:" $low_pop $hi_pop $step_pop   



for y in `seq $low_y $step_y $hi_y`; 
do  
    for x in `seq $low_x $step_x $hi_x`; 
    do 
        for p in `seq $low_pop $step_pop $hi_pop`;
        do 
            echo "Experiment: ${y} ${x} ${p}" 
            outfile="Y_value:_${y}X_value:_${x}Pop_value:_${p}.txt"
            python3 shrimpSimBase.py $y $x $p 20 > $outfile 
            echo 1
        done 
    done
done  
