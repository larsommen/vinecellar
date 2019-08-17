#!/bin/bash
cd /home/pi/winecellar
git pull
python /home/pi/winecellar/sendUpdataLog.py
