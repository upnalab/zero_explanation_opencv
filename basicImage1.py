#swaps two squares and changes their color from the frame
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() #frame is BGR instead of RGB
    
    # we operate with the frame as if it was a matrix
    h,w,c = frame.shape
    thirdW = int(w/3)
    thirdH = int(h/3)
    
    leftBlock = np.copy(frame[thirdH:thirdH*2, thirdW:thirdW*2, :] )
    rightBlock = np.copy(frame[thirdH:thirdH*2, thirdW*2:thirdW*3, :] )
    
    leftBlock[:,:,0:2] = 0 #keep only red channel
    rightBlock[:,:,1:3] = 0 #keep only only blue channel
    
    #put back the blocks swapped swapped
    frame[thirdH:thirdH*2, thirdW:thirdW*2, :] = rightBlock
    frame[thirdH:thirdH*2, thirdW*2:thirdW*3, :] = leftBlock
    
    cv2.imshow('Camera Feed', frame) # Display the captured frame in a window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
