import socket

IP = "193.122.125.86"
PORT = 1234
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) ##ipv4,tcp

async def receive_message():
    IP = "193.122.125.86"
    PORT = 1234
    async with s.connect((IP,PORT)) as sockets:

        while True:
            data = await sockets.recv()
            return data
