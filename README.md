# Onsites_Task5

##  multiple client chat application
This is a very basic chat application using tcp sockets in python.

To run this application, save the python files locally in the system and run them by:
python3 server_chat.py
python3 client_chat.py

If the client is run in a system different from that of server, change the ip address of the client_chat.py to that of the server.

#### Prerequisites:
Python 3.6 or greater
threading (inbuilt in python standard library)
sockets (inbuilt in python standard library)

Status:
Currently, there is a small problem with the server sending data to multiple clients when more than one clients join the application.
