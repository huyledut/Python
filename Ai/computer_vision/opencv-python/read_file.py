from cv2 import cv2


def read_img(path, **kwargs):
    # Read
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    # Size
    print("Old size: ", image.shape)
    if "size" in kwargs.keys():
        image = cv2.resize(image, kwargs["size"], interpolation=cv2.INTER_AREA)

    # Show
    cv2.imshow("My Picture 1: ", image)

    # Save image
    cv2.imwrite("saved_images/image.jpg", image)

    # Pause Screen
    cv2.waitKey()

    # Close all window
    cv2.destroyAllWindows()

