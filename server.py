import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "25.34.220.231"
port = 59980
s.bind((host, port))
s.listen(2)
cs = []
for i in range(2):
    clnt, addr = s.accept()
    clnt.setblocking(0)
    cs.append(clnt)

while True:
    if len(cs) != 0:
        for c in cs:
            c.send(b"СООБЩЕНИЕ!")