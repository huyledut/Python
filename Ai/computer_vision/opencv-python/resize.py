import cv2
import imutils


# read the image
image = cv2.imread("D:\Dev\openvn-python\saved_images\image.jpg")
cv2.imshow("original image", image)
print("original image shape: ", image.shape)
cv2.waitKey()

# resize the image
image_resized = cv2.resize(image, (200, 100))
cv2.imshow("resized image", image_resized)
print("resized image shape: ", image_resized.shape)
cv2.waitKey()

# resize the image
image_resized_2 = cv2.resize(image, dsize=None, fx=0.5, fy=0.5)
cv2.imshow("resized image 2", image_resized_2)
print("resized image 2 shape: ", image_resized_2.shape)
cv2.waitKey()

# rotate the image: reotate 90 degrees clockwise
image_rotated = imutils.rotate(image, 90)
cv2.imshow("rotated image", image_rotated)
print("rotated image shape: ", image_rotated.shape)
cv2.waitKey()

# close all the windows
cv2.destroyAllWindows()