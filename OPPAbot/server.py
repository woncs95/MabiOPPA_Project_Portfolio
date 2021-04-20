import socket
import select


HEADER_LENGTH = 1024
IP = ""
PORT = 1234


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((socket.gethostname(), 1234))
server_socket.listen()

sockets_list = [server_socket]

clients = {}

def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)

        if not len(message_header):
            return False

        message_length = int(message_header.strip())
        return {"header": message_header, "data": client_socket.recv(message_length)}

    except:
        return False

while True:
    read_sockets, _ = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_adress = server_socket.accept()

            user = receive_message(client_socket)
            if user is False:
                continue

                sockets_list.append(client_socket)

                clients[client_socket] = user

                print(f"Accepted new connection from {client_adress[0]}:{client_adress[1]} username:{user['data']}")

        else:
            message = receive_message(notified_socket)

            if message is false:
                print(f"Closed connection from {clients[notified_socket]['data']}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]
            print(f"Received message from {user['data']}:{message['data']}")