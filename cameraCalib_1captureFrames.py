#capture images as Space is pressed
import cv2
import os
import glob
 
DIR_NAME = "calibFrames"

if not os.path.exists(DIR_NAME):
    os.makedirs(DIR_NAME)    
    
path = "./" + DIR_NAME + "/"
nImages = len( glob.glob(path + '\\*.jpg') )

cv2.namedWindow('camera')
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_text = gray.copy()
    gray_text = cv2.putText(gray_text, 'Frames saved: ' + str(nImages) + 
                            ' - Space to capture, ESC to exit', (10,30),
                            cv2.FONT_ITALIC, 0.5, (0,0,255), 1, cv2.LINE_AA)
    
    cv2.imshow('camera', gray_text)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q') or key == 27: #q or ESC
        break
    elif key == 32:  #Space bar to capture image
        nImages += 1
        targetFile = path + '/' + str(nImages) + '.jpg'
        print("Saving at: ", targetFile)
        cv2.imwrite(targetFile, gray)
        
# # When everything done, release the capture
cv2.destroyAllWindows()