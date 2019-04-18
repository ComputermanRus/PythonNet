import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "212.164.64.248"
port = 8888
s.connect((host, port))
s.send(b'Read?')
data = s.recv(1024)
if data:
    print("Получено:", data) 
z = input()
s.close()