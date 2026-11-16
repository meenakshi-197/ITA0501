import cv2

video = cv2.VideoCapture("video1.mp4")

while True:
    ret, frame = video.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        if w > 30 and h > 10:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    frame = cv2.resize(frame, (640, 360))

    cv2.imshow("Text Detection", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
