# Run the script as: 'python port_scanner.py'
# Enter the target IP

# load the python script module that makes network connections
import socket 

# enter the target IP for example 192.168.1.10
target = input("Target IP: ")

# for loop that goes through ports 1 - 1024
for port in range(1, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))  

    if result == 0:
        try:
            service = socket.getservbyport(port, "tcp")
        except:
            service = "Unknown service"

        print(f"Port {port} is open ({service})")

    sock.close() 