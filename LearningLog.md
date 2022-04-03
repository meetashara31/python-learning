# AI / ML
> Problems I found
1. cv2.CascadeClassifier() paramerter updated so stackoverflow helps for new param.
2. How to access Numpy.ndarray value 
```
# Single usage
(x,y,w,h) = face_cordinates[0]

# loop within all face
for(x,y,w,h) in face_cordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
```
3. We are using "Haar Cascade" algorithm for face detection till now
Harr is inventor of this algorithm
- Algorithm working
```
There are three 3 haar features that are used find face
similarity
![features](Learning\haar_features.jpg)
algorithme try to find this features in given image and decides if
face exitsts or not
```

4. Simplest algorithm to start with
```
Haar cascade is the simplest algorithm to start with there
are lots of trained model available online easily
```