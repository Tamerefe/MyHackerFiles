#### Dns Scanning

```nmap -sU -sV -n -v -PN 8.8.8.8 -p 53```

#### Site Scanning

```nmap -sU -sV -n -v -Pn ,,,.com -p 161```

#### TCP Scanning

```nmap -sT -sV -n -v -Pn ,,,.com -p 80```

#### Browsing Without Getting Caught in a Firewall

```nmap -sS -sV -n -V -Pn ,,,.com -p 80```

#### Scanning the Processor

```nmap -sT -n -v -Pn -o 23.236.62.147```

#### Port Scanning

```nmap -sV -sT -n -v -Pn ,,,.com -p 21```

#### Port Anononimus User Open Scanning

```nmap -p 21 --script=ftp-anon -Pn -n ,,,.com```

#### Brute Force Attack

```nmap -sV -sT --script=ftp-brute -p 21 -v -n -Pn ,,,.com```

#### Simba File Exchange Scanning

```nmap --script=smb-enum-shares -Pn -p 139,445 -n 23.236.62.147```

#### Vulnerability (ADP) Scanning

```
nmap -sV -script=rdp-vuln-ms12-020 -p 3389 ,,,.com
...
nmap --script=smb-check-vulns -Pn -p 139,445 -n ,,,.com
```

#### Dual Port Scanning

```nmap -sT -sV -n -Pn -n ,,,.com -p 80,22```

#### Scanning Between 2 Ports

```nmap -sT -sV -n -Pn -n ,,,.com -p 20-443```

#### Fraud and Scanning of Many IP Systems

```nmap -D ip,ip,ip,ip -e eth0 -sV -v -n -Pn ,,,.com -p 80``` (Write the ip to scan where it says ip)

#### Sending Requests Piece by Piece

```
nmap -f -f -sS -sV -n -v -Pn ,,,.com -p 22 (-f splits requests up to 8)
nmap --mtu 10 -sS -sV -n -v -Pn ,,,.com -p 25 (can be divided by 10)
```

#### For Package Manipulation

```nmap --badsum -n -v -sS -sV -Pn ,,,.com -p 21```

#### Different Scanning Method

```nmap --ttl 100 -n -v -sS -sV -Pn ,,,.com -p 21```

#### Zenmap 

```Target:,,,.com``` (Intense Scan)/(Quick Scan)

#### Dirbuster

```
nmap -sT -sV -n -v -Pn ,,,.com
nmap -sT -sV -n -v -Pn ,,,.com -80,443

dirbuster
(/usr/share/dirbuster/wordlists)
```