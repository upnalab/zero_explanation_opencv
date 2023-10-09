OpenCV snippets. No explanation, no understanding. No remorse, no regret.

## Create the environment with conda
Command+T or your preferred way for opening the terminal 

```console
conda create --name cvtest python=3.9
conda activate cvtest
pip install opencv-python
pip install matplotlib
```

Installing an IDE for editing the snippets (optional), it will take forever:
```console
pip install spyder
```

You can download this repo with:
```console
git clone https://github.com/upnalab/zero_explanation_opencv/
cd zero_explanation_opencv/
```

Now you can edit the snippets as:
```console
spyder nameOfSnippet.py &
```
Or just run them with: python nameOfSnippet.py

## Snippets

### videoLoop
Captures a frame from camera 0 and shows it on the screen repeatedly

### basicImage1
gets 2 blocks from the image swaps them and keeps only one color channel

### basicImage2
picks only 1 line at a time from the camera

### basicImage3
shows the camera feed split into 4 images: red, blue, green component and greyscale

### inputSliders
using a slider widget to adjust in runtime a parameter

### faceAndEyesHaar
simple face and eye detection using a pretrained haar xml file

### detectGreenBlob
you can print "color circles.pdf"
depending on light conditions you may need to move the circle around and click on it and get the range of HSV values
detects a green blob by Hue thresolding and contour detection

### detectGreenBlobWorldCoords
transforms from camera coordinates to a world coordinate system in a plane defined with 4 points.

### arucos2D
You can use the code genArucos.py to generate a PDF with the desired dictionary and number of arucos.


### cameraCalib
For working in 3D, camera calibration is required.

Run cameraCalib_1captureFrames to capture some frames of the calibration sheet from different angles. You can check the examples there to see how they are.

Run cameraCalib_2calcParams  to process the frames in ./calibFrames/.jpg and calculate the coefficients. It will output the undistorted frames in the same folder.

### arucos3D
uses the camera calibration parameters to provide position and rotation 3D vectors for the detected arucos

### handsMediapipe
Requires to run: pip install mediapipe
Minimum code to track the hands and draw their joints along their indices.

### yolov5
Ideally use another environment
Requires to run: pip install yolov5
and then: yolov5 detect
