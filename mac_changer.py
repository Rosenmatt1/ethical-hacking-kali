#!/usr/bin/env python3

import subprocess

# raw_input() for python2 to jut use commnd python
interface = input("interface > ")
# "wlan0"
new_mac = input("new MAC > ")
# "00:1:22:33:44:77"

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface " down", shell=True)  # the true allows to run Linux commands through function
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + "up", shell=True)

subprocess.call(["ifconfig", interface, "down"])
# a list that tells the order of commands allowed by the user to pevent the user input from running other commands