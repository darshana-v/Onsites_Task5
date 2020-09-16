#!/usr/bin/python3
import os
import socket
import threading
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
buffer = 4096
port = 1234
ip = socket.gethostbyname(socket.gethostname())
print("CLIENT SERVER STARTED!")

try:
    s.connect((ip, port))
    print("Connected to the server!")
except:
    print("Could not connect!")
s.setblocking(False)

# if you want to get the username of the user from their system
# name = os.environ.get('USERNAME')
name = input("Enter your username:")

# Sending the username of the client to the server
s.send(name.encode('utf-8'))
print("To exit the application, enter '[exit]'.")

def send_msg():
    while True:
        msg = input(str())
        msg = "<" + name + ">: " + msg
        s.send(msg.encode())

        if msg == '[exit]':
            Msg = "Left the chat room"
            s.send(Msg.encode())
            s.close()
            sys.exit()


def recv_msg():
    while True:
        try:
            message = s.recv(buffer)
            #if not message:
            #    sys.exit()
            msg = message.decode()
            print(msg)
        except:
            pass


# Send and receive messages continuously
t = threading.Thread(target=recv_msg())
t.start()
send_msg()
