import socket
import sys
from time import sleep

HOST, PORT = "localhost", 3288
data = "hello"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((HOST, PORT))
    sock.sendall(bytes(str(data), "utf_8"))
    received = sock.recv(1024)

    sleep(10)

    sock.sendall(bytes(str(data), "utf_8"))
    received = sock.recv(1024)

    sleep(10)

    sock.sendall(bytes(str(data), "utf_8"))
    received = sock.recv(1024)

finally:
    sock.close()