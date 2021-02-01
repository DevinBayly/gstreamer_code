import socket
import time 
import numpy as np
UDP_IP = "192.168.0.29"
UDP_PORT = 7000
sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
while True:
    rands = (np.random.random((2000))*255).astype("uint8")
    sock.sendto(f"{list(rands)}".encode(), (UDP_IP, UDP_PORT))
    time.sleep(1/20)
