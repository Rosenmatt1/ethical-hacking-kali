#!/usr/bin/env python3
import subprocess # the true allows to run Linux commands through function

ip_address = "192.168.1.1/24"

subprocess.call("netdiscover " + "-r " + ip_address, shell=True)