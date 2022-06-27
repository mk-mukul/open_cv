import cv2 as cv

img = cv.imread('images/car.jpg')
cv.imshow('Car', img)

# convert image to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# blur a image
blur = cv.GaussianBlur(img,(7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny", canny)

#  dilating the image
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow("Dilated", dilated)

# edoding
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow("Eroded", eroded)

# resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# cropping
croped = img[50:200, 200:400]
cv.imshow('Croped', croped)

cv.waitKey(0)



