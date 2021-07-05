#!/bin/bash

echo  "enter any command : "

read x

if [  "$x" ==  "date" ]
then

	echo  "MY current time is , `date`"

else  

	echo  "Sorry i don't know what is this command .."


fi
