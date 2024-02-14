#!/usr/bin/env python
import os

import py_compile

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Compiler Tool")

print("""

Welcome Compiler Tool


""")


Compil = raw_input("Enter the Program Name: ")

py_compile.compile(Compil)