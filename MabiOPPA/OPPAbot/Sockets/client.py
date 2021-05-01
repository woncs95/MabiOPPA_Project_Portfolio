import socket


class Client():
    def __init__(self):
        self.host = 'localhost'
        self.port = 5000

        self.s = socket.socket()
        self.s.connect((self.host, self.port))
        self.s.send(str.encode(input("Echo this: ")))
        while True:
            data = self.s.recv(1024)
            if not data:
                break

            print("Message from server: " + data.decode("utf-8"))


x = Client()
