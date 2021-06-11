import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 8877))
s.listen(1)

while True:
    conn, addr = s.accept()
    data = conn.recv(2048)
    conn.close()
    print(data)