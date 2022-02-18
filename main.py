import socket
import os
from gfplib import *
from _thread import *
from co import *
ServerSocket = socket.socket()
host = ''
port = 8081
ThreadCount=0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(1000)

def gw(T):
    return T
def threaded_client(connection):
    connection.send(str.encode('Welcome to the Servern'))
    while True:
        try:
            data = connection.recv(2048)
            m=data.decode('utf-8')
            pri=ge(m)
            if str(m)=="quit":
                print(g("Server:")+"Client diconnected")

                print("===========================================")
                break
            print("Client ask price for:"+m)
            reply = g('Price '+m+":") + pri
            if not data:
                break
            connection.sendall(str.encode(reply))
        except:
            print("Client disconnected")
            break
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print(cy('Client address: ') + cy(address[0] + ':' + str(address[1])))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print(cy('Client id: ' + str(ThreadCount)))
    print(r(31*"-"))
ServerSocket.close()