import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "25.34.220.231"
port = 51477
s.connect((host, port))
s.send(b'Are you achuel?')
data = s.recv(1024)
if data:
    print("Recieved: ", data)
z = input()
s.close()