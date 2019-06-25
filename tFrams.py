#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 20:42:54 2019

@author: Emma
"""

import cv2

vc=cv2.VideoCapture("basketball.mp4")
c=1
if vc.isOpened():
    rval,frame=vc.read()
else:
    rval=False
while rval:
    rval,frame=vc.read()
    print('image/'+str(c)+'.jpg')
    cv2.imwrite('image/'+str(c)+'.png',frame)
    c=c+1
    cv2.waitKey(1)
vc.release()