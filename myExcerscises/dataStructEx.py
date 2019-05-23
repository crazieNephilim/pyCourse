from collections import Counter
import operator

myDic = {}
myDic = Counter(['apple','red','apple','red','red','pear'])
print myDic
print "Max: " + str(max(myDic.iteritems(), key=operator.itemgetter(1))[0]) + ' = ' + str(max(myDic.iteritems(), key=operator.itemgetter(1))[1])