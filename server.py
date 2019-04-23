import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "25.34.220.231"
port = 51477
s.bind((host, port))
s.listen(2)
conn, addr = s.accept()
data = conn.recv(1024)
if data:
    print(addr, data)
    conn.send(b"Read!")
z = input()
conn.close