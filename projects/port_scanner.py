# Run the script as: 'python port_scanner.py'
# Enter the target IP

# load the python script module that makes network connections
import socket 

# enter the target IP for example 192.168.1.10
target = input("Target IP: ")

# for loop that goes through ports 1 - 1024
for port in range(1, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates a new socket (IPv4 with TCP traffic)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))  #tries to make connection to target IP with current port

    if result == 0: # 0 means "port is open"
        print(f"Port {port} is open") 

    sock.close() 