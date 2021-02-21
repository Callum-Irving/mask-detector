from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
import sys
import cv2
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np
import os


class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def run(self):
        cv2_base_dir = os.path.dirname(os.path.abspath(cv2.__file__))

        face_model = os.path.join(
            cv2_base_dir, 'data/haarcascade_frontalface_default.xml')
        face_model = cv2.CascadeClassifier(face_model)

        eye_model = os.path.join(
            cv2_base_dir, 'data/haarcascade_eye_tree_eyeglasses.xml')
        eye_model = cv2.CascadeClassifier(eye_model)

        mouth_model = "datasets/haarcascade_mouth.xml"
        mouth_model = cv2.CascadeClassifier(mouth_model)

        if not os.path.exists("Captured Faces"):
            os.mkdir("Captured Faces")

        frame_counter = 0
        num_captured_faces = 0

        # capture from web cam
        capture = cv2.VideoCapture(0)
        while capture.isOpened():
            ret, frame = capture.read()
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

            self.change_pixmap_signal.emit(frame)

        capture.release()


class Webcam(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt live label demo")
        self.disply_width = 640
        self.display_height = 480
        # create the label that holds the image
        self.image_label = QLabel(self)
        self.image_label.resize(self.disply_width, self.display_height)
        # create a text label
        self.textLabel = QLabel('Webcam')

        # create a vertical box layout and add the two labels
        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.textLabel)
        # set the vbox layout as the widgets layout
        self.setLayout(vbox)

        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()

    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(
            rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(
            self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = Webcam()
    a.show()
    sys.exit(app.exec_())
