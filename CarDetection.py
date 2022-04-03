import cv2

#car img_ file
img_file = 'images/car3.jpg'

#our pre-trained car classifier
classifier_file= 'models/car_detector.xml'
#car tracker
car_tracker = cv2.CascadeClassifier(classifier_file)

# create opencv image
img = cv2.imread(img_file)

#convert image to black and white 
#convert to grayscale (neede for haar cascade)
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#create car classifier rectangular box
car_tracker = cv2.CascadeClassifier(classifier_file)


#detect cars
cars = car_tracker.detectMultiScale(black_n_white)

#print(cars)
#[[1589   10   57   57]
#[1568  118   33   33]

#Draw rectabgles around the cards
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)

# display the image with the faces spotted
cv2.imshow('Clever Programmer Car Detector', img) #img color and #black_white 

# Dont autoclose (wait here in the code and listen for key press)
cv2.waitKey()

print("Code completed")