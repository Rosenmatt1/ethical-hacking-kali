#!/usr/bin/env python3

import subprocess # the true allows to run Linux commands through function
import optparse
#allows to use users inputs as arguments

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New Mac address")

(options, arguments) = parser.parse_args()

interface = options.interface
# "wlan0"
new_mac = options.new_mac
# "00:11:22:33:44:77"

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

# subprocess.call(["ifconfig ", interface, " down"])
# subprocess.call(["ifconfig ", interface, " hw ether ", + new_mac, shell=True])
# subprocess.call(["ifconfig ", interface, " up"])
# a list that tells the order of commands allowed by the user to prevent the user input from running other commands