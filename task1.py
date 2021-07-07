#!/usr/bin/python3

import time,sys
import  subprocess

data='''
Press 1 to check lengh of given string :
Press 2 to current date and time  :
Press 3 to open default web browser in current OS :
Press 4 to search something on Google : 
Press 5 to run any linux command given by user :
Press 6 to Directory IN current user Desktop  : 
Press 7 to reboot your system  :
'''
print(data)

# taking input from user 
user_data=input() 
# input function always accept in str format 
print("User given ",user_data)
#print("User given "+user_data)

if  user_data  ==  '1' :
	st=input("Enter any string: ")
	l=len(st)
	print("String length is ",l)
elif  user_data ==   '2'  :
	mytime=time.ctime()
	print("Current time is ",mytime)
elif  user_data ==   '5'  :
	# taking input 
	cmd=input("enter any linux command : ")
	if sys.platform ==  'linux' :
		print("plz wait we are running command ..")
		time.sleep(1)
		output=subprocess.getoutput(cmd)
		print(output)
	else : 
		print("ONly linux command is gonna support ")
		time.sleep(2)
		print("current platform is ",sys.platform)


else :
	print("Wrong Input values ..")
