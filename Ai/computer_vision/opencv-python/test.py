import cv2

# image = cv2.imread("saved_images/image.jpg")
# cv2.imshow("original image", image)
# cv2.waitKey()

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray image", gray)
# cv2.waitKey()

# cv2.destroyAllWindows()
camera_id = 0
video = cv2.VideoCapture(camera_id)
key = None
while True:
    success, frame = video.read()
    print("Press q to exit")

    if not success or (key == ord('q')):    
        print("exiting")
        video.release()
        cv2.destroyAllWindows() 
        break

    cv2.imshow("original frame", frame)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray frame", frame)
    key = cv2.waitKey()

 