#!/usr/bin/env python3
import subprocess # the true allows to run Linux commands through function
import scapy.all as scapy

# route -n (in terminal shows all the IP address)
# def scan(ip):
#     scapy.arping(ip)
#
# scan("10.0.2.1/24")

# function to get MAC address manually instead of using scappy
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)

    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    arp_request_broadcast = broadcast/arp_request
    # arp_request_broadcast.show()
    answered, unanswsered = scapy.srp(arp_request_broadcast)

    # print(broadcast.summary())
    # scapy.ls(scapy.Ether())
    # print(arp_request.summary())
    # scapy.ls(scapy.ARP())  list all fields we can change


scan("10.0.2.1/24")


# ip_address = "192.168.1.1/24"
#
# subprocess.call("netdiscover " + "-r " + ip_address, shell=True)