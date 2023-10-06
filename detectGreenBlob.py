#encircles the largest green contour on screen
#click with the mouse to print HSV values and adjust your filter
import cv2


def clickOnCamera(event, x, y, flags, param):
    global hsv
    if event == cv2.EVENT_LBUTTONDOWN:
        print( hsv[y,x,:] )
        
cv2.namedWindow("camera")
cv2.namedWindow("mask")
cv2.setMouseCallback("camera", clickOnCamera)


# define the lower and upper of "green" in the HSV color space
filterBottom = (87, 200, 115)
filterTop = (93, 255, 160)

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
        #print( cv.contourArea(c) )
        #area = cv2.contourArea(contour)
        #perimeter = cv2.arcLength(contour, True)  # True means it's a closed contour
        #circularity = (4 * np.pi * area) / (perimeter * perimeter)
        ((x, y), radius) = cv2.minEnclosingCircle(c) 
        cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
       
    cv2.imshow('camera',frame)
    cv2.imshow('mask', mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()