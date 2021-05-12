#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 21:11:40 2021

@author: sherin
"""

import pytesseract
import cv2
import matplotlib.pyplot as plt
#reading image
img = cv2.imread("/home/sherin/Downloads/samtes.jpg") 
#showing image
#plt.imshow(img)
#converting image to text
img2char = pytesseract.image_to_string(img)
#print text from that image
print(img2char)
imgbox = pytesseract.image_to_boxes(img)
print(imgbox)
imgH, imgW,_ = img.shape
for boxes in imgbox.splitlines():
    boxes = boxes.split(' ')
    x,y,w,h = int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
    cv2.rectangle(img, (x,imgH-y), (w,imgH-h), (0,0,255),3)
plt.imshow(img)   
#from video and webcam
import numpy as np
font_scale = 1.5
font = cv2.FONT_HERSHEY_PLAIN
#cap = cv2.VideCapture("/home/sherin/Downloads/video1.mp4")
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("cannot open webcam")
cntr =0;
while True:
    ret,frame = cap.read()
    #cntr = cntr+1;
    #if((cntr%20)==0):
    imgH, imgW,_ = frame.shape
    x1,y1,w1,h1 = 0,0,imgH,imgW
    imgchar = pytesseract.image_to_string(frame)
    imgboxes = pytesseract.image_to_boxes(frame)
    for boxes in imgboxes.splitlines():
        boxes = boxes.split(' ')
        x,y,w,h = int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
        cv2.rectangle(frame, (x,imgH-y), (w,imgH-h), (0,0,255),3)
        cv2.putText(frame, imgchar, (x1 + int(w1/50),y1 + int(h1/50)), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        cv2.imshow('text detection tutorial',frame)
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
        