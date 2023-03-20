import cv2
from time import sleep


def read_img_from_cam(camera_id, **kwargs):

    # May be read file from path
    if "path" in kwargs:
        cap = cv2.VideoCapture(kwargs["path"])
    elif "camera_id" in kwargs:
        cap = cv2.VideoCapture(camera_id)
    else:
        # Default camera
        cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        success, frame = cap.read()

        # Press Q on keyboard to exit or read image fail
        if not success or (cv2.waitKey(1) & 0xFF == ord('q')):
            print("Exiting Program")   
            cap.release()
            cv2.destroyAllWindows()
            break
        
        # Show size of frame
        # (height, width, color_channel) = frame.shape[:2]
        print("Size of picture", frame.shape)

        # Show image
        cv2.imshow(f"My Picture from camera_id {camera_id}:", frame)

        # Save image
        cv2.imwrite("saved_images/image.jpg", frame)

        print("Press q to exit")

        # Sleep for func
        if "sleep" in kwargs:
            # Sleep for 5 second
            sleep(kwargs["sleep"])    
