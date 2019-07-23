import matplotlib.pyplot as plt
import numpy as np



fig = plt.figure()
ax = plt.axes()
values = []
xAxis = ["-2", "-1.4", "-1.2", "-1", "-0.4", "-0.2","0"]


with open('/home/pi/winecellar/tmpdata/today.temp', 'r') as f:
	lines = f.read().splitlines()
	for x in range(-7,0):
		values.append(float(lines[x]))


ax.plot(xAxis, values, label='Temperatur ($^\circ$C)')
plt.xlabel('Timer.minutter')
plt.ylabel('$^\circ$C')
plt.title('Trend for seneste 2 timer')
ax.legend(bbox_to_anchor=(0.21, 1.15), loc=1, borderaxespad=0, fancybox=True, framealpha=0.5)

plt.show()


plt.savefig('/home/pi/trending.png')
