from scapy.all import *

pkts_list = rdpcap('/home/pythontools/Downloads/file.pcap')

#This shows the number of packets in the file
lenpkrt = len(pkts_list)
#print(lenpkrt)

#This is an example of reading a packet
#pkts_list[x].summary()

#This is how you access the parameters
srcip = pkts_list[0]['IP'].src
#print(srcip)
x=0

#this is an example of looping through and printing out a specific paramter
# while (x < lenpkrt-1):
#     print(x)
#     x= x + 1
#     srcip = pkts_list[x]['IP'].src
#     print(srcip)

#While loop is used to find a src ip in question
while (x < lenpkrt-1):
    #print(x)
    x= x + 1
    srcip = str(pkts_list[x]['IP'].src)

    if srcip == '192.168.2.147':
        try:
            print pkts_list[x].summary()
            ipaddr = pkts_list[x]['IP'].src
            mac = pkts_list[x]['Ethernet'].src
            hostName = pkts_list[x]['NBNS query request'].QUESTION_NAME
            print "****************IP Address: " + ipaddr + " MAC address: " + mac + " Host Name: " + hostName 
            
        except:
            pass
    
        
        #This will show you the whole packet
        # wholePacket = pkts_list[0].show()
        # print (wholePacket)
        # this exits the progam as soon as a positive result is returned
        #break