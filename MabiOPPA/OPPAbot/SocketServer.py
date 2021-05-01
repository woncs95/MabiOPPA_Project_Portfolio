import socket


IP="127.0.0.1"
PORT = 7070

#socket connection
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((IP, PORT))
s.listen()

def receive_message():
  while True:
    socketclient, adress = s.accept()
    print(f"{socketclient} is conncected in {adress}")
    socketclient.send(str.encode("hello"))
    try:
      data = string.decode(socketclient.recv(1024))
      return data
    except:
      return False