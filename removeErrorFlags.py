#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import commands
import os


existsTempError = os.path.isfile('/home/pi/winecellar/tmpdata/errorTemp.test')
existsHumidError = os.path.isfile('/home/pi/winecellar/tmpdata/errorHumid.test')

if existsHumidError:
	subprocess.call(['rm', '/home/pi/winecellar/tmpdata/errorHumid.test'])

if existsTempError:
        subprocess.call(['rm', '/home/pi/winecellar/tmpdata/errorTemp.test'])	
