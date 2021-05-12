import socket
import asyncio
import time

IP="127.0.0.1"
PORT = 7070

#socket connection
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.settimeout(5)
s.bind((IP, PORT))
s.listen()

def receive_message():
    print("receiving")
    while socket.timeout:

            socket_client, adress = s.accept()
            print(f"{socket_client} is conncected in {adress}")
            socket_client.send("hello".encode('utf-8'))
            print("receiving data")
            data = socket_client.recv(100).decode('utf-8')
            print("data received")
            return data
    print("no data found")
    time.sleep(1)
