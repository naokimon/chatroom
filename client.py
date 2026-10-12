import json
import socket as sock

PORT = 6767

def create_chat_user(tcp_ip: str, port: int, name: str):
    c = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

    c.connect((tcp_ip, port))

    response = c.recv(1024)
    print(response.decode())

    user_ip = sock.gethostbyname(sock.gethostname())

    join_message = {
        "type": "join",
        "name": name,
        "ip": user_ip
    }   

    join_data = json.dumps(join_message).encode("utf-8")

    c.sendall(join_data)

    while True:
        try:
            data = c.recv(1024)
        except ConnectionResetError:
            print("Server disconnected.")
            break
        print(data.decode())


host = sock.gethostname()
ip = sock.gethostbyname(host)
create_chat_user(ip, PORT, "naoki")

