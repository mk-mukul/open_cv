import cv2 as cv

img = cv.imread('images/face.jpeg')
cv.imshow('Face', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Face', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number if faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow("Detected Faces", img)


cv.waitKey(0)




# Read video
capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)
    print(f'Number if faces found = {len(faces_rect)}')
    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), thickness=2)
    cv.imshow("Video", frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.distroyAllWindows()