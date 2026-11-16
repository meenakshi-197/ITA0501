import cv2
import numpy as np

width = int(input("Enter width: "))
height = int(input("Enter height: "))

img = np.ones((height, width, 3), dtype=np.uint8) * 255

box_w = width // 10
box_h = height // 10

img[0:box_h, 0:box_w] = [0, 0, 0]
img[0:box_h, width-box_w:width] = [255, 0, 0]
img[height-box_h:height, 0:box_w] = [0, 255, 0]
img[height-box_h:height, width-box_w:width] = [0, 0, 255]

cv2.imshow("Four Colored Boxes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
