#!/usr/bin/python
import urllib
import urllib2

#URL to create a new user on the OWASP website
url = "http://192.168.56.103/bWAPP/user_new.php"
data = {'login' : 'NewUser1', 'email' : 'tester1@email.net', 'password' : 'password1', 'password_conf' : 'password1', 'secret' : 'kittyCat', 'mail_activation' : '1', 'action': 'Submit' }
params = urllib.urlencode(data)
req = urllib2.Request(url, data=params)
handle = urllib2.urlopen(req)
page = handle.read()
print(page)