import numpy as np
import cv2
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from PIL import Image
from scipy import signal



img = cv2.imread("tablet.png", -1)
print img.dtype
print img.shape
cv2.imshow('image',img)
cv2.waitKey(1000)


glyph = img[75:165,150:185]
cv2.imshow('glyph',glyph)
print glyph.shape
cv2.waitKey(1000)

x12 = cv2.matchTemplate(img,glyph,cv2.TM_CCORR_NORMED)
print x12.shape
print x12
value_max = np.argmax(x12)
print value_max
y, x = np.unravel_index(np.argmax(x12), x12.shape)  # find the match
print y,x

