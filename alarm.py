#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import get_user_data
import sys
import commands
from email.mime.text import MIMEText #to be used to create mail opbject
from subprocess import Popen, PIPE #to send email via gmail

temperature = float(sys.argv[1])

humidity = float(sys.argv[2])

setup = get_user_data.getall()

#set date to current date
date = commands.getoutput("date")


alert = ''
body = '<table>'

body += '<tr>'
if (temperature > float(setup.get('temp_limit'))):
	body += "<td>Temperaturen er </td><td><font color = 'red'>" + str(round(temperature,2)) + chr(176) +  "C  </font></td>"	
	alert += 'OBS temperatur!!!'
else:
	body += "<td>Temperaturen er </td><td><font color = 'blue'>" + str(round(temperature,2)) + chr(176) +  "C  </font></td>" 

body += '</tr><tr>'

if (humidity > float(setup.get('humit_limit'))):
	body += "<td>Luftfugtigheden er </td><td><font color = 'red'>" +  str(round(humidity,1)) + "%</font></td>"
	alert += " OBS Luftfugtighed!!!"
else:
	body += "<td>Luftfugtigheden er </td><td><font color = 'darkgreen'>" +  str(round(humidity,1)) + "%</font></td>"

body += '</tr><tr>'
body += '<td>'

body += alert

body += '</td><td></tr></table></br></br>'


msg = MIMEText(body, 'html')
msg["From"] = setup.get('from_address')
msg["To"] = setup.get('customer_mail')
msg["Bcc"] = setup.get('bcc')
msg["Subject"] = "ALARM !!! fra din vinkælder." + " " + date
p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE, universal_newlines=True)
p.communicate(msg.as_string())
