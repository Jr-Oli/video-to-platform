import pyexcel as p
import numpy as np
from new_position import find_movement
import vlc

from_sheet = p.iget_records(file_name='Test_Data1.csv')
data = []
counter = 0

for coords in from_sheet:
    data.append([coords['x'],coords['y'],coords['z'],coords['x0'],coords['y0'],coords['z0']])
    counter += 1 
print(data)
newX = find_movement(data[0][0],data[1][0])
newY = find_movement(data[0][1],data[1][1])
newZ = find_movement(data[0][2],data[1][2])
newX0 = find_movement(data[0][3],data[1][3])
newY0 = find_movement(data[0][4],data[1][4])
newZ0 = find_movement(data[0][5],data[1][5])
print("Our table needs to move it's X axis by",round(newX,2))
print("Our table needs to move it's Y axis by",round(newY,2))
print("Our table needs to move it's Z axis by",round(newZ,2))
print("Our table needs to move it's X0 axis by",round(newX0,2))
print("Our table needs to move it's Y0 axis by",round(newY0,2))
print("Our table needs to move it's Z0 axis by",round(newZ0,2))

#Instance = vlc.Instance('--fullscreen')
#player = Instance.media_player_new()
#Media = Instance.media_new('D:/video-to-platform/Joes Stuff/Test/test_vid.mp4')
#Media.get_mrl()
#player.set_media(Media)
#player.play()

p.free_resources()
