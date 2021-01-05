import socket

host=socket.gethostname()
s=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
s.bind((host,2207))
s.listen(1)
conn,addr = s.accept()

with open('yeawon.txt','wb') as f:
    while True:
        l = conn.recv(1024)
        if not l: break
        f.write(l)
s.close()
