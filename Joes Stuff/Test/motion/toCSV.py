#!/usr/bin/env python

import csv

#Clears out the sheet for a new set of data

def coorTruncate():
    with open('coordinates.csv', mode='w', newline='') as coordinatesFile:
        coordinatesFile.truncate()
        coorWriter = csv.writer(coordinatesFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        coorWriter.writerow(['x', 'y', 'z', 'x0', 'y0', 'z0'])

#Writes to row for each frame of data
#Vector contents, x1, y1, x2, y2, length, angle
def coorWrite(vector):
    with open('coordinates.csv', mode='a', newline='') as coordinatesFile:
        coorWriter = csv.writer(coordinatesFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        coorWriter.writerow([(vector[2] - vector[0]), (vector[3] - vector[1]), 0,0,0,0])