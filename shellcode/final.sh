#!/bin/bash

echo "Press 1 to check your current OS name : "
echo "Press 2 to check your kernel and kernel version  : "
echo "Press 3 to RAM amount in your OS  : "
echo "Press 4 to Install Java - icluding jdk8 and JRE env  : "
echo "Press 5 to create 5 files in your current user Desktop  Folder : "
echo "Press 6 to remove all .txt files from current user Desktop folder : "
echo "Press 7 to sample java code  : "

read user_input;

if  [  $user_input -eq 1  ]
then
	
	echo  "My current OS name and info is : "
	sleep 1 
	hostnamectl |   grep -i system 

elif  [  $user_input -eq 2  ]
then
	echo "kernel Name is  : `uname`"
	sleep 1
	echo "Kernel Version is : `uname -r`"


else 

	echo  "YOU have to choose the Right Number "
	sleep 1
	echo "Read the message carefully and re run the code "

fi 

