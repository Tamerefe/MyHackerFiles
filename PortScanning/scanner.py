import socket 

def scan(target, ports):
    clcoding = socket.gethostbyname(target)
    print('\n' + 'Starting Scan for ' + clcoding + '\n')

    for port in range(1, ports):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((clcoding, port))
        if result == 0:
            print('Port {} is open'.format(port))
        sock.close()

target = input('Enter the target to scan: ')
ports = int(input('Enter the number of ports to scan: '))
scan(target, ports)
