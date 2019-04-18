import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "25.48.107.237"
port = 8888
s.bind((host, port))

s.listen(2)

conn, addr = s.accept()

data = conn.recv(1024)
if data:
    print(addr, data)
    conn.send(b"Read!")

z = input()

conn.close