import subprocess

allfiles = subprocess.call(['ls', "-alg", "/home/pi/winecellar"])
print allfiles
