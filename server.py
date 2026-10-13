import json
import socket as sock

PORT = 6767

def create_room_server():
    s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

    host = sock.gethostname()
    ip = sock.gethostbyname(host)

    s.bind((ip, PORT))

    s.listen()

    users = []

    while True:
        c, addr = s.accept()
        users.append(c)

        c.sendall(f"IP: {ip}".encode())

        join_data = c.recv(1024)

        for client in users:
            client.sendall(join_data)

        while True:
            try:
                chat_data = c.recv(1024)

                for client in users:
                    client.sendall(chat_data)
            except ConnectionResetError:
                print("Client has left")
                break

        c.close()


create_room_server()