import numpy as np
import cv2
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from PIL import Image
from scipy import ndimage

img1 = cv2.imread("van_gogh.png", -1)  
cv2.imshow('img1',img1)
cv2.waitKey(6000)
print img1.shape

im_med = ndimage.median_filter(img1, 3)
cv2.imshow('im_med',im_med)
cv2.waitKey(6000)

