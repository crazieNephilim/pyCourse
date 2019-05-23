# !/usr/bin/python
import os, sys
from operator import itemgetter, attrgetter

# using command mkdir
a = 'ps -ef >> proces.txt'
output = os.popen(a)

f = open("/home/pythontools/Documents/pyCourse/proces.txt","r")

lineArr = []
newLineArr = []
fileArr = []

for line in f:
    
    lineArr = line.split()
    procUser = str(lineArr [0])
    procID = str(lineArr [1])
    parrID = str(lineArr [2])
    procStartTime = str(lineArr [4]) + ' ' + str(lineArr [6])
    cmmd = str(lineArr [7])
    
    newLineArr.append(procUser)
    newLineArr.append(procID)
    newLineArr.append(parrID)
    newLineArr.append(procStartTime)
    newLineArr.append(cmmd)
    fileArr.append(newLineArr)
    newLineArr = []
f.close()

fileArr.sort(key=lambda x: (x[2], x[1]))

f = open("/home/pythontools/Documents/pyCourse/sortedProces.txt","w")
f.write("User\tProcesID\tParrentID\tStartTime\tCommand\n") 
for item in fileArr:
    line = str(item[0]) + "\t" + str(item[1]) + "\t" + str(item[2]) + "\t" + str(item[3]) + "\t" + str(item[4]) + "\n"
    f.write(line)

f.close()