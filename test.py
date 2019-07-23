#!/usr/local/bin/python
# -*- coding: utf-8 -*-


import bme280
import get_user_data
import os

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
	temperature = temperature - float(setup.get('setoff_temp'))
	humidity = humidity*float(setup.get('setoff_hum'))
#on failure - send error-message-mail
except Exception as ex:
	error = str(ex)
	subprocess.call(['python', '/home/pi/winecellar/systemalertmail.py', error])

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


try:
	todayTempDataFile = open("/home/pi/winecellar/tmpdata/today.temp", "a+")
	todayTempDataFile.write(str(temperature) + "\n")
	todayTempDataFile.close()

	todayHumidDataFile = open("/home/pi/winecellar/tmpdata/today.humid", "a+")
	todayHumidDataFile.write(str(humidity) + "\n")
	todayHumidDataFile.close()

except Exception as ex:
        error = str(ex)
        subprocess.call(['python', '/home/pi/winecellar/systemalertmail.py', error])


existsTempError = os.path.isfile('/home/pi/winecellar/tmpdata/errorTemp.test')
existsHumidError = os.path.isfile('/home/pi/winecellar/tmpdata/errorHumid.test')

# test if limits are compromised - send mail
if not existsTempError and temperature > int(setup.get('temp_limit')):
	subprocess.call(['python', "/home/pi/winecellar/getLatestTempData.py"])
	subprocess.call(['python', "/home/pi/winecellar/alarmTemp.py", str(temperature), str(humidity)])
	subprocess.call(['touch', "/home/pi/winecellar/tmpdata/errorTemp.test"])


if not existsHumidError and  humidity > int(setup.get('humit_limit')):
	subprocess.call(['python', "/home/pi/winecellar/getLatestHumidData.py"]) 
	subprocess.call(['python', "/home/pi/winecellar/alarmHumid.py", str(temperature), str(humidity)])
	subprocess.call(['touch', "/home/pi/winecellar/tmpdata/errorHumid.test"])
