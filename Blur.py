import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox

from UI_functons import *

class ImageBlur():

    # Haar Cascade for Face Detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
    vc = ""
    #Get GUI Files


    def ImageProcessing(self, path):
        # Read Input Image
        print("this is called")
        image = cv2.imread(path)

        # Detect the faces in Images
        faces = self.face_cascade.detectMultiScale(image, 1.3, 5)

        for (x, y, w, h) in faces:
            # Enclose the detected faces inside a rectangular box
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 3)
            # Select the detected face area
            face_color = image[y:y + h, x:x + w]
            # Blur the detected face
            blur = cv2.GaussianBlur(face_color, (51, 51), 0)
            image[y:y + h, x:x + w] = blur

        # Display the Blurred Faces Image
        return image

    def VideoBlur(self, image_frame):
        # Detect faces in the Webcam Video Stream
        faces = self.face_cascade.detectMultiScale(image_frame, 1.3, 5)
        for (x, y, w, h) in faces:
            # Enclose inside a blue rectangular box
            cv2.rectangle(image_frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
            # Select only detected face portion for Blur
            face_color = image_frame[y:y + h, x:x + w]
            # Blur the Face with Gaussian Blur of random Kernel Size 51*51
            blur = cv2.GaussianBlur(face_color, (51, 51), 0)
            image_frame[y:y + h, x:x + w] = blur
        # Display the Blurred Faces
        return image_frame



