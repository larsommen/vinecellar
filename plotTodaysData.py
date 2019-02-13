#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import datetime
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
mpl.rcParams.update({'font.size': 10})

# open the text file and create arrays of temperature and humidity

temp = tuple(open("/home/pi/winecellar/tmpdata/today.temp", 'r'))
humid = open("/home/pi/winecellar/tmpdata/today.humid", 'r')

# round values and remove newline chars

temp = [round(float(x[:len(x)-1]),1) for x in temp]

humid = [round(float(x[:len(x)-1]),1) for x in humid]

#humid = [x[:4] for x in t]

#make sure the array of temps is same length as array of humids

if (len(temp) != len(humid)):
	if (len(temp) > len(humid)):
		temp = np.resize(temp, len(humid))
	else:
		humid = np.resize(humid, len(temp))

# set up x-axis from start time til now with the number of intervals in the temp and humid arrays

initialDatetime = datetime.datetime.now() - datetime.timedelta(minutes=20*len(temp))
t = [(initialDatetime + datetime.timedelta(minutes=i*20)).strftime('%H:%M') for i in range(len(temp))]


#plot values

fig, ax = plt.subplots()

ax.plot(t, temp, label='Temperatur')
ax.plot(t, humid, label='Luftfugtighed')
ax.legend(bbox_to_anchor=(0.15, 1.13), loc=1, borderaxespad=0, fancybox=True, framealpha=0.5)

# set labels
today = str(datetime.datetime.now().strftime("%d. %m. %Y"))
danishTitle = "Seneste døgn (" + today + ")"
danishTitle= danishTitle.decode('utf-8') 

ax.set(xlabel='Klokkeslet', 
	ylabel='' ,# Temp. ($^\circ$C) --  Luftfugtighed (%)',
	title=danishTitle)
ax.grid()
plt.gcf().autofmt_xdate()

# hide some values in labels

n = 6
for index, label in enumerate(ax.xaxis.get_ticklabels()):
	if index % n   != 0 :
    		label.set_visible(False)
m =1 
for index, label in enumerate(ax.yaxis.get_ticklabels()):
        if index % m  != 0:
                label.set_visible(False)

# posistion plot and label in visible area

plt.gcf().subplots_adjust(left=0.12)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(top=0.9)
#plt.gcf().subplots_adjust(right=0.8)
#save file


fig.savefig("/home/pi/winecellar/img/today.png")
