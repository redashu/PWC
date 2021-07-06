#!/bin/bash

# creating a variable 

n=10

while [  $n -gt 0  ]
do
	echo "Hey Guys this is while loop .. "
	sleep 2
	echo "My os name is : `cat /etc/os-release` "
	sleep 2
	echo "______________________________________"
	echo  "@@@@@@@@@@@@@@@@@@@@@@@@+++++++++++++"
	sleep 3
done
