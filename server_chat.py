#!/usr/bin/python3
import socket
import sys
import threading

host = socket.gethostname()
port = 1234
buffer = 4096
socket_list = []
CLIENTS = {}


def accept_conn(conn):
    while True:
        msg = conn.recv(buffer)
        broadcast(conn, msg)


def broadcast(user, msg):
    print(msg.decode('utf-8'))
    for conn in socket_list:
        if conn != user:
            try:
                conn.send(msg)
            except:
                conn.close()
                socket_list.remove(conn)



try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print("Could not create socket. Error code: {} Error: {}".format(str(msg[0]), msg[1]))
    sys.exit()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip = socket.gethostbyname(host)
try:
    server_socket.bind((ip, port))
except socket.error as msg:
    print("Bind failed. Error code: {} Error: {}".format(str(msg[0]), msg[1]))
    sys.exit()

socket_list = [server_socket]
server_socket.listen(200)
print("Server is waiting for connections!")
while True:
    conn, addr = server_socket.accept()
    client_name = conn.recv(buffer)
    conn.send("You have joined the chatroom!".encode())
    socket_list.append(conn)
    CLIENTS[conn] = client_name

    print("%s has connected." % client_name)
    broadcast(conn, "A new user has joined the chatroom!".encode())

    clients_accept = threading.Thread(target=accept_conn, args=(conn,))
    clients_accept.start()

