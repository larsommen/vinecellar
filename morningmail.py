#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

import get_user_data
import calculateData
import mvfileweekday
import sys
import commands
import bme280
import datetime
from email.mime.text import MIMEText #to be used to create mail object
from subprocess import Popen, PIPE #to send email via gmail
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
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

# get last 24 hours average, minimum and maximum tempreture
avgtemp, mintemp, maxtemp = calculateData.getStats('/home/pi/winecellar/tmpdata/today.temp')

# get last 24 hours average, minimum and maximum humidity
avghumid, minhumid, maxhumid = calculateData.getStats('/home/pi/winecellar/tmpdata/today.humid')

alert = ''
body = '<table>'

body += '<tr>'

greating = "<H1>Godmorgen " + setup.get('customer_name') + "</H1><b>Her er seneste data fra din vink&aelig;lder  </b>"


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

body += '</td><td></tr></table></br></br>'

body += alert +"<br><br><br>"

body += "<table><tr><td><b>Seneste 24 timers m&aring;linger: </b></td><td><b> Gennemsnit </b></td><td><b> Minimum </b></td><td><b> Maximum </b><td></tr> \
<tr><td>Temperatur</td><td style='background-color:lightgray'>" + avgtemp + "</td><td>" + mintemp + "</td><td style='background-color:lightgray'>" + maxtemp + "</td></tr>" \
"<tr><td>Luftfugtighed</td><td>" + avghumid + "</td><td style='background-color:lightgray'>" + minhumid + "</td><td>" + maxhumid + "</td></tr>"  \
+ "</table><br><br>"

#move todays tmp temp data file
mvfileweekday.move("/home/pi/winecellar/tmpdata/today.temp")

#move todays tmp humid data file
mvfileweekday.move("/home/pi/winecellar/tmpdata/today.humid")

# Create the root message and fill in the from, to, and subject headers
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = "Godmorgen fra din vinkælder." + " " + date 
msgRoot['From'] = setup.get('from_address') 
msgRoot['To'] = setup.get('customer_mail')
msgRoot['Bcc'] = setup.get('bcc')
msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

#make destinct id for graph file
today = datetime.date.today().strftime("%B%d%Y") + setup.get('id')

body += '<br><img src="cid:' + today + '"><br><br><object align="right">'+ setup.get('id') + "</object>"



# We reference the image in the IMG SRC attribute by the ID we give it below
msgText = MIMEText(body, 'html')
msgAlternative.attach(msgText)

# This assumes the image is on the described path
fp = open('/home/pi/winecellar/img/today.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<' + today + '>')

msgRoot.attach(msgImage)

# Send the email
p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE, universal_newlines=True)
p.communicate(msgRoot.as_string())
