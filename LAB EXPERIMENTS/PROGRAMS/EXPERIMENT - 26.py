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
    height, width, _ = frames[0].shape

    out = cv2.VideoWriter(
        "reverse_video.mp4",
        cv2.VideoWriter_fourcc(*"mp4v"),
        20,
        (width, height)
    )

    for frame in reversed(frames):
        out.write(frame)

        display = cv2.resize(frame, (500, 350))
        cv2.imshow("Reverse Video", display)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    out.release()
    cv2.destroyAllWindows()

    print("Reverse video created successfully")
