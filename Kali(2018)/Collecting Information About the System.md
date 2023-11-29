```whois``` ... = Gives most of the information on the website <br>
```ping``` = IP and ping value of the site <br>
- You can do it on the Robtex Website <br>

```WebArchive``` = Sitenin geçmişini gösterir <br>
```Pipl``` = Finds the Person <br>
```Foundstone sitedigger``` = Finds Site Vulnerabilities <br>
```theharvester -d mpalmun.com -l 1000 -b all``` = Scans the site <br>

```
---
msfconsole
use auxiliary/gather/search_email_collector 
show opt�ons
set DOMAIN mpalmun.com
exploit

----
site.*.mpalmun.com
site:mpalmun.com inurl:page.php?intPagelD=
site:mpalmun.com inurl:?id=
intext:kullanici sifre site:mpalmun.com = Whatever you type instead of user password is searched on the site.
allintext:sifre site:mpalmun.com
inurl:admin site:mpalmun.com
allinurl:adminpanel , allinurl:"/admin/" , allinurl:wp-admin
allinurl:adminpanel site:maplmun.com
allinurl:"/admin/" site:mpalmun.com
allinurl:wp-admin site:mpalmun.com 
filetype:xls "�ifre" site:mpalmun.com
intitle:index.of site:mpalmun.com
intitle:index.of ws_ftp log site:mpalmun.com
intitle:index.of inurl:"/admin/" site:mpalmun.com
"Powered by phpBB" inurl:"index.php?s" OR inurl:"index.php?style"
```

### Active Information Collection

```
tcptraceroute 23.236.62.147
traceroute 147.62.236.23.bc.googleusercontent.com / Windows ��in tracert mpalmun.com

wafw00f https://www.mpalmun.com

nmap -p80 --script http-waf-detect --script-args="http-waf-detect.aggro,http-waf-detect.uri=/testphp.vulnweb.com/artists.php" www.mpalmun.com

https://www.mpalmun.com/.../.../.../etc/passwd
https://www.mpalmun.com/cmd.exe

dig mpalmun.com A
dig mpalmun.com MX
dig mpalmun.com NS
dig @ns0.wixdns.net zonetransfer.me axfr
dig @ns0.wixdns.net zonetransfer.me version.bind chaos txt

nmap -sU -sV -n -v -PN @ns0.wixdns.net zonetransfer.me -p 53
nmap -sU -sV -n -v -PN mpalmun.com -p 161


msfconsole
use auxiliary/scanner/snmp/snmp_login 
show options
set RHOSTS 23.236.62.147
exploit

use auxiliary/scanner/snmp/snmp_enum
show options
set RHOSTS mpalmun.com
exploit
```

### Dmitry

```
dmitry
dmitry -iwnsepf /\.com
dmitry -iwnsepf /\.com -o /root/info.txt
```

### Learning IP VPN or Not

```
ike-scan
ike-scan 23.236.62.147
```

### Finding Out Which Port Someone Is Using

```
p0f
p0f -i eth0
```

### Site Vulnerability Analysis

```
recon-ng
show modules
use recon/domains-vulnerabilities/punkspider
show options
set SOURCE //.com
run
```


