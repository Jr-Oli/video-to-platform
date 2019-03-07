import socket
import pyexcel as p
from new_position import find_movement
from threading import Timer
import time

print (os.path.abspath(os.curdir))

#Host/Port
HOST, PORT = "localhost", 9999

#Pull data from excel shet
FROM_SHEET = p.iget_records(file_name='Sim_Test_Data.xlsx')

DATA = []
CHOSENDATA = []
COUNTER = 0
#Fill an array with an array that contains each line from excel sheet
for coords in FROM_SHEET:
    DATA.append([coords['x'], coords['y'], coords['z'], coords['x0'], coords['y0'], coords['z0']])
    DATA[COUNTER][0] = round(DATA[COUNTER][0], 2)
    DATA[COUNTER][1] = round(DATA[COUNTER][1], 2)
    DATA[COUNTER][2] = round(DATA[COUNTER][2], 2)
    DATA[COUNTER][3] = round(DATA[COUNTER][3], 2)
    DATA[COUNTER][4] = round(DATA[COUNTER][4], 2)
    DATA[COUNTER][5] = round(DATA[COUNTER][5], 2)
    COUNTER += 1

def select_test_range(choice):
    if choice == 0:
        SELECTEDDATA = DATA[0:202]
        return SELECTEDDATA
    elif choice == 1:
        SELECTEDDATA = DATA[203:403]
        return SELECTEDDATA
    elif choice == 2:
        SELECTEDDATA = DATA[404:604]
        return SELECTEDDATA
    elif choice == 3:
        SELECTEDDATA = DATA[605:805]
        return SELECTEDDATA 
    elif choice == 4:
        SELECTEDDATA = DATA[806:1006]
        return SELECTEDDATA
    elif choice == 5:
        SELECTEDDATA = DATA[1007:1207]
        return SELECTEDDATA
    else:
        print("Please input a correct choice.")
print("---------------------------------------------")
print("| Welcome to stewart platform simulator.    |")
print("| Please make one of the following choices: |")
print("| 0=Max X                                   |")
print("| 1=Max Y                                   |")
print("| 2=Max Z                                   |")
print("| 3=Max X0                                  |")
print("| 4=Max Y0                                  |")
print("| 5=Max Z0                                  |")
print("---------------------------------------------")
userinput = input("Make your choice:")



#print("Number of entries: ", COUNTER)
#print(DATA)

#Not needed if not sending individual movements
#NEWX = find_movement(DATA[0][0], DATA[1][0])
#NEWY = find_movement(DATA[0][1], DATA[1][1])
#NEWZ = find_movement(DATA[0][2], DATA[1][2])
#NEWX0 = find_movement(DATA[0][3], DATA[1][3])
#NEWY0 = find_movement(DATA[0][4], DATA[1][4])
#NEWZ0 = find_movement(DATA[0][5], DATA[1][5])



# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send DATA
    sock.connect((HOST, PORT))

    #Uncomment for debugging purposes#
    #sock.sendall(bytes("Current platform position: " + str(DATA[0]) + "\n","utf_8"))
    #sock.sendall(bytes("Moving to position: " + str(DATA[1]) + "\n","utf_8"))
    #sock.sendall(bytes("Our platform needs to move it's X axis by " + str(NEWX) + " units. \n","utf_8"))
    #sock.sendall(bytes("Our platform needs to move it's Y axis by " + str(NEWY) + " units.\n","utf_8"))
    #sock.sendall(bytes("Our platform needs to move it's Z axis by " + str(NEWZ) + " units.\n","utf_8"))
    #sock.sendall(bytes("Our platform needs to move it's X0 axis by " + str(NEWX0) + " units.\n","utf_8"))
    #sock.sendall(bytes("Our platform needs to move it's Y0 axis by " + str(NEWY0) + " units.\n","utf_8"))
    #sock.sendall(bytes("Our platform needs to move it's Z0 axis by " + str(NEWZ0) + " units.\n","utf_8"))


    #for i in range(len(DATA)):

        #Socket
        #sock.sendall(bytes(str(DATA[i]) +"\n", "utf_8"))
        #print(DATA[i])
        #time.sleep(.3)

    #ser.close()

    #for x in DATA[0]:
        #sock.sendall(bytes(str(x) +"\n", "utf_8"))
p.free_resources()
