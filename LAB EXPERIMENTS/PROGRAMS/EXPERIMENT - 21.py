import cv2
import numpy as np

img = cv2.imread("input.jpg")

if img is None:
    print("Image not found")
else:
    img = cv2.resize(img, (500, 350))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((5, 5), np.uint8)

    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)

    cv2.imshow("Original Image", img)
    cv2.imshow("Opening Output", opening)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
