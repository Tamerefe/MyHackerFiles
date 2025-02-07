import wmi
import time


c = wmi.WMI()

for x in range (0,4):  
    b = "Working" + "." * x
    print (b, end="\r")
    time.sleep(0.5)

for os in c.Win32_OperatingSystem():
    print(os.Caption)
    print(os.OSArchitecture)
    print(os.Version)