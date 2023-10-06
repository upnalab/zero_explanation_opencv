#show the camera feed with a blur that can be controlled with a slider
import cv2

cap = cv2.VideoCapture(0)


cv2.namedWindow('sliders')
def nothing(x):
    pass
cv2.createTrackbar('blur size','sliders',8,255,nothing)


while(True):
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurSize = 1+cv2.getTrackbarPos('blur size','sliders')
    gray = cv2.blur(gray, (blurSize,blurSize))
    
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()