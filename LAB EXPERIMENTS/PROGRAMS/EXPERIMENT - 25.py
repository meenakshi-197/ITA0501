import cv2

image = cv2.imread("watch.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (9, 9), 2)

circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=50,
    param1=100,
    param2=50,
    minRadius=20,
    maxRadius=200
)

if circles is not None:
    circles = circles[0, :]

    for x, y, r in circles:
        x = int(x)
        y = int(y)
        r = int(r)

        cv2.circle(image, (x, y), r, (0, 255, 0), 2)
        cv2.putText(
            image,
            "Watch",
            (x - 40, y - r - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        break

image = cv2.resize(image, (640, 480))

cv2.imshow("Watch Recognition", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
