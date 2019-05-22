import re
from collections import Counter

#logfile =  input("What log file are you parsing? ")


def apache_log_reader(logfile):
    myregex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    with open(logfile) as f:
        log = f.read()
        my_iplist = re.findall(myregex,log)
        ipcount = Counter(my_iplist)
        for k, v in ipcount.items():
            print("IP Address " + "=> " + str(k) + " " + "Count " + "=> " + str(v))

#Create an entry point for our code
if __name__ =='__main__':
    apache_log_reader("/home/pythontools/Documents/python/PythonClass/scripts/apachelog/access_log")