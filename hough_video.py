import cv2
import numpy as np
import datetime

cap = cv2.VideoCapture("TP-B004C1-20210325-070112-tracker.mp4")

while(True):
  ret, src = cap.read()
  kernel = np.ones((5,5), np.uint8)
  img = cv2.dilate(src, kernel, iterations = 1)

  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  gaus = cv2.GaussianBlur(gray, (5, 5), 0)
  edges = cv2.Canny(gaus,50,150,apertureSize = 3)

  #edges = cv2.dilate(edges, kernel, iterations = 1)


  #t1 = datetime.datetime.now()
  minLineLength = 180 
  maxLineGap = 5
  lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180*1, threshold=5, minLineLength=minLineLength, maxLineGap=maxLineGap)

  #t2 = datetime.datetime.now()

  #delta = t2-t1
  #print(delta)

  if lines is not None:
    for line in lines:
      for x1, y1, x2, y2 in line:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)


  cv2.imshow('lines', img)
  if cv2.waitKey(0) == ord('q'):
    break


cap.release()
cv2.destroyAllWindows()


