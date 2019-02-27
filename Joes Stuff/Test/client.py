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
print("Number of entries: ", counter)
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
    
    #Uncomment for debugging purposes#
    #sock.sendall(bytes("Current platform position: " + str(data[0]) + "\n","utf_8"))
    #sock.sendall(bytes("Moving to position: " + str(data[1]) + "\n","utf_8"))
    #sock.sendall(bytes("Our platform needs to move it's X axis by " + str(newX) + " units. \n","utf_8"))
    #sock.sendall(bytes("Our platform needs to move it's Y axis by " + str(newY) + " units.\n","utf_8"))
    #sock.sendall(bytes("Our platform needs to move it's Z axis by " + str(newZ) + " units.\n","utf_8"))
    #sock.sendall(bytes("Our platform needs to move it's X0 axis by " + str(newX0) + " units.\n","utf_8"))
    #sock.sendall(bytes("Our platform needs to move it's Y0 axis by " + str(newY0) + " units.\n","utf_8"))
    #sock.sendall(bytes("Our platform needs to move it's Z0 axis by " + str(newZ0) + " units.\n","utf_8"))

    for x in data[0]:
        sock.sendall(bytes(str(x) +"\n","utf_8"))
p.free_resources()
