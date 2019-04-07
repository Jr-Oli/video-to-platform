import socket
import pyexcel as p
import time

#Host/Port
HOST, PORT = "localhost", 3288
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
fileLocation = 't_r_accel.csv'
#Pull data from excel shet
FROM_SHEET = p.iget_records(file_name=fileLocation)

DATA = []
COUNTER = 0
#Fill an array with an array that contains each line from excel sheet
for coords in FROM_SHEET:
    DATA.append([coords['x'], coords['y'], coords['z'], coords['x0'], coords['y0'], coords['z0']])
    DATA[COUNTER][0] = round(DATA[COUNTER][0], 3)
    DATA[COUNTER][1] = round(DATA[COUNTER][1], 3)
    DATA[COUNTER][2] = round(DATA[COUNTER][2], 3)
    DATA[COUNTER][3] = round(DATA[COUNTER][3], 3)
    DATA[COUNTER][4] = round(DATA[COUNTER][4], 3)
    DATA[COUNTER][5] = round(DATA[COUNTER][5], 3)
    COUNTER += 1
for i in range(len(DATA)):
    #print(CHOSENDATA[i])
    sock.sendall(bytes(str(DATA[i]), "utf_8"))
    time.sleep(.3)

p.free_resources()
