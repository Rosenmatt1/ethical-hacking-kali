#!/usr/bin/env python3

import subprocess # the true allows to run Linux commands through function
import optparse
#allows to use users inputs as arguments
#parser

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac address")
    # python mac_changer.py --interface wlan0 --mac 00:11:22:33:44:55
    # python mac_changer.py --i wlan0 --m 00:11:22:33:44:55
    return parser.parse_args()


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)
    # subprocess.call(["ifconfig ", interface, " down"])
    # subprocess.call(["ifconfig ", interface, " hw ether ", + new_mac, shell=True])
    # subprocess.call(["ifconfig ", interface, " up"])
    # a list that tells the order of commands allowed by the user to prevent the user input from running other commands

(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)