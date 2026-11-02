
import cv2

img = cv2.imread("input.jpg")

if img is None:
    print("Image not found")
else:
    img = cv2.resize(img, (500, 350))

    roi = img[50:150, 50:150]
    copied = roi.copy()

    output = img.copy()
    output[180:280, 300:400] = copied

    cv2.imshow("Original Image", img)
    cv2.imshow("Cropped ROI", roi)
    cv2.imshow("Copy and Paste Output", output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

