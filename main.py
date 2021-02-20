import os
import numpy as np
import cv2

cv2_base_dir = os.path.dirname(os.path.abspath(cv2.__file__))
haar_model = os.path.join(
    cv2_base_dir, 'data/haarcascade_frontalface_default.xml')
face_haar_cascade = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')
haar_model = cv2.CascadeClassifier(haar_model)
capture = cv2.VideoCapture(0)  # Video capture using first camera

while True:
    # Get frame from webcam
    _, frame = capture.read()
    # Convert to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.equalizeHist(gray_frame)

    faces = haar_model.detectMultiScale(gray_frame, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
