# kernel is basically the weight metric
# Circullay symmetric gaussian filter : Important - get to know and love
# Size of the kernel has to be big enough to accomodate the size of the sigma. #Size of the sigma is important.
#Parameters:	GaussianBlur
#ksize: It should be odd and positive.
#sigma :Gaussian standard deviation. If it is non-positive, it is computed #from ksize as sigma = 0.3*((ksize-1)*0.5 - 1) + 0.8 .

import numpy as np
import cv2
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from PIL import Image

img1 = cv2.imread("saturn.png", -1)  
cv2.imshow('img1',img1)
cv2.waitKey(6000)
print img1.shape

blur = cv2.GaussianBlur(img1,(9,9),0)
cv2.imshow('blur',blur)
cv2.waitKey(6000)


