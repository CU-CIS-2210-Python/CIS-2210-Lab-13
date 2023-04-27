import socket

hostname = socket.gethostname()   
ip = socket.gethostbyname(hostname)   

print(f"Your Computer's Host Name is: {hostname}")   
print(f"Your Computer's IP Address is: {ip}")   