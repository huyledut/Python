import cv2

image = cv2.imread('saved_images\image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('color image', image)
cv2.waitKey()

edge_image = cv2.Canny(image, threshold1=70, threshold2=150)
cv2.imshow('edge image', edge_image)
cv2.waitKey()

cv2.destroyAllWindows()
