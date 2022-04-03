import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')
# trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades)

while True:
    webcam = cv2.VideoCapture(0)
    success_frame_read, frame = webcam.read()
    if not success_frame_read:
        break

    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cordinates = trained_face_data.detectMultiScale(grayscaled_img)

    for(x,y,w,h) in face_cordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('webcame title', frame)

    key = cv2.waitKey(1)

    if key==81 or key==113:
      break

webcam.release()
print("Code Completed.........")