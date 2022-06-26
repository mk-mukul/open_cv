import cv2 as cv

# Read image
img = cv.imread('images/lal-minar.jpeg')
cv.imshow('Lal Minar', img)
cv.waitKey(0)


# Read video
capture = cv.VideoCapture('videos/diwali.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.distroyAllWindows()
