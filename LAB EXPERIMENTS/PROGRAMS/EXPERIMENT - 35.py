import cv2

img = cv2.imread("input.jpg")

if img is None:
    print("Image not found")
else:
    img = cv2.resize(img, (500, 350))

    text = input("Enter text: ")

    cv2.putText(img, text, (30, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    cv2.imshow("Text on Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
