#process the frames in ./calibFrames/ and computes the coefficients
import cv2
import numpy as np
import os
import glob

DIR_NAME = "calibFrames"

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

checkersW, checkersH = 9, 6
objp = np.zeros( (checkersW*checkersH, 3), np.float32)
objp[:,:2] = np.mgrid[0:checkersW,0:checkersH].T.reshape(-1,2)

#object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob(os.path.abspath(os.getcwd()) + '\\' + DIR_NAME + '\\*.jpg')

for file in images:
    img = cv2.imread(file)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    ret, corners = cv2.findChessboardCorners(gray, (checkersW, checkersH),None)

    if ret == True:
        objpoints.append( objp )
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)
        
        cv2.drawChessboardCorners(img, (checkersW, checkersH), corners2,ret)
        cv2.imshow('img',img)
        cv2.waitKey(100)

cv2.destroyAllWindows()


ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, 
                                                   imgpoints, 
                                                   gray.shape[::-1],None,None)

meanError = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i],imgpoints2, cv2.NORM_L2)/len(imgpoints2)
    meanError += error
meanError /= len(objpoints)

print ("Total error: ", meanError)
print("Camera matrix: ", mtx)
print("Distorsion coefficients: ", dist)

