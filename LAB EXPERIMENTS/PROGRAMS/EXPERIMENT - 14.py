import cv2
import numpy as np

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
else:
    rows, cols = img.shape[:2]

    pts1 = np.float32([[50, 50], [cols-50, 50],
                       [50, rows-50], [cols-50, rows-50]])

    pts2 = np.float32([[0, 0], [cols, 0],
                       [50, rows], [cols-50, rows]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    result = cv2.warpPerspective(img, matrix, (cols, rows))

    cv2.imshow("Original Image", img)
    cv2.imshow("Perspective Transformed Image", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
