import numpy as np
import cv2
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
    
img = cv2.imread("dolphin.png")
print img.dtype
print img.shape
img1 = img[101:104,201:204]
imred = img[:,:,0]
imgreen = img[:,:,1]
imblue = img[:,:,2]
print img[100,50]

implot = np.array(imgreen[256,:])
implot1 = implot.tolist()
plt.plot(implot1)
plt.savefig("abc.png")

cv2.line(img,(1,480),(1280,480),(0,0,0),2)
cv2.imshow('image',img)
cv2.waitKey(1000)
cv2.imshow('imager',imred)
cv2.waitKey(1000)
cv2.imshow('imageg',imgreen)
cv2.waitKey(1000)
cv2.imshow('imageb',imblue)
cv2.waitKey(1000)



