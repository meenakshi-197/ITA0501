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

    smile = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_smile.xml"
    )

    faces = face.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        roi = gray[y:y+h, x:x+w]

        smiles = smile.detectMultiScale(
            roi, 1.7, 20
        )

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(
                img,
                (x+sx, y+sy),
                (x+sx+sw, y+sy+sh),
                (0, 255, 0), 2
            )

    cv2.imshow("Smile Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
