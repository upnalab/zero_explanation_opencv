#encircles the largest green contour on screen
#if 4 corner points have been defined by clicking (top-left, top-right, bottom-right, top-right)
#then the camera coords are transformed to world coords and shown on screen
import cv2
import numpy as np

WORLD_WIDTH = 800
WORLD_HEIGHT = 600
worldPoints = [[0,0],[WORLD_WIDTH,0],[WORLD_WIDTH,WORLD_HEIGHT],[0,WORLD_HEIGHT]]

cameraPoints = [] #top-left, top-right, bottom-right, bottom-left
def clickOnCamera(event, x, y, flags, param):
    global cameraPoints
    if event == cv2.EVENT_LBUTTONUP:
        if len(cameraPoints) >= 4:
            cameraPoints.clear()
        cameraPoints.append([x, y])
cv2.setMouseCallback("camera", clickOnCamera)
        
cv2.namedWindow("camera")
cv2.namedWindow("mask")
cv2.setMouseCallback("camera", clickOnCamera)


# define the lower and upper of "green" in the HSV color space
filterBottom = (55, 40, 95)
filterTop = (90, 110, 150)

cap = cv2.VideoCapture(0)        
while(True):
    ret, frame = cap.read()
    
    blurred = cv2.GaussianBlur(frame, (11, 11), 0) #blur
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV) #change to Hue Saturation V
    mask = cv2.inRange(hsv, filterBottom, filterTop) #binarize by Hue
    mask = cv2.erode(mask, None, iterations=2) #erode and dilate = closing
    mask = cv2.dilate(mask, None, iterations=2)
    
    cnts, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea) #get the largest contour
        ((x, y), radius) = cv2.minEnclosingCircle(c) 
        cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
        if len(cameraPoints) == 4:
            matrix = cv2.getPerspectiveTransform(np.float32(cameraPoints), np.float32(worldPoints))
            camPoint = np.array([[[x,y]]], dtype = "float32")
            worldPoint = cv2.perspectiveTransform(camPoint, matrix)
            wPointX = int(worldPoint[0,0,0])
            wPointY = int(worldPoint[0,0,1])
            print("blob detected at " + str(wPointX) + "," + str(wPointY))
                
    for p in cameraPoints:
        cv2.circle(frame, (p[0],p[1]), 3, (0,0,255), -1)
        
    cv2.imshow('camera',frame)
    cv2.imshow('mask', mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()