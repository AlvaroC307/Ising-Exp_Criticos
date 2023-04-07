""" from Medidas import *
from Montecarlo import *
import cv2

# DOXXEAR:

# create a VideoCapture object to capture video from the default camera (index 0)
cap = cv2.VideoCapture(0)

# check if camera is opened successfully
if not cap.isOpened():
    print("Error opening video capture")

# loop over frames from the video stream
while True:
    # read the next frame from the video stream
    ret, frame = cap.read()

    # check if frame is None (i.e., end of video stream)
    if frame is None:
        print("No frame captured, exiting...")
        break

    # display the frame in a window named "Webcam"
    cv2.imshow("Webcam", frame)

    # wait for a key press to exit
    if cv2.waitKey(1) == ord("q"):
        break

# release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows() """
