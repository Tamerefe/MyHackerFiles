#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Check Vpn")

print("""

Welcome to VPN Control Tool

""")

targetip = raw_input("Enter Target IP: ")

os.system("ike-scan " + targetip)