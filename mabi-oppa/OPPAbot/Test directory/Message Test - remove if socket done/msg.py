import socket

#IP = "217.160.61.235"
IP = "::"
PORT = 7070
s = socket.socket(socket.AF_INET6,socket.SOCK_STREAM) ##ipv4,tcp
s.connect((IP,PORT))
msg=s.recv(100)
print(msg.decode("utf-8"))
header="header"
data="Magus.run_counter.I like licking feet"
s.send(data.encode('utf-8'))
print(s.recv(100).decode("utf-8"))
