"""
Threshold là một hàm phân ngưỡng ảnh nhằm đưa ảnh về dạng nhị phân (đen và trắng, 0->255)
Ảnh nhị phân thường được dùng cho phân đoạn ảnh (segmentation)
> T -> 255 ngược lại là 0
"""
# Step 1: Convert BGR Image to Gray Image
# Step 2: Choose Threshold
import cv2

image = cv2.imread('saved_images\image.jpg')
cv2.imshow('color image', image)
cv2.waitKey()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray image', gray)
cv2.waitKey()

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# ret is real threshold
print('Threshold is:', ret)
print('Matrix binary image is:\n', thresh)
cv2.imshow('threshold image', thresh)
cv2.waitKey()

# may use Adaptive Threshold Function 
cv2.destroyAllWindows()