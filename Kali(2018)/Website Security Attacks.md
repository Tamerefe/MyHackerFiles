### Website Copy
```
httrack
site
/root/
10.0.2.5
1
enter
enter
enter
y
```

### Site Vulnerability Analysis Pentest Study

- Open owasp zap
  - Manual scan
```
https://10.0.2.5
attack
alert
```

### Skipfish (Saves the Site, Disrupts it and Finds the Vulnerabilities)

```skipfish -o /root/tarama http://10.0.2.5```

### WebScarab (Detects Links on the Site)

### Change Proxy

```Spider```

### Wpscan

```
wpscan --url //.com --enumerate u
wpscan --url //.com --wordlist /root/Desktop/password.txt --username admin
wpscan --url //.com --enumerate p
```

