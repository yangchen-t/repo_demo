import socket 
import threading


def handle_client(c,addr):
        print(addr, "connected.")
        while True:
            data = c.recv(1024)
            if not data:
                break
            c.sendall(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0",1235))
    s.listen()

    while True:
        c, addr = s.accept()

        t = threading.Thread(target=handle_client, args=(c, addr)).start