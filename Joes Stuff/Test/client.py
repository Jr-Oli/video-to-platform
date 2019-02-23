import socket
import sys

HOST, PORT = "localhost", 9999
data = "We are here".join(sys.argv[1:])
data1 = "We are here1"
data2 = "We are here2"
# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data1 + "\n", "utf-8"))
    sock.sendall(bytes(data2 + "\n", "utf-8"))
