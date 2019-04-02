import numpy as np
import cv2

rms = 0.17324999326972687

# copy parameters to arrays
# K = Camera Matrix
K = np.array([[611.1173635, 0, 515.31108992], [0, 611.06728767, 402.07541332], [0, 0, 1]])
# d = Distortion Coefficients
d = np.array([-0.36824145, 0.2848545, 0, 0, 0])

# read one of your images
img = cv2.imread("Distorted/scene1.png")
h, w , c = img.shape

print("Img height: "+ str(h))
print("Img width: "+ str(w))
print("Img channels: "+ str(c) + "\n")

# undistort
newcamera, roi = cv2.getOptimalNewCameraMatrix(K, d, (w,h), 0) 
newimg = cv2.undistort(img, K, d, None, newcamera)

print(newcamera)
