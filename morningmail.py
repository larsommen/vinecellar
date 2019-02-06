#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import get_user_data
import sys
import commands
import bme280
from email.mime.text import MIMEText #to be used to create mail opbject
from subprocess import Popen, PIPE #to send email via gmail

try:
	# read data from bme280
	temperature,pressure,humidity = bme280.readBME280All()

#on failure - send error-message-mail
except Exception as ex:
	error = str(ex)
	subprocess.call(['python', 'systemalertmail.py', error])


setup = get_user_data.getall()

#set date to current date
date = commands.getoutput("date")


alert = ''
body = '<table>'

body += '<tr>'

greating = "<b>Godmorgen " + setup.get('customer_name') + "</b>"


body += "<td>" + greating + "</td>" + "<td></td> </tr><tr>"

body += "<td></td><td></td></tr><tr>"

if (temperature > float(setup.get('temp_limit'))):
	body += "<td>Temperaturen er </td><td><font color = 'red'>" + str(round(temperature,2)) + chr(176) +  "C  </font></td>"	
	alert += '<b>OBS temperatur!!!</b>'
else:
	body += "<td>Temperaturen er </td><td><font color = 'blue'>" + str(round(temperature,2)) + chr(176) +  "C  </font></td>" 

body += '</tr><tr>'

if (humidity > float(setup.get('humit_limit'))):
	body += "<td>Luftfugtigheden er </td><td><font color = 'red'>" +  str(round(humidity,1)) + "%</font></td>"
	alert += "<b> OBS Luftfugtighed!!!</b>"
else:
	body += "<td>Luftfugtigheden er </td><td><font color = 'darkgreen'>" +  str(round(humidity,1)) + "%</font></td>"

body += '</tr><tr>'
body += '<td>'

if (temperature <= float(setup.get('temp_limit')) and humidity <= float(setup.get('humit_limit'))):
	alert += "<b>Alt er fint</b></td>"

body += "<td></td><td></td></tr><tr>"

#body += alert

body += '</td><td></tr></table></br></br>'

body += alert

msg = MIMEText(body, 'html')
msg["From"] = setup.get('from_address')
msg["To"] = setup.get('customer_mail')
msg["Bcc"] = setup.get('bcc')
msg["Subject"] = "Godmorgen fra din vinkælder." + " " + date
p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE, universal_newlines=True)
p.communicate(msg.as_string())
