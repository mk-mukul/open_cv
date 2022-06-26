import cv2 as cv
import numpy as np

# make blank image
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow("Blank", blank)

# 1. paint the image a certain color
# blank[:] = 0,255,0
# cv.imshow("Green", blank)
# blank[200:300, 300:400] = 0,0,255
# cv.imshow("Red", blank)
# blank[:] = 255,0,0
# cv.imshow("Blue", blank)

# 2. draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[0]//2,blank.shape[1]//2), (0,255,0), thickness=-1)
cv.imshow("Rectangle", blank)

# 3. draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 80, (255, 0,0), thickness=-1)
cv.imshow("Circle", blank)

# 4. draw a line
cv.line(blank,  (100,60), (400,460), (255,255,255), thickness=3)
cv.imshow("Line", blank)

# 5. write text
cv.putText(blank, "Hello", (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow("Text", blank)

cv.waitKey(0)

