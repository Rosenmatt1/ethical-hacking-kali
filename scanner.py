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
    # answered_list, unanswsered_list = scapy.srp(arp_request_broadcast, timeout=1)
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0] #tells it to return only 1st item returned which is the answered list
    # print(answered_list.summary())

    print("IP\t\t\tMAC ADDRESS\n------------------------------------")   #the \t creates a tab os space and the \n goes to next line
    for element in answered_list:
        # print(element[1].show())
        print(element[1].psrc + "\t\t" + element[1].hwsrc)


    # print(broadcast.summary())
    # scapy.ls(scapy.Ether())
    # print(arp_request.summary())
    # scapy.ls(scapy.ARP())  list all fields we can change


scan("10.0.2.1/24")


# ip_address = "192.168.1.1/24"
#
# subprocess.call("netdiscover " + "-r " + ip_address, shell=True)