#!/usr/bin/python
__author__ = 'kilroy'
#  (c) 2014, WasHere Consulting, Inc.
#  Written for Infinite Skills
#  this requires NTFS on the file system
#  used to check for vuln in alternate Data Streams. Could create a program that loops through this

fh = open("file.txt:myfile", "w")
fh.write("this is a test")
fh.close()

fh = open("file.txt:myfile", "r")
data = fh.read(100)
print(data)


