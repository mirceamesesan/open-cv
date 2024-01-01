import cv2 as cv
import random

img = cv.imread('./assets/photos/AdobeStock_611357913_Preview.jpeg', -1) # 0 = grayscale, 1 = color, -1 = unchanged

img = cv.resize(img, (int(img.shape[1]), int(img.shape[0])))

for i in range(100,200):
    for j in range(img.shape[1]):
        red, green, blue = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        img[i][j] = [ blue, green, red ]

cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()


# video = cv.VideoCapture('assets/videos/AdobeStock_203290125_Video_HD_Preview.mov')