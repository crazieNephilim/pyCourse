# !/usr/bin/python
import os, sys

loc = '/etc/* '
loc1 = '/sys/* '
loc2 = '/root/* '
a = 'ls -la ' + loc + loc1 + loc2 + '>> permission_log.txt'
output = os.popen(a)

f = open("/home/pythontools/Documents/pyCourse/permission_log.txt","r")
lineArr = []
logArr = []

for line in f:
    if not line.startswith('total') and not line.startswith('/'):
        if not line.strip():
            continue
        else:
            lineArr = line.split()    
            logArr.append(lineArr) 

logArr.sort(key=lambda x: (x[-1]))

f = open("/home/pythontools/Documents/pyCourse/log_old_proc.txt","w")
for i in logArr:
    for j in i:
        f.write(str(j) + "\t")
    f.write("\n")