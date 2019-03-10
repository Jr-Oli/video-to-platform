#!/usr/bin/env python

'''
example to show optical flow

USAGE: opt_flow.py [<video_source>]

Keys:
 1 - toggle HSV flow visualization
 2 - toggle glitch

Keys:
    ESC    - exit
'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2 as cv
import video
import math


def draw_flow(img, flow, step=16):
    global arrows
    
    h, w = img.shape[:2]
    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
    fx, fy = flow[y,x].T
    lines = np.vstack([x, y, x+fx, y+fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)
    vis = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    cv.polylines(vis, lines, 0, (0, 255, 0))
    for (x1, y1), (_x2, _y2) in lines:
        arrows.append([x1,y1, _x2, _y2, math.sqrt((_x2-x1)*(_x2-x1) + (_y2-y1)*(_y2-y1)), math.degrees(math.atan2(_x2-x1, _y2-y1)) ])
        cv.circle(vis, (x1, y1), 1, (0, 255, 0), -1)
    return vis


def draw_hsv(flow):
    h, w = flow.shape[:2]
    fx, fy = flow[:,:,0], flow[:,:,1]
    ang = np.arctan2(fy, fx) + np.pi
    v = np.sqrt(fx*fx+fy*fy)
    hsv = np.zeros((h, w, 3), np.uint8)
    hsv[...,0] = ang*(180/np.pi/2)
    hsv[...,1] = 255
    hsv[...,2] = np.minimum(v*4, 255)
    bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
    return bgr


def warp_flow(img, flow):
    h, w = flow.shape[:2]
    flow = -flow
    flow[:,:,0] += np.arange(w)
    flow[:,:,1] += np.arange(h)[:,np.newaxis]
    res = cv.remap(img, flow, None, cv.INTER_LINEAR)
    return res

if __name__ == '__main__':
    import sys
    print(__doc__)
    try:
        fn = sys.argv[1]
    except IndexError:
        fn = 0

    arrows = []
    cam = video.create_capture(fn)
    ret, prev = cam.read()
    prevgray = cv.cvtColor(prev, cv.COLOR_BGR2GRAY)
    show_hsv = False
    show_glitch = False
    cur_glitch = prev.copy()

    frameCounter = 0
    
    while True:
        
        frameCounter += 1
        print('Frame ' + str(frameCounter) + '/n')
        
        ret, img = cam.read()
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        flow = cv.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        prevgray = gray

        cv.imshow('flow', draw_flow(gray, flow))
        if show_hsv:
            cv.imshow('flow HSV', draw_hsv(flow))
        if show_glitch:
            cur_glitch = warp_flow(cur_glitch, flow)
            cv.imshow('glitch', cur_glitch)

        arrows.clear()
        finalImg = draw_flow(gray,flow)
        
        print(arrows[0])
        
        arrowCounter = 0
        
        '''
        for [x1, y1, _x2, _y2, length] in arrows : 
            arrowCounter += 1
            if length != 0:
                print('Arrow number ' + str(arrowCounter) + ' start ' + '[' + str(x1) + ',' + str(y1) + ']')
                print('Arrow number ' + str(arrowCounter) + ' end ' + '[' + str(_x2) + ',' + str(_y2) + ']')
                print('Angle of the Dangle: ' + str(math.degrees(math.atan2(_x2-x1, _y2-y1))))
                print('Length ' + str(length))
        '''
            
        
        ch = cv.waitKey(5000)
        if ch == 27:
            
            #print(arrows)
            #for arrow in arrows: print(arrow[0])
            break
        if ch == ord('1'):
            show_hsv = not show_hsv
            print('HSV flow visualization is', ['off', 'on'][show_hsv])
        if ch == ord('2'):
            show_glitch = not show_glitch
            if show_glitch:
                cur_glitch = img.copy()
            print('glitch is', ['off', 'on'][show_glitch])
    #print(arrows[0])
    cv.destroyAllWindows()