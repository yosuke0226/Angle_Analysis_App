# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 21:39:19 2022

@author: emhl0
"""


import cv2
import time
from pylsd.lsd import lsd

import numpy as np

img = cv2.imread('gx01.jpg')
# img = cv2.resize(img,(int(img.shape[1]/5),int(img.shape[0]/5)))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray,(5,5),5)

t1 = time.time()
edges = cv2.Canny(gray,50,150,apertureSize = 3)
linesH = cv2.HoughLinesP(edges, rho=1, theta=np.pi/360, threshold=50, minLineLength=50, maxLineGap=10)
t2 = time.time()

linesL = lsd(gray)
t3 = time.time()

img2 = img.copy()
for line in linesH:
    x1, y1, x2, y2 = line[0]

    # 赤線を引く
    img2 = cv2.line(img2, (x1,y1), (x2,y2), (0,0,255), 3)

cv2.imwrite('samp_hagh.jpg',img2)
img3 = img.copy()
img4 = img.copy()
for line in linesL:
    x1, y1, x2, y2 = map(int,line[:4])
    img3 = cv2.line(img3, (x1,y1), (x2,y2), (0,0,255), 3)
    if (x2-x1)**2 + (y2-y1)**2 > 1000:
        # 赤線を引く
        img4 = cv2.line(img4, (x1,y1), (x2,y2), (0,0,255), 3)
print("Hagh")
print(len(linesH),"lines")
print(t2-t1,"sec")
print("time per a line :{:.4f}".format((t2-t1)/len(linesH)))
print("LSD")
print(len(linesL),"lines")
print(t3-t2,"sec")
print("time per a line {:.4f}".format((t3-t2)/len(linesL)))
cv2.imwrite('samp_pylsd.jpg',img3)
cv2.imwrite('samp_pylsd2.jpg',img4)