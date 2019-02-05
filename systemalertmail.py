#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import get_user_data
import sys
import commands
import bme280
from email.mime.text import MIMEText #to be used to create mail opbject
from subprocess import Popen, PIPE #to send email via gmail

ex = sys.argv[1]

#set date to current date
date = commands.getoutput("date")


#template = "An exception of type {0} occurred. Arguments:\n{1!r}"
message = ex
print message

setup = get_user_data.getall()

customername = setup.get('customer_name')
body = customername + "<br><br>" + message

msg = MIMEText(body, 'html')
msg["From"] = setup.get('from_address')
msg["To"] = setup.get('bcc')

subject = "Error fra " + customername + "'s vinkælder." + " " + date
msg["Subject"] = subject
p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE, universal_newlines=True)
p.communicate(msg.as_string())
