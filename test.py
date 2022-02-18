import socket
from co import *

ClientSocket = socket.socket()
host = '192.168.1.64'
port = 8081
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(r("Troubles with server!"))
    quit()
try:
    Response = ClientSocket.recv(1024)
except:
    pass
while True:
    i = input('Enter ticker: ').upper()
    try:
        ClientSocket.send(str.encode(i))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))
    except:
        print(r("Server stopped!"))
    if i == "quit":
        ClientSocket.send(str.encode("Client exit"))
        exit(1)
ClientSocket.close()