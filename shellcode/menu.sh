#!/bin/bash

if  [  "$1" ==  "firefox" ]
then
	firefox  www.google.com/search?q=hello


elif  [  "$1" == "date" ]
then
	echo  "current time is  `date` "


elif  [  "$1" ==  "shell" ]

then
	echo  "I am LInux kernel using shell echo $SHELL"


elif  [ $# -eq 0 ]

then
	echo "Plase provide some argument value "

else 
	echo  "I don't know what to do "


fi
