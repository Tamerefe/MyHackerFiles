```
mysql -u root -h 10.0.2.9
show databases;
use mysql
show tables;
select * from user;
use owasp10;
show tables;
select * from credit_cards;
```

### HexorBase (Infiltrating the Database)

- #### Bruteforce Database Servers
```
--
nmap -sS -sV 10.0.2.5
10.0.2.5
user or word list
Ateempt Blank Password
Launch Attack
--
Administration
username or password
Lock as Default Login
MySql
10.0.2.5
```

### DB Browser For SQlite (Create DataBase)

```
New Database
databases.db
...
Add field
...
Ok
Browse Data
...
Write Changes
```