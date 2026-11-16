import cv2

img = cv2.imread("human.jpg")

if img is None:
    print("Image not found")
else:
    img = cv2.resize(img, (500, 350))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    eye = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml"
    )

    faces = face.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=6,
        minSize=(80, 80)
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(
            img,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

        face_gray = gray[y:y+h, x:x+w]

        eye_region = face_gray[0:int(h*0.65), :]

        eyes = eye.detectMultiScale(
            eye_region,
            scaleFactor=1.1,
            minNeighbors=8,
            minSize=(20, 20)
        )

        for (ex, ey, ew, eh) in eyes:

            cv2.rectangle(
                img,
                (x+ex, y+ey),
                (x+ex+ew, y+ey+eh),
                (255, 0, 0),
                2
            )

    cv2.imshow("Eye Detection", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
