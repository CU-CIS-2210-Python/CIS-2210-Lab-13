import socket

#HTTP 1.1 RFC: https://www.ietf.org/rfc/rfc1945.txt
#HTTP 1.1 RFC: https://datatracker.ietf.org/doc/html/rfc2616


HOST = "www.example.com"  # The server's hostname or IP address
PORT = 80  # The port used by the server

#Connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    #Convert the connection into a stream we can read and write
    stream = s.makefile("rw")

    #Write a 
    stream.write("GET /\n")
    stream.write(f"Host: {HOST}\n")
    stream.write("\n")
    stream.flush()

    for line in stream.readlines():
        print(line.strip())