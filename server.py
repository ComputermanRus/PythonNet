import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "25.34.220.231"
port = 59980
s.bind((host, port))
s.listen(1)
cs = []
for i in range(1):О
    clnt, addr = s.accept()
    clnt.setblocking(0)
    cs.append(clnt)

while True:
    if len(cs) != 0:
        for c in cs:
            c.send(b"MESSAGE!")
            print(b"Sended!")