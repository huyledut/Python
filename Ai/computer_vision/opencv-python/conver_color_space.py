import cv2

# read the image
image = cv2.imread("D:\Dev\openvn-python\saved_images\image.jpg")
cv2.imshow("image", image)
cv2.waitKey()

# conver the color space (default is BGR)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# show image
cv2.imshow('image gray', image_gray)
cv2.waitKey()

# close all the windows
cv2.destroyAllWindows()
