import cv2

cap = cv2.VideoCapture("video.mp4")

frames = []

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frames.append(frame)

cap.release()

if len(frames) == 0:
    print("Video not found")
else:
    for frame in reversed(frames):
        frame = cv2.resize(frame, (500, 350))

        cv2.imshow("Reverse Slow Motion", frame)

        if cv2.waitKey(150) & 0xFF == 27:
            break

    cv2.destroyAllWindows()
