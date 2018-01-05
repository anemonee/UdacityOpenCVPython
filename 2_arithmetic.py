import numpy as np
import cv2
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

#adding images and multiplying by scalar
img1 = cv2.imread("bicycle.png", -1)    
img2 = cv2.imread("dolphin.png", -1)
imadd1 = cv2.add(img1,img2)
# blending
imadd = cv2.addWeighted(img1,0.15,img2,0.85,0)
cv2.imshow('imadd1',imadd1)
cv2.waitKey(3000)
cv2.imshow('imadd',imadd)
cv2.waitKey(3000)

img3 = (img1[:,:])
img3 = img3*3
print img3
cv2.imshow('img3',img3)
cv2.waitKey(5000)
