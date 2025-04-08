#!/bin/bash

dir=$1
#temp=/store/user/carbour/mc/alp/mUFO/m30/CRAB_PrivateMC/mUFO_ALP_m30_step1/241015_185744/0000/mUFO_ALP_m30_GEN-SIM

x=$2
n=$3

while [ $x -le $n ]
do
    echo "--------------------------------------------------"
    echo "invalidating file_ "$x".txt"

    echo crab-dev setfilestatus --dbs-instance prod/phys03 -f "$dir"_$x.root -s INVALID
    echo ===

    crab-dev setfilestatus --dbs-instance prod/phys03 -f "$dir"_$x.root -s INVALID

    x=$(($x + 1))
done


