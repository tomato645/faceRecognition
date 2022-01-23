# if you want to stop running, you press ESC key.

import cv2

face_cascade = cv2.CascadeClassifier("./assets/")


cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = img[y: y + h, x: x + w]
        face_gray = gray[y: y + h, x: x + w]
        cv2.putText(img, 'Recognizing... press ESC to stop', (0,50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,200), 2, cv2.LINE_AA)
    cv2.imshow('video image', img)
    key = cv2.waitKey(10)
    
    # escを押したら終了
    if key == 27:
        print("Pressed ESC")
        break

cap.release()
cv2.destroyAllWindows()