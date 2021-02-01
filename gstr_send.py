import socket
import time 
import numpy as np
UDP_IP = "localhost"
UDP_PORT = 20001
sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
while True:
    rands = (np.random.random((2000))*255).astype("uint8")
    #print("sending")
    sock.sendto(f"{list(rands)}".encode(), (UDP_IP, UDP_PORT))
    #print("sent")
    time.sleep(1)
    #print("done sleeping")
