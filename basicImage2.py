#adds 1 line per frame to the shown result
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame = cap.read() 
h,w,c = frame.shape

image = np.zeros((h, w, 3), dtype=np.uint8)
x = 0

while True:
    ret, frame = cap.read() 
   
    x += 1
    if x >= w-1:
        x = 0
    
    image[:, x:-1, :] = frame[:, x:-1, :]
    image[:, x+1, :] = [255, 0, 0]
    
    cv2.imshow('Img', image) # Display the captured frame in a window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
