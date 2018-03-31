#!/bin/bash
#cd
#cd Documents
#test -d no66 || mkdir no66
#cd no66
#ls
#utilcode_path='../../Desktop/MakeNTU/make_ntu_no_66-master'
python3 iot_download.py

cd download
#For the first time, filname.txt exists and content = initial
#head --lines=1 ../filename_new.txt > ../filename_old.txt
ls -c1 > ../filename_new.txt
cd ..

#servermain input?
python3 servermain.py
#while [ 1==1 ]; do
#    echo $SECONDS
#    end=$((SECONDS+3))
#    while [ $SECONDS -lt $end ]; do
#        :
#    done
#    :
#done

