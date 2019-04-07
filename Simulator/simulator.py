import socket
import pyexcel as p
import time

#Host/Port
HOST, PORT = "localhost", 3288
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
fileLocation = 'translation_results.csv'
#Pull data from excel shet
FROM_SHEET = p.iget_records(file_name=fileLocation)

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

#Fills an array with only data that the user decides.
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

#Prompt user for their choice        
print("---------------------------------------------")
print("| Welcome to stewart platform simulator.    |")
print("| *Program assumes video is played at 30fps*|")
print("| Please make one of the following choices: |")
print("| 0=Max X                                   |")
print("| 1=Max Y                                   |")
print("| 2=Max Z                                   |")
print("| 3=Max X0                                  |")
print("| 4=Max Y0                                  |")
print("| 5=Max Z0                                  |")
print("---------------------------------------------")
try:
    userinput = int(input("Make your choice: "))
except ValueError:
    print("Please enter an integer")

#Pass user's choice into the data selector
CHOSENDATA = select_test_range(userinput)

print("Thank you, please standby.")
time.sleep(3)
print("Sending platform position @ 30fps:")

for i in range(len(CHOSENDATA)):
    #print(CHOSENDATA[i])
    sock.sendall(bytes(str(CHOSENDATA[i]), "utf_8"))
    time.sleep(.3)

p.free_resources()
