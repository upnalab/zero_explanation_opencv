import cv2
import cv2.aruco as aruco
import numpy as np

#obtained with camera calibration
mtx = np.array([[642.41,0.,303.28],[0.,640.85,220.05],[0.,0.,1.]])
dist = np.array([[ 0.00213435,0.33666433,-0.00879525,-0.01382496, -1.43408673]])

MARKER_SIZE = 0.03 #3cm adjust

cap = cv2.VideoCapture(0)

dictionary = aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100)
parameters =  aruco.DetectorParameters()
detector = aruco.ArucoDetector(dictionary, parameters)

cv2.startWindowThread()

while(True):
    ret, frame = cap.read() 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    corners, ids, rejectedImgPoints = aruco.detectMarkers(
            gray, dictionary, parameters=parameters)
    
    gray = aruco.drawDetectedMarkers(gray, corners, ids)
    cv2.imshow('frame',gray)
    
    
    rvecs, tvecs, _objPoints = aruco.estimatePoseSingleMarkers(corners, 
                                                               MARKER_SIZE, 
                                                               mtx, 
                                                               dist)
    #tvecs and rvecs are 3D in respect to the camera
    if (rvecs is not None) and (tvecs is not None):
        print("Positions ", tvecs, " rotations ", rvecs)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
