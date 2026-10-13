import cv2
import numpy as np

img = cv2.imread("input image.jpg")

if img is None:
    print("Image not found. Check the image path.")
else:
    original = img.copy()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    corners = cv2.cornerHarris(gray, 2, 3, 0.04)
    img[corners > 0.01 * corners.max()] = [0, 0, 255]

    original = cv2.resize(original, (500, 350))
    img = cv2.resize(img, (500, 350))

    cv2.imshow("Input Image", original)
    cv2.imshow("Harris Corner Detection Output", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
