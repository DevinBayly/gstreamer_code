import socket
import time
from PIL import Image 
from io import BytesIO
import numpy as np


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.connect(('localhost',20001))

while True:
    data = s.recv(1024)
    if data != b'':
        print(data)
    time.sleep(1)

