import socket
import time 

def send_wav() :
    #host=socket.gethostname()
    host=[]
    port=[]
    host.append("175.195.55.172")
    #host.append("165.194.35.5")
    #host.append("165.194.35.5")
    port.append(12123)
    #port.append(2201)
    #port.append(2202)
    for i in range(0,len(host)):
        s=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
        s.connect((host[i],port[i]))

        with open('piano.wav','rb') as f:
            for l in f : s.sendall(l)
        s.close()
send_wav()
