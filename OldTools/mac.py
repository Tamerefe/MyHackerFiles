#!/usr/bin/env python
import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet CHANGE MAC")

print("""

Welcome to MAC Address Change Tool :)

1) Determine Mac Address Randomly

2) Specify Mac Address Manually

3) Freeze Mac Address to Original

""")

no = raw_input("Enter a Number: ")

if(no=="1"):

	os.system("ifconfig eth0 down")
	os.system("macchanger -r eth0")
	os.system("ifconfig eth0 up")

	print("\033[92mThe new MAC Address was determined manually.")
elif(no=="2"):

	macadres = raw_input("Enter New Mac Address: ")

	os.system("ifconfig eth0 down")
	os.system("macchanger --mac " + macadres + "eth0")
	os.system("ifconfig eth0 up")

	print("\033[92mThe new MAC Address was determined manually.")
elif(no=="3"):

	os.system("ifconfig eth0 down")
	os.system("macchanger -p eth0")
	os.system("ifconfig eth0 up")

	print("\033[92mMAC Orjinale Dondu.")
else:

	print("I Can't Specify Mac Address, But You're Good Again, I'll Restart")

	os.system("python mac.py")