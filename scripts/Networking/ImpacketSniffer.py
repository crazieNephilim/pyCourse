#!/usr/bin/python
'''
synscan.py ...
see scan.py for parameters

this works extremely well in a windows that likes to communicate
scanning hosts in same ethernet is possible
scanning host not within the same ethernet may success but does not need to

many algorithms were tried

-   raw socket support needs higher previleges
    and is impossible because windows does not allow to sniff with them
    or to submit sniffable packets
->  not implemented here

    "Why do you need special libraries for TCP-SYN scans?"
    thats why.

using pcap the program is devided into phases
usually it succeeds in phase 1.
phase 0:
    add targets and phase 1
phase 1+: (parallel)
    send arp request to resolve target
    bombard it with the right packets
    sniff
phase 2:
    send out udp to resolve mac address by sniffing
    send out raw socket tcp syn requests (need higher previleges) optional
phase 3:
    if not yet succeeded in phase 1: = mac not found
    bombard all macs with packets
phase 4:
    bombard broadcasting [mac ff:ff:ff:ff:ff:ff] with packets
phase 5:
    clean up - no use

use DEBUG_PHASE to show phases

currently only ipv4 is supported

'''


import sys
import time
import _thread
import pcapy # pcapy
import impacket
import random

import impacket.ImpactDecoder as ImpactDecoder


import array

import scan
from scan import *

DEFAULT_SOCKET_TIMEOUT = 20
NOTIFY_TIMEOUT = 2

# argument incdeces for socket.socket(...)
SOCK_INIT_FAMILY = 0
SOCK_INIT_TYPE = 1
SOCK_INIT_PROTO = 2

STATE_STATE = 1
STATE_TIME = 0

PCAP_ARGS = ()
PCAP_KW = dict(promisc = True, timeout_ms = 0)

DEBUG = False
DEBUG_IFACE =   False and DEBUG # put out which devices are set up
DEBUG_IP =      False and DEBUG # print ip debug output for ip packets v4
DEBUG_ARP =     False and DEBUG # send arp communication debug out
DEBUG_SYN =     False and DEBUG # print out the syn requests sent
DEBUG_PACKET =  False and DEBUG # packet inspection as seen by scanner
DEBUG_PHASE =   True and DEBUG # scanner phases - 5
DEBUG_STATE =   False and DEBUG # debug output about the state
DEBUG_PHASE2 =  False and DEBUG # debug output about what is sent in phase 2
                                 # you need higher previleges for some of these operations

ETHER_BROADCAST = (0xff,) * 6 # mac ff:ff:ff:ff:ff:ff


# --- Conversions --------------------------------------------------------------

def ip_tuple(ip):
    '''Decode an IP address [0.0.0.0] to a tuple of bytes'''
    return tuple(map(int, ip.split('.')))

def tuple_ip(ip):
    '''Encode a a tuple of bytes to an IP address [0.0.0.0]'''
    return '.'.join(map(str, (ip[0], ip[1], ip[2], ip[3])))

# --- Packet Creation --------------------------------------------------------------

def generate_empty_arp_request():
    # build ethernet frame
    eth = ImpactPacket.Ethernet()
    eth.set_ether_type(0x0806)          # this is an ARP packet
    eth.set_ether_dhost(ETHER_BROADCAST)# destination host (broadcast)

    # build ARP packet
    arp = ImpactPacket.ARP()
    arp.set_ar_hrd(1)
    arp.set_ar_hln(6)                   # ethernet address length = 6
    arp.set_ar_pln(4)                   # ip address length = 4
    arp.set_ar_pro(0x800)               # protocol: ip
    arp.set_ar_op(1)                    # opcode: request
    arp.set_ar_tha(ETHER_BROADCAST)     # target hardware address (broadcast)
    eth.contains(arp)
    return eth, arp

def generate_empty_ip_packet():
    eth = ImpactPacket.Ethernet()
    #### values to be set:
    # type, shost, dhost
    eth.set_ether_type(0x800)

    ip = ImpactPacket.IP()

    #### values to be set:
    # version, IHL, TOS, total_length, ID, Flags, Fragment offset, 
    # TTL, Protocol, Checksum, source_addr, destination_addr, options
    ip.set_ip_v(4)  
    ip.set_ip_hl(5)