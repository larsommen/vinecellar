import matplotlib.pyplot as plt
import numpy as np
import commands
import get_user_data
plt.switch_backend('agg')
from datetime import *
import itertools

# get yesterdays number

weekdaynumber = datetime.utcnow().isocalendar()[2]
weekday = str(weekdaynumber)
filenameYesterday= "/home/pi/winecellar/tmpdata/today.temp" + weekday


setup = get_user_data.getall()

fig = plt.figure()
ax = plt.axes()
values = []
xAxis = ['-2', '-1:40', "-1:20", "-1", "-0:40", "-0:20","0"]
altY = [1,2,3,4,5,6,7]
 
lim=float(setup.get('temp_limit'))
limit = [lim,lim,lim,lim,lim,lim,lim]

yesterdays = open(filenameYesterday, "r")
todays = open('/home/pi/winecellar/tmpdata/today.temp', 'r')


missing =8 
values =[]

with open("/home/pi/winecellar/tmpdata/today.temp", "r") as f:
	try:
		lines = f.read().splitlines()
		for x in range(1,8):
			values.append(float(lines[-x]))
			missing = missing -1
	except:
		if missing > 0:
			with open(filenameYesterday, "r") as f:
				try:
                			lines = f.read().splitlines()
                			for x in range(1,missing):
                        			values.append(float(lines[-x]))
				except:
					print "error"	

switch =[]


for x in range (len(values)-1, -1, -1):
	switch.append(values[x])

values = switch

now = datetime.now().strftime("%H:%M")

#with open('/home/pi/winecellar/tmpdata/today.temp', 'r') as f:
#	lines = f.read().splitlines()
#	for x in range(-7,0):
#		values.append(float(lines[x]))

ax.plot( values, label='Temperatur ($^\circ$C)', linewidth=2)
ax.plot( limit, label="Temp limit", color="red",  linewidth=5)
plt.xlabel('Timer:minutter')
plt.ylabel('$^\circ$C')
plt.title('Trend seneste 2 timer -- '+ now )
plt.gcf().subplots_adjust(left=0.12)
plt.gcf().subplots_adjust(top=0.84)
ax.legend(bbox_to_anchor=(0.24, 1.19), loc=1, borderaxespad=0, fancybox=True, framealpha=0.5)
ax.set_xticklabels(xAxis, minor=False)


plt.savefig('/home/pi/winecellar/img/trendingTemp.png')
