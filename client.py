import socket

IP = "127.0.0.1"
PORT = 3514

client_socket = socket.socket()
client_socket.connect((IP, PORT))


#send and receive message
while True:
    msg = input(":: ")

    client_socket.send(bytes(msg, 'utf-8'))
    print(client_socket.recv(1024).decode())

client_socket.close()

