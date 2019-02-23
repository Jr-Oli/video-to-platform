import pyexcel as p
import numpy as np
from new_position import find_movement
import socket
import sys
import time

#Host/Port
HOST, PORT = "localhost", 9999

from_sheet = p.iget_records(file_name='Test_Data1.csv')
data = []
counter = 0

for coords in from_sheet:
    data.append([coords['x'],coords['y'],coords['z'],coords['x0'],coords['y0'],coords['z0']])
    counter += 1 
print(data)
newX = round(find_movement(data[0][0],data[1][0]),2)
newY = round(find_movement(data[0][1],data[1][1]),2)
newZ = round(find_movement(data[0][2],data[1][2]),2)
newX0 = round(find_movement(data[0][3],data[1][3]),2)
newY0 = round(find_movement(data[0][4],data[1][4]),2)
newZ0 = round(find_movement(data[0][5],data[1][5]),2)

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes("Our table needs to move it's X axis by " + str(newX) + "\n","utf_8"))
    time.sleep(5)
    sock.sendall(bytes("Our table needs to move it's Y axis by " + str(newY) + "\n","utf_8"))
    sock.sendall(bytes("Our table needs to move it's Z axis by " + str(newZ) + "\n","utf_8"))
    sock.sendall(bytes("Our table needs to move it's X0 axis by " + str(newX0) + "\n","utf_8"))
    sock.sendall(bytes("Our table needs to move it's Y0 axis by " + str(newY0) + "\n","utf_8"))
    sock.sendall(bytes("Our table needs to move it's Z0 axis by " + str(newZ0) + "\n","utf_8"))

#print("Our table needs to move it's X axis by",round(newX,2))
#print("Our table needs to move it's Y axis by",round(newY,2))
#print("Our table needs to move it's Z axis by",round(newZ,2))
#print("Our table needs to move it's X0 axis by",round(newX0,2))
#print("Our table needs to move it's Y0 axis by",round(newY0,2))
#print("Our table needs to move it's Z0 axis by",round(newZ0,2))


p.free_resources()
