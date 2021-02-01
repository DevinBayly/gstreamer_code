import socket
 
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024
 
# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
 
print("waitig for message") 
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
 
msg = "Message from Server {}".format(msgFromServer[0])
print(msg)
