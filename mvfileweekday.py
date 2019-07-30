#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
from datetime import *

def move(filename):
	weekdaynumber = datetime.utcnow().isocalendar()[2]
	weekday = str(weekdaynumber)
	src = filename
	dst = filename + weekday
	if os.path.isfile(src):
	    os.rename(src, dst)
	return dst
