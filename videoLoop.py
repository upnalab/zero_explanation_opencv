#shows sequently frames from the camera
#generated by GPT3.5 "can you generate python code for opencv just a loop that reads one frame from the camera and shows it "
import cv2

# Open the default camera (usually camera index 0), you can use other indices for other devices
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() # Capture a frame from the camera

    cv2.imshow('Camera Feed', frame) # Display the captured frame in a window

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
