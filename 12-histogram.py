import cv2 as cv
import matplotlib.pyplot as plt
# visulise the distribution of intensity of pixels

# img = cv.imread('images/lal.jpg')
img = cv.imread('images/lal-minar.jpeg')
cv.imshow('Car', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# grayscale histogram
# gray_hist = cv.calcHist(gray, [0], None, [256], [0,256])

# plt.figure()
# plt.title('Gray scale histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# color histogram
plt.figure()
plt.title('Color histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()


cv.waitKey(0)


