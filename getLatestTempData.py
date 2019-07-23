import matplotlib.pyplot as plt
import numpy as np
import datetime
import commands
import get_user_data


setup = get_user_data.getall()

fig = plt.figure()
ax = plt.axes()
values = []
xAxis = ["-2", "-1:40", "-1:20", "-1", "-0:40", "-0:20","0"]

lim=float(setup.get('temp_limit'))
limit = [lim,lim,lim,lim,lim,lim,lim]

with open('/home/pi/winecellar/tmpdata/today.temp', 'r') as f:
	lines = f.read().splitlines()
	for x in range(-7,0):
		values.append(float(lines[x]))

date = commands.getoutput("date")
ax.plot(xAxis, values, label='Temperatur ($^\circ$C)')
ax.plot(xAxis, limit, label="Temp limit", color="red")
plt.xlabel('Timer:minutter')
plt.ylabel('$^\circ$C')
plt.title('Trend seneste 2 timer ' )
ax.legend(bbox_to_anchor=(0.21, 1.15), loc=1, borderaxespad=0, fancybox=True, framealpha=0.5)

plt.show()


plt.savefig('/home/pi/winecellar/img/trendingTemp.png')
