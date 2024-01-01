import cv2 as cv
import numpy as np

img = cv.imread('./assets/photos/AdobeStock_611357913_Preview.jpeg')

roi = img[200:500, 300:750] # region of interest
img[100:400, 300:750] = roi


cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
