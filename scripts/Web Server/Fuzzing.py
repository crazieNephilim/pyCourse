#!/usr/bin/python2
__author__ = 'kilroy'
#  (c) 2014, WasHere Consulting, Inc.
#  Written for Infinite Skills

from pyfuzz.generator import *
import socket

msg =   random_ascii() + b" / HTTP/1.1\nHost: 192.168.56.103\r\n"
print(msg)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("192.168.56.103", 80)
    s.connect(addr)
    s.sendall(msg)
    resp = s.recv(4096)
    print(resp)
except Exception as e:
    print(e)
finally:
    s.close()
