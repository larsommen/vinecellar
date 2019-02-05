# created for importing userdata from file to dictionary

import re

def getall():
	userdata = dict() 
	with open("/home/pi/config.txt", "r") as lines:
		for line in lines:
			line = line[:len(line)-1]	
			newpost = re.split(":", line)
			userdata.update({newpost[0]:newpost[1]})
	return userdata;

