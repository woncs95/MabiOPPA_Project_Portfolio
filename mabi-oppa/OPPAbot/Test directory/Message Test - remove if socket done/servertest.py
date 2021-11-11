import socket

IP="localhost"
PORT = 7070

#socket connection
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((IP, PORT))
s.listen()

while True:
    socket_client, adress = s.accept()
    print(f"{socket_client} is conncected in {adress}")
    socket_client.send(str.encode("hello"))
    print("receiving data")
    data = socket_client.recv(100).decode('utf-8')
    print("data received")
    print(data)