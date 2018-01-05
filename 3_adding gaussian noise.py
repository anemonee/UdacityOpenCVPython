import numpy as np
import cv2
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from PIL import Image

img0 = cv2.imread("saturn.png", -1)  
cv2.imshow('saturn',img0)
cv2.waitKey(6000)

row0,col0 = img0.shape
mean0 = 0 # gaussian mean BGR channels
sigma0 = 2 # gaussian sigma BGR channels
gaussian_noise0 = np.random.randn(row0,col0)*sigma0
noise_image0 = gaussian_noise0.astype(np.uint8)
print noise_image0.shape
cv2.imshow('noise0',noise_image0)
cv2.waitKey(6000)

img0_new = img0+noise_image0
cv2.imshow('img0_new',img0_new)
cv2.waitKey(6000)



img1 = cv2.imread("pic1.jpg", -1)  
cv2.imshow('img1',img1)
cv2.waitKey(6000)

row,col,ch = img1.shape
mean = 0 # gaussian mean BGR channels
sigma = 20 # gaussian sigma BGR channels
gaussian_noise = np.random.randn(row,col,ch)*sigma
noise_image = gaussian_noise.astype(np.uint8)
print noise_image.shape
noise_image_red = noise_image[:,:,0]
noise_image_green = noise_image[:,:,1]
noise_image_blue = noise_image[:,:,2]
noise = np.dstack([noise_image_red, noise_image_green, noise_image_blue])
cv2.imshow('noise',noise)
cv2.waitKey(6000)

img1_new = img1+noise
cv2.imshow('img1_new',img1_new)
cv2.waitKey(6000)


