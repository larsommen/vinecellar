#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import get_user_data
import sys
import commands
import subprocess
from subprocess import check_output
import bme280
from email.mime.text import MIMEText #to be used to create mail opbject
from subprocess import Popen, PIPE #to send email via gmail
import formatInput

setup = get_user_data.getall()

try:
	# read data from bme280
	temperature,pressure,humidity = bme280.readBME280All()
	temperature = temperature - float(setup.get('setoff_temp'))
	humidity = humidity * float(setup.get('setoff_hum'))
#on failure - send error-message-mail
except Exception as ex:
	error = str(ex)
	subprocess.call(['python', 'systemalertmail.py', error])


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

if (temperature <= float(setup.get('temp_limit')) and humidity <= float(setup.get('humit_limit'))):
	body += "<td>Alt er fint</td>"


body += alert

body += '</td><td></tr></table></br></br>'

ipaddress = commands.getoutput("hostname -I")

uptimeis = commands.getoutput("uptime")

body += ipaddress

body += "</br>"

body += uptimeis + "</br>"

body += "</br> Indhold i foldere: </br></br>"

contence = check_output(['ls', '-alg', '/home/pi/winecellar'])


contence = formatInput.doTable(contence) 

body += "winecellar: </br>" + contence + "</br></br>"

contence = check_output(['ls', '-alg', '/home/pi/winecellar/img'])

contence = formatInput.doTable(contence)

body += "img: </br>" + contence + "</br></br>"

contence = check_output(['ls', '-alg', '/home/pi/winecellar/tmpdata'])

contence = formatInput.doTable(contence)

body += "tmpdata: </br>" + contence + "</br></br>"

contence = check_output(['df'])

contence = formatInput.doTable(contence)

body += "Diskspace: </br>" + contence + "</br></br>" + '<object align="right">' + setup.get('id') + '</object>'


msg = MIMEText(body, 'html')
msg["From"] = setup.get('from_address')
msg["To"] = setup.get('customer_mail')
msg["Bcc"] = setup.get('bcc')
customername = setup.get('customer_name')

subject = "Status fra " + customername + "'s " + setup.get('short_title')+ ". " + date
msg["Subject"] = subject
p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE, universal_newlines=True)
p.communicate(msg.as_string())
