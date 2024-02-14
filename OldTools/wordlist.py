#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Create worldlist")

print("""

Welcome to Wordlist Creation Tool

""")

minimum = raw_input("Enter Minimum Number of Characters: ")
maximum = raw_input("Enter Maximum Number of Characters: ")
chrch = raw_input("Enter the Characters You Want: ")

os.system("crunch" + minimum + " " + maximum + " " + chrch)

print("Successfully Completed")