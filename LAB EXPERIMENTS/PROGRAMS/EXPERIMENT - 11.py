
import cv2

img = cv2.imread("input.jpg")

if img is None:
    print("Image not found")
else:
    rotated = cv2.rotate(img, cv2.ROTATE_180)

    cv2.imshow("Original Image", img)
    cv2.imshow("180 Degree Rotated Image", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
