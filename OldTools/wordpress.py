#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Wordpress Scan")

print("""

Welcome to the Wordpress Scanning Tool

1) Quick Scan

2) Plugin Scanning

3) Theme Browsing

4) Administrator Username Scan

""")

no = raw_input("Enter a Number: ")

if(no=="1"):
	site = raw_input("Enter Site Address: ")
	os.system("wpscan --url " + site)
elif(no=="2"):
	site = raw_input("Enter Site Address: ")
	os.system("wpscan --url " + site + " --enumerate p" )
elif(no=="3"):
	site = raw_input("Enter Site Address: ")
	os.system("wpscan --url " + site + " --enumerate t" )
elif(no=="4"):
	site = raw_input("Enter Site Address: ")
	os.system("wpscan --url " + site + " --enumerate u" )
else:
	print("You Made a Wrong Choice, I'm Closing the Program")