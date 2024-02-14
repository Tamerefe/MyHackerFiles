#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet FIREWALL DETECTION")

print("""

Welcome to the Firewall Detection Tool


""")

site = raw_input("Enter Site Address: ")

os.system("wafw00f " + site)