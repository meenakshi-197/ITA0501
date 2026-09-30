import cv2
import matplotlib.pyplot as plt

image = cv2.imread("image.jpg")

if image is None:
    print("Image not found!")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    equalized = cv2.equalizeHist(gray)

    cv2.imshow("Grayscale Image", gray)
    cv2.imshow("Histogram Equalized Image", equalized)

    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.hist(gray.ravel(), 256, [0, 256])
    plt.title("Original Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

    plt.subplot(1, 2, 2)
    plt.hist(equalized.ravel(), 256, [0, 256])
    plt.title("Equalized Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
