import socket
import time 
import numpy as np
UDP_IP = "localhost"
UDP_PORT = 20001
sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
from PIL import Image 
from io import BytesIO


while True:
    #print("sending")
    buf = BytesIO()
    rand = Image.fromarray(np.uint8(np.random.random((80,80,4))*255))
    rand.save(buf,format="png")
    buf.seek(0)
    sock.sendto(buf.read(), (UDP_IP, UDP_PORT))
    #print("sent")
    time.sleep(1)
    #print("done sleeping")
