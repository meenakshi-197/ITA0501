import cv2

img = cv2.imread("input.jpg")

if img is None:
    print("Image not found")
else:
    img = cv2.resize(img, (500, 350))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    threshold_value = int(input("Enter threshold value: "))

    ret, output = cv2.threshold(
        gray, threshold_value, 255, cv2.THRESH_BINARY
    )

    cv2.imshow("Original Image", img)
    cv2.imshow("Segmented Image", output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
