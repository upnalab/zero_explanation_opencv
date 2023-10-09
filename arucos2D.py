import cv2
import cv2.aruco as aruco
 
cap = cv2.VideoCapture(0)

aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_100)
parameters = aruco.DetectorParameters_create()
cv2.startWindowThread()
 
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    corners, ids, rejectedImgPoints = aruco.detectMarkers(
            gray, aruco_dict, parameters=parameters)
    
    #ids contains the id of the detected arucos. 
    #corners their camera coordinates. 
    
    aruco.drawDetectedMarkers(frame, corners, ids)
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()