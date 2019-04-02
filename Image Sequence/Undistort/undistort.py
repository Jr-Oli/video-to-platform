import numpy as np
import cv2
import os, os.path


# copy parameters to arrays
K = np.array([[611.18384754, 0, 515.31108992], [0, 611.06728767, 402.07541332], [0, 0, 1]])
d = np.array([-0.36824145, 0.2848545, 0, 0, 0]) # just use first two terms (no translation)

# read one of your images
i = 1
while i < 11:
    img = cv2.imread('C:/Users/Joes Laptop/Desktop/video-to-platform/Image Sequence/Undistort/Distorted/'+ str(i) +'.png')
    h, w = img.shape[:2]

    # undistort
    newcamera, roi = cv2.getOptimalNewCameraMatrix(K, d, (w,h), 0) 
    newimg = cv2.undistort(img, K, d, None, newcamera)

    cv2.imwrite("Undistorted/undistorted"+str(i)+".png", newimg)
    i+=1