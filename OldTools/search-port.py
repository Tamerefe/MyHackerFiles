#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Port Scan")

print("""

	  
Welcome to Port Scanning Tool :)

1) Quick Scan

2) Service and Version Information

3) Operating System Information

	  
""")

no = raw_input("Enter a number: ")

if(no=="1"):
	hedefip = raw_input("Enter Target IP: ")
	os.system("nmap " + hedefip)
elif(no=="2"):
	hedefip = raw_input("Enter Target IP: ")
	os.system("nmap -sS -sV " + hedefip)
elif(no=="3"):
	hedefip = raw_input("Enter Target IP: ")
	os.system("nmap -sS -sV " + hedefip)
else:
	print("You Made a Wrong Choice Chief :(")