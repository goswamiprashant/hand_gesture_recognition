# concept of convex hull
import cv2
import numpy as np
hand=cv2.imread("Capture.png",0)

ret,the=cv2.threshold(hand,127,255,cv2.THRESH_BINARY)

contours,_ =cv2.findContours(the.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

hull=[cv2.convexHull(c) for c in contours ]

final=cv2.drawContours(hand,hull,-1,(255,0,0))

cv2.imshow("Original",hand)
cv2.imshow("Thresh",the)
cv2.imshow("Convex Hull",final)


cv2.waitKey(0)
cv2.destroyAllWindows()




#--------------------------------------------------------------------------------------------------------------------------------

cv2.imshow("Erosion",erosion)
cv2.waitKey(0)

cv2.imshow("Dilate",dilation)
cv2.waitKey(0)

cv2.imshow("webcam0",mask)
cv2.waitKey(0)
cv2.imshow("webcam1",hsv)
cv2.waitKey(0)
cv2.imshow("Webcam",crop)
cv2.imshow("Webcam",blur)
cv2.waitKey(0)