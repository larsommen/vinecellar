#!/usr/local/bin/python
# -*- coding: utf-8 -*-


import bme280
import get_user_data


#all imports
import commands
import subprocess
from datetime import *

#get week number
today = datetime.today()
weeknumber = datetime.utcnow().isocalendar()[1]

#set name on log file
logfilename = "/home/pi/logs/" + str(weeknumber) + ".log"


#set date to current date
date = commands.getoutput("date")

setup = get_user_data.getall()

try:
	# read data from bme280
	temperature,pressure,humidity = bme280.readBME280All()

#on failure - send error-message-mail
except Exception as ex:
	error = str(ex)
	subprocess.call(['python', 'systemalertmail.py', error])

#log data
logentry = str(temperature) + "," + str(pressure) + "," + str(humidity) + "," + str(date) + "\n"

try:
	logfile = open(logfilename, "a+")
	logfile.write(logentry)
	logfile.close()

#on failure - send error-message-mail
except Exception as ex:
        error = str(ex)
        subprocess.call(['python', '/home/pi/winecellar/systemalertmail.py', error])


# test if limits are compromised - send mail
if temperature > int(setup.get('temp_limit')) or humidity > int(setup.get('humit_limit')):
	subprocess.call(['python', "/home/pi/winecellar/alarm.py", str(temperature), str(humidity)])
