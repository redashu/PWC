#!/bin/bash

<<EOF
echo "Enter any data : "
read  x;

sleep 2
echo "User given $x "
EOF

# EOF -- end of file 


echo "Hey current date and time  is  ... `date` "

sleep 2
echo "accepting inline inputs "
sleep 1
# another method of taking input -- inline input 

echo  $1  # first argument after file name 
sleep 1
echo $2 
sleep 1

echo $@ # all the arguments 

sleep 1
echo $# # to calculate number of arguments 
