#!/bin/bash


for((i=1;i<5;i++))
do
	echo hello world
	sleep 1
done

# method 2 

for  i  in  `seq 5`
do
	echo  "Hello Centos"
	sleep 1
done


# method 3

for i  in  `seq $1`
do
	echo  "my name is  `whoami`"
	sleep 1

done

# method 4 
for i in  date  cal whoami pwd  
do
	echo "plz wait we are running commnad : $i"
	sleep 1
	$i 

done
