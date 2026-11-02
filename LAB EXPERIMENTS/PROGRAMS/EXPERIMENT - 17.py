import cv2

img = cv2.imread("input.jpg")

if img is None:
    print("Image not found")
else:
    img = cv2.resize(img, (500, 350))
    watermarked = img.copy()

    cv2.putText(watermarked, "WATERMARK",
                (50, 320),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 255, 255), 2)

    cv2.imshow("Original Image", img)
    cv2.imshow("Watermarked Image", watermarked)

    cv2.imwrite("watermarked.jpg", watermarked)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
