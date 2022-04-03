import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')
# trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades)

img = cv2.imread('images/faceImage.jpg')

grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cordinates = trained_face_data.detectMultiScale(grayscaled_img)

for(x,y,w,h) in face_cordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Capstion for this girl', img)
cv2.waitKey()

print("Code Completed.........")