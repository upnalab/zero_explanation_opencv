#shows the video feed in 4 windows with different components
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame = cap.read() 

cv2.namedWindow('red')
cv2.namedWindow('green')
cv2.namedWindow('blue')
cv2.namedWindow('grey')

while True:
    ret, frame = cap.read() 
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    red = np.copy( frame )
    red[:,:,0:2] = 0
    green = np.copy( frame )
    green[:,:,0] = 0
    green[:,:,2] = 0
    blue = np.copy( frame )
    blue[:,:,1:3] = 0
    
    
    cv2.imshow('grey', gray)
    cv2.imshow('red', red)
    cv2.imshow('green', green)
    cv2.imshow('blue', blue)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
