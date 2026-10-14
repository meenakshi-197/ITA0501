import cv2
import matplotlib.pyplot as plt

img = cv2.imread("input.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

colors = ('b', 'g', 'r')

plt.figure(figsize=(10, 5))

for i, color in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)

plt.title("Color Histogram")
plt.xlabel("Color Intensity Level")
plt.ylabel("Number of Pixels")
plt.xlim([0, 256])
plt.grid()
plt.show()

plt.imshow(img_rgb)
plt.title("Input Image")
plt.axis("off")
plt.show()
