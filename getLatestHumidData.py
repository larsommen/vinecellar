import matplotlib.pyplot as plt
import numpy as np
import get_user_data
plt.switch_backend('agg')

setup = get_user_data.getall()


fig = plt.figure()
ax = plt.axes()
lim=float(setup.get('humit_limit'))
limit = [lim,lim,lim,lim,lim,lim,lim]

xAxis = ["-2", "-1:40", "-1:20", "-1", "-0:40", "-0:20","0"]

values = []

with open('/home/pi/winecellar/tmpdata/today.humid', 'r') as f:
	lines = f.read().splitlines()
	for x in range(-7,0):
		values.append(float(lines[x]))


ax.plot(values, label='Luftfugtighed (% relativ)', color='coral')
ax.plot(limit, label="Temp limit", color="red", linewidth=5 )
plt.xlabel('Timer:minutter')
plt.ylabel('%')
plt.title('Trend seneste 2 timer')
ax.legend(bbox_to_anchor=(0.31, 1.15), loc=1, borderaxespad=0, fancybox=True, framealpha=0.5)
ax.set_xticklabels(xAxis, minor=False)
#plt.show()


plt.savefig('/home/pi/winecellar/img/trendingHumid.png')
