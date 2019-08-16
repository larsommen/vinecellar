# winecellar
A project to monitor temperature and humidity in wine cellars using a Raspberry Pi and the BME280 sensor

This project will using the i2c on a raspberry pi, check temperature and humiditi every 20 minutes, send an email if limits have been compromised. Every morning send a mail to the owner of the wine cellar stating temperature and humidity and a similar email to sys-admin with some extra information.
In case of a file-io or a sensor-error a mail will be created and send to the sys-admin

Version history:
ver. 0.95  (current) - works as described above - look at the [wiki](https://github.com/larsommen/winecellar/wiki) for further detail.
