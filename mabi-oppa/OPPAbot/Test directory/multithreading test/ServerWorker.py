import socket
import asyncio
import time
from threading import Thread


IP="::"
PORT = 7070

# socket connection
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((IP, PORT))
s.listen()


def receive_message():
    #print("receiving")
    #print("start time: " + time.ctime(time.time()))
    try:
        socket_client, adress = s.accept()
        #print("client accepted: " + time.ctime(time.time()))
        print(f"{socket_client} is conncected in {adress}")
        socket_client.send("hello".encode('utf-8'))
        #print("send hello to client" + time.ctime(time.time()))
        #print("receiving data")
        data = socket_client.recv(256).decode('utf-8')
        #print("server receive data from client time" + time.ctime(time.time()))
        socket_client.send("thank you".encode('utf-8'))
        #print("data received")
        #print("end loop" + time.ctime(time.time()))
        return data
    except:
        e=Exception
        print(e.args)
        return False


