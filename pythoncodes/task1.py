#!/usr/bin/python3

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
	print("Ok good to GO...")

else :
	print("Wrong Input values ..")
