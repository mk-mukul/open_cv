import cv2 as cv
import matplotlib.pyplot as plt
# visulise the distribution of intensity of pixels

img = cv.imread('images/car.jpg')
cv.imshow('Car', img)

# convert pixel to eithre 0 or i
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# simplw thresholding
threshold, thresh = cv.threshold(gray, 225, 255, cv.THRESH_BINARY)
cv.imshow("Threshold image", thresh)

# inverse thresholding
threshold, thresh_inv = cv.threshold(gray, 225, 255, cv.THRESH_BINARY_INV)
cv.imshow("Threshold inverse image", thresh_inv)

# adaptive thresholding
adaptive_thress = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 5)
cv.imshow("Adaptive threshold image", adaptive_thress)

cv.waitKey(0)


