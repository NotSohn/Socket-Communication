import socket

IP = "127.0.0.1"
PORT = 3514

#my_username = input("Username: ")

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((IP, PORT))


#send and receive message
while True:
    msg = input(":: ")

    client_socket.send(bytes(msg, 'utf-8'))
    print(client_socket.recv(1024).decode())

client_socket.close()

