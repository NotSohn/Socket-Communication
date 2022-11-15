import socket

IP = "127.0.0.1"
PORT = 3514

server_socket = socket.socket()

# For now, since this is only going to be on a singular machine basis, we're going to keep the socket binded on the local host
server_socket.bind((IP,PORT))
server_socket.listen(3)

while True:
    c,address = server_socket.accept()
    print(' : ' + c.recv(1024).decode())

    while True:
        msg = input('::')
        c.send(bytes(msg,'utf-8'))
        print(' : ' + c.recv(1024).decode())

server_socket.close()


