#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import datetime
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import array as arr

mpl.rcParams.update({'font.size': 10})

# open the text file and create array of humidity

humid = open("/home/pi/winecellar/tmpdata/today.humid", 'r')

# round values and remove newline chars

humid = [round(float(x[:len(x)-1]),0) for x in humid]

# set up x-axis from start time til now with the number of intervals in the temp and humid arrays

initialDatetime = datetime.datetime.now() - datetime.timedelta(minutes=20*len(humid))
t = [(initialDatetime + datetime.timedelta(minutes=i*20)).strftime('%H:%M') for i in range(len(humid))]

#plot values

fig, ax = plt.subplots()

ax.plot(t, humid, color='green', label='Luftfugtighed (% relativ)')
ax.legend(bbox_to_anchor=(0.3, 1.13), loc=1, borderaxespad=0, fancybox=True, framealpha=0.5)

# set labels
today = str(datetime.datetime.now().strftime("%d. %m. %Y"))
danishTitle = "Seneste døgn (" + today + ")"
danishTitle= danishTitle.decode('utf-8') 

ax.set(xlabel='Klokkeslet', 
	ylabel='' ,
	title=danishTitle)
ax.grid()
plt.gcf().autofmt_xdate()

# hide some values in labels

n = 6
for index, label in enumerate(ax.xaxis.get_ticklabels()):
	if index % n   != 0 :
    		label.set_visible(False)

# posistion plot and label in visible area

plt.gcf().subplots_adjust(left=0.12)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(top=0.9)
#plt.gcf().subplots_adjust(right=0.8)
#save file


fig.savefig("/home/pi/winecellar/img/todayHumid.png")
