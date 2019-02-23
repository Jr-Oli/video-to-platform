import socket
import array as arr
UDP_IP = "35.50.3.93"
UDP_PORT = 2000
MESSAGE = arr.array('h', [-5,])
#MESSAGE  = -1
print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet, UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

