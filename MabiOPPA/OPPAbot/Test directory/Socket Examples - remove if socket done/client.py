import socket


class Client():
    def __init__(self):
        self.host = 'localhost'
        self.port = 7070

        self.s = socket.socket()
        self.s.connect((self.host, self.port))

        while True:
            self.s.send(str.encode(input("Echo this: ")))
            data = self.s.recv(1024)
            #if not data:
                #break

            print("Message from server: " + data.decode("utf-8"))


x = Client()
