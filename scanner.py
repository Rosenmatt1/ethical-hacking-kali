#!/usr/bin/env python3
import subprocess # the true allows to run Linux commands through function
import scapy.all as scapy
import optparse #allows to use users inputs as arguments

# route -n (in terminal shows all the IP address)
# def scan(ip):
#     scapy.arping(ip)
#
# scan("10.0.2.1/24")

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help=" ip address to send back MAC")
    # python mac_changer.py --target 10.0.2.1/24
    # python mac_changer.py --t 10.0.2.1/24
    (options, arguments) = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify a target, use --help for more info.")
    return options

# function to get MAC address manually instead of using scapy.arping
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    # arp_request_broadcast.show()
    # answered_list, unanswsered_list = scapy.srp(arp_request_broadcast, timeout=1)
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] #tells it to return only 1st item returned which is the answered list
    # print(answered_list.summary())

    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
        # print(element[1].show())
        # print(element[1].psrc + "\t\t" + element[1].hwsrc)
    return client_list
    # print(broadcast.summary())
    # scapy.ls(scapy.Ether())
    # print(arp_request.summary())
    # scapy.ls(scapy.ARP())  list all fields we can change


def print_result(results_list):
    print("IP\t\t\tMAC ADDRESS\n------------------------------------")  # the \t creates a tab os space and the \n goes to next line
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)
# 10.0.2.1/24


# ip_address = "192.168.1.1/24"
# subprocess.call("netdiscover " + "-r " + ip_address, shell=True)