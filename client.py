import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 1787  # The port used by the server

#Connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    #Convert the connection into a stream we can read and write
    stream = s.makefile("rw")

    while True:
        #Ask the user for a message and send it
        messageToSend = input("Type your message: ")
        stream.write(messageToSend + "\n")
        stream.flush()

        #Wait for a message from the other program and print it out
        print("Waiting...")
        receivedMessage = stream.readline()
        print(f"Got message: {receivedMessage.strip()}")