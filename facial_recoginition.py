import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Video capture obj 0 for webcam or you can add video file
cap = cv2.VideoCapture(0)

# Capture each frame
while True:
    _, img = cap.read()

# Image capture obj
#img = cv2.imread('gp.jpg')

# Method works on black and white images so coverting them in grayscale 
# Order BGR : Blue, Green, RED
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grayImg, 1.2, 7)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('img', img)
        k =cv2.waitKey(30) & 0xff
         # If esc key is pressed break the loop
        if k==27:
                break
cap.release()
