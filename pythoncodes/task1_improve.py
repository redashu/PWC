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
Press 8 to exit the code : 
'''
# function to calculate str length
def  calstr():
	st=input("Enter any string: ")
	l=len(st)
	print("Length or String",l)

# function for running linux command 

def  runlinux():
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


while 5 > 3:

	print(data)

	# taking input from user 
	user_data=input() 
	# input function always accept in str format 
	print("User given ",user_data)

	# running options 
	if  user_data  ==  '1' :
		# calling calstr function 
		calstr()
	elif  user_data ==   '2'  :
		mytime=time.ctime()
		print("Current time is ",mytime)
	elif  user_data ==   '5'  :
		# calling runlinux function 
		runlinux()
	elif user_data ==  '8' :
		exit() # code finish 
	else :
		print("Wrong Input values ..")




