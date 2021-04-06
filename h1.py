import cv2
import numpy as np
import datetime

src = cv2.imread('bus0.png')
kernel = np.ones((5,5), np.uint8)
img = cv2.dilate(src, kernel, iterations = 1)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gaus = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(gaus,50,150,apertureSize = 3)

cv2.imshow('edges', edges)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

h, w = edges.shape
print(h, w)


t1 = datetime.datetime.now()
minLineLength = 150 
maxLineGap = 10
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180*1, threshold=5, minLineLength=minLineLength, maxLineGap=maxLineGap)

t2 = datetime.datetime.now()

delta = t2-t1
print(delta)

for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imwrite('houghlines.jpg',img)

cv2.imshow('lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


