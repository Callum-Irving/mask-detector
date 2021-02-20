import os
import numpy as np
import cv2
from datetime import datetime

cv2_base_dir = os.path.dirname(os.path.abspath(cv2.__file__))

face_model = os.path.join(
    cv2_base_dir, 'data/haarcascade_frontalface_default.xml')
face_model = cv2.CascadeClassifier(face_model)

eye_model = os.path.join(
    cv2_base_dir, 'data/haarcascade_eye_tree_eyeglasses.xml')
eye_model = cv2.CascadeClassifier(eye_model)

mouth_model = "datasets/haarcascade_mouth.xml"
mouth_model = cv2.CascadeClassifier(mouth_model)

capture = cv2.VideoCapture(0)  # Video capture using first camera

frame_counter = 0
num_captured_faces = 0

while True:
    # Get frame from webcam
    _, frame = capture.read()
    # Convert to greyscale
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey_frame = cv2.equalizeHist(grey_frame)

    faces = face_model.detectMultiScale(grey_frame, 1.3, 5)

    for (x, y, w, h) in faces:
        # Draw outline around face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cropped_grey = grey_frame[y:y+h, x:x+w]
        cropped_colour = frame[y:y+h, x:x+w]

        eyes = eye_model.detectMultiScale(cropped_grey)
        for (ex, ey, ew, eh) in eyes:
            # Draw filled black rectangle over eyes so that
            #   mouth detector does not detect eyes
            cv2.rectangle(cropped_grey, (ex, ey),
                          (ex+ew, ey+eh), (0, 0, 0), -1)

        mouthes = mouth_model.detectMultiScale(cropped_grey)
        if len(mouthes) > 0:
            frame_counter += 1
        else:
            frame_counter = 0

        for (mx, my, mw, mh) in mouthes:
            cv2.rectangle(cropped_colour, (mx, my),
                          (mx+mw, my+mh), (0, 0, 255), 2)
            if frame_counter > 30:
                if os.listdir("Captured Faces"):
                    face_num = int(os.listdir("Captured Faces")
                                   [-1].split(".")[0]) + 1
                else:
                    face_num = 0

                cv2.imwrite("Captured Faces/" +
                            str(face_num) + ".jpg", frame)
                frame_counter = 0
                num_captured_faces += 1

    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
