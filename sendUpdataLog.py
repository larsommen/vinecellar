#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
from subprocess import Popen, PIPE #to send email via gmail
import smtplib
from email.mime.multipart import MIMEMultipart
from datetime import *
import get_user_data
import mvfile


setup = get_user_data.getall()

msg = MIMEMultipart('alternative')

#get week number
today = datetime.today()
weeknumber = datetime.utcnow().isocalendar()[1]

filename = "/home/pi/updates.log"
f = file(filename)
attachment = MIMEText(f.read())
attachment.add_header('Content-Disposition', 'attachment', filename=filename)           
msg.attach(attachment)

msg["From"] = setup.get('from_address')
msg["To"] = setup.get('bcc')
msg["Subject"] = "Opdateslog fra " + str(setup.get('customer_name')) + "\'s "+ setup.get('short_title') 
p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE, universal_newlines=True)
p.communicate(msg.as_string())
