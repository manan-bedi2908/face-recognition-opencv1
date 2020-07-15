import cv2

video = cv2.VideoCapture(0)
address = "https://192.168.0.100:8080/video"
video.open(address)
classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:

    ret, frame = video.read()

    if ret:
        faces = classifier.detectMultiScale(frame)

        for face in faces:
            x, y, w, h = face
            frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 4)

        cv2.imshow("My Window", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()