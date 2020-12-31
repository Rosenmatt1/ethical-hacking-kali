#!/usr/bin/env python3

import subprocess # the true allows to run Linux commands through function
import optparse
#allows to use users inputs as arguments

# raw_input() for python2
interface = input("interface > ")
# "wlan0"
new_mac = input("new MAC > ")
# "00:11:22:33:44:77"

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

# subprocess.call(["ifconfig ", interface, " down"])
# subprocess.call(["ifconfig ", interface, " hw ether ", + new_mac, shell=True])
# subprocess.call(["ifconfig ", interface, " up"])
# a list that tells the order of commands allowed by the user to prevent the user input from running other commands