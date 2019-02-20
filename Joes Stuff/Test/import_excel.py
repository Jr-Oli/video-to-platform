import pyexcel as p
import numpy as np
from new_position import find_x

from_sheet = p.iget_records(file_name='Test_Data1.csv')
data = []
counter = 0

for coords in from_sheet:
    data.append([coords['x'],coords['y'],coords['z'],coords['x0'],coords['y0'],coords['z0']])
    counter += 1 

newX = find_x(data[1][1],data[0][1])
print("Our table needs to move it's X axis by",newX)
p.free_resources()
