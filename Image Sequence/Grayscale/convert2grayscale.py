import cv2
import os, os.path

# path joining version for other paths
DIR = 'Colored/'
numFiles =  (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
print("There are: " + str(numFiles) + " files in the directory of "+str(DIR))
 
i = 1
while i < numFiles+1:
    image = cv2.imread('Colored/'+ str(i) +'.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("Grayscale/calib"+str(i)+".png", gray)
    i+=1