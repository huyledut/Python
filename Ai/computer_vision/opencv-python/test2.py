import cv2
import imutils
from time import sleep

path = "videos/VID_1.mp4"
video = cv2.VideoCapture(path)
key = None
rotate = 0

while True:

    success, frame = video.read()

    if not success or key == ord('q'):
        video.release()
        cv2.destroyAllWindows()
        print("exited")
        break
    elif key == ord('l'):
        rotate = 90
    elif key == ord('r'):
        rotate = -90
    
    frame = imutils.rotate(frame, rotate)
    cv2.imshow('video', frame)
    sleep(0.1)
    key = cv2.waitKey(1)
        
