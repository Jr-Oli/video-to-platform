import pyexcel as p
import numpy as np

from_sheet = p.iget_records(file_name='Test_Data1.csv')
data = []
counter = 0

print("Here is our total data set:")
for coords in from_sheet:
    print ("{[X:%s], [Y:%s], [Z:%s], [X0:%s], [Y0:%s], [Z0:%s]}" % (coords['x'],coords['y'],coords['z'],coords['x0'],coords['y0'],coords['z0']))
    counter += 1 
    data.append([coords['x'],coords['y'],coords['z'],coords['x0'],coords['y0'],coords['z0']])

#print(counter)
print("\n And here is our selected data set")
    
numpydata = np.array(data)
print(numpydata[1])


p.free_resources()
