#!/usr/bin/env python3
import subprocess # the true allows to run Linux commands through function
import scapy.all as scapy

# route -n (in terminal shows all the IP address)
# def scan(ip):
#     scapy.arping(ip)
#
# scan("10.0.2.1/24")

# function to get MAC address manually intead of using scappy
def scan(ip):



# ip_address = "192.168.1.1/24"
#
# subprocess.call("netdiscover " + "-r " + ip_address, shell=True)