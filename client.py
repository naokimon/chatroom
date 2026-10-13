import json
import socket as sock
import threading

PORT = 6767

def send_message(c: sock.socket, message: dict):
    msg_data = json.dumps(message).encode("utf-8") + b"\n"

    c.sendall(msg_data)

def receive_message(c: sock.socket):
    buffer = b""

    while True:
        data = c.recv(4096)

        if not data:
            break

        buffer += data

        while b"\n" in buffer:
            line, buffer = buffer.split(b"\n", 1)

            if not line:
                continue

            message = json.loads(line.decode("utf-8"))

            match message["type"]:
                case "message":
                    print(f"{message["name"]}: {message["message"]}")
                case "join":
                    print(f"{message["name"]} has joined the chatroom! ({message["ip"]})")


def create_chat_user(tcp_ip: str, port: int, name: str):
    c = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

    c.connect((tcp_ip, port))

    response = c.recv(1024)
    print(response.decode())

    user_ip = sock.gethostbyname(sock.gethostname())

    send_message(c,{
        "type": "join",
        "name": name,
        "ip": user_ip
    })

    receiver = threading.Thread(
        target=receive_message,
        args=(c,),
        daemon=True
    )

    receiver.start()

    try:
        while True:
            text = input()

            send_message(c, {
                "type": "message",
                "name": name,
                "message": text
            })
    except (OSError, EOFError):
        pass

    print("Leaving chatroom...")



host = sock.gethostname()
ip = sock.gethostbyname(host)
create_chat_user(ip, PORT, "naoki")

