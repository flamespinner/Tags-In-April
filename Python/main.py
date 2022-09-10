from charset_normalizer import detect
import cv2
import numpy as np
#from apriltag import apriltag

cam = cv2.VideoCapture(0) # 0 -> index of camera

#handle error
if not cam.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cam.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
    # Display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cam.release()
cv2.destroyAllWindows()