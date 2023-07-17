import socket 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 1235))
    s.sendall(b"hello")
    data = s.recv(1024)
    print(data)