import os
import datetime

def move(filename):
	weekday = str(datetime.datetime.today().weekday())

	src = filename
	dst = filename + weekday

	if os.path.isfile(src):
	    os.rename(src, dst)
