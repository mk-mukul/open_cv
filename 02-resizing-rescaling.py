import cv2 as cv

# funstion to change reaolution
# only work form live video
def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)


# function to resize
# Work for image,  videos and live videos
def rescaleFrame(frame, scale=0.9):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

# Resize image
img = cv.imread('images/lal-minar.jpeg')
resize_img = rescaleFrame(img, 0.10)
cv.imshow('Lal Minar', resize_img)
cv.waitKey(0)


# Resize video
capture = cv.VideoCapture('videos/diwali.mp4')
while True:
    isTrue, frame = capture.read()
    resize_frame = rescaleFrame(frame, 0.60)
    cv.imshow("Video", frame)
    cv.imshow("Video Resize", resize_frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.distroyAllWindows()


