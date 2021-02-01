import socket
import time
from PIL import Image 
from io import BytesIO
import numpy as np


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind(('localhost',20001))
s.listen(1)

conn,addr = s.accept()

try:
    while True:
        print("going")
        time.sleep(1)
        buf = BytesIO()
        rand = Image.fromarray(np.uint8(np.random.random((800,800,3))*255))
        rand.save(buf,format="jpeg")
        buf.seek(0)
        ## send parts
        total =0 
        bytes_to_send = buf.read()
        while total < len(bytes_to_send):
            sent = conn.send(bytes_to_send[total:])
            if sent == 0:
                print("no more to send")
                break
            total+=sent
            print('sent ',sent,'bytes','total is',total)
        print("end of loop")
except Exception as e:
    print(e)
    conn.close()
    s.close()


print("done")
