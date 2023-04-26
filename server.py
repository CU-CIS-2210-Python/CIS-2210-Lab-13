import socket;

PORT = 1787  # The port used by the server

#Create a socket, store it in the s variable
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", PORT))   #Bind on all addresses, on the specified PORT
    s.listen()                  #Listen for connections

    print("Waiting for connection...")
    conn, addr = s.accept() #Wait for a connection from a client.

    with conn:
        #Print the address we have a connection from
        print(f"Got new connection from {addr}")

        #Convert the connection into a stream we can read and write
        stream = conn.makefile('rw')
        
        while True:
            #Wait for a message from the other program and print it out
            print("Waiting...")
            receivedMessage = stream.readline()
            print(f"Got message: {receivedMessage.strip()}")

            #Ask the user for a message and send it
            messageToSend = input("Type your message: ")
            stream.write(messageToSend + "\n")
            stream.flush()