import cv2

img = cv2.imread("input.jpg")

if img is None:
    print("Image not found")
else:
    big = cv2.resize(img, (600, 600))
    small = cv2.resize(img, (200, 200))

    cv2.imshow("Original Image", img)
    cv2.imshow("Bigger Image", big)
    cv2.imshow("Smaller Image", small)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
