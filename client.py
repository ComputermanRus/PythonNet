import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "25.34.220.231"
port = 59980
s.connect((host, port))
while True:
    data = s.recv(1024)
    if data:
        print("Recieved: ", data)
s.close()