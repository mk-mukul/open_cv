import cv2 as cv

img = cv.imread('images/car.jpg')
cv.imshow('Car', img)

# averaging
average = cv.blur(img, (3,3))
cv.imshow("Average Blur", average)

# gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("Gaussina Blur", gauss)

# median blur
median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median)

# Bilateral Blurring
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("Bilateral Blur", bilateral)

cv.waitKey(0)