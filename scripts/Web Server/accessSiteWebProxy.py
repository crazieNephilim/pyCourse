#!/usr/bin/python

import urllib2

#requires connection to internet
#get OWASP ZAP to show that it went through proxy

proxy = urllib2.ProxyHandler({'http' : '127.0.0.1:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
handle = urllib2.urlopen('http://www.microsoft.com')

print(handle.read())