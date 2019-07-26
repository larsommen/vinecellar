import matplotlib.pyplot as plt
import numpy as np
import get_user_data
plt.switch_backend('agg')
from datetime import *

setup = get_user_data.getall()


# get yesterdays number

weekdaynumber = datetime.utcnow().isocalendar()[2]
weekday = str(weekdaynumber)
filenameYesterday= "/home/pi/winecellar/tmpdata/today.humid" + weekday

fig = plt.figure()
ax = plt.axes()
lim=float(setup.get('humit_limit'))
limit = [lim,lim,lim,lim,lim,lim,lim]

xAxis = ["-2", "-1:40", "-1:20", "-1", "-0:40", "-0:20","0"]


missing =8 
values =[]

with open("/home/pi/winecellar/tmpdata/today.humid", "r") as f:
	try:
		lines = f.read().splitlines()
		for x in range(1,8):
			values.append(float(lines[-x]))
			missing = missing -1
	except:
		print missing
		if missing > 0:
			with open(yesterdays, "r") as f:
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


#with open('/home/pi/winecellar/tmpdata/today.humid', 'r') as f:
#	lines = f.read().splitlines()
#	for x in range(-7,0):
#	values.append(float(lines[x]))


ax.plot(values, label='Luftfugtighed (% relativ)', color='coral', linewidth=2)
ax.plot(limit, label="Fugt limit", color="red", linewidth=5 )
plt.xlabel('Timer:minutter')
plt.ylabel('%')
plt.title('Trend seneste 2 timer -- ' + now)
plt.gcf().subplots_adjust(left=0.12)
plt.gcf().subplots_adjust(top=0.84)
ax.legend(bbox_to_anchor=(0.36, 1.2), loc=1, borderaxespad=0, fancybox=True, framealpha=0.5)
ax.set_xticklabels(xAxis, minor=False)
#plt.show()


plt.savefig('/home/pi/winecellar/img/trendingHumid.png')
