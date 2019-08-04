import cv2
import numpy as np
from PyQt5 import QtCore, QtWidgets, QtGui
import uuid

class Capture(QtCore.QThread):
    image_data = QtCore.pyqtSignal(np.ndarray)

    
    def __init__(self, camera_port = 0, parent = None):
        super().__init__(parent)
        self.cap = cv2.VideoCapture(camera_port)
        self.timer = QtCore.QBasicTimer()


    def start_cap(self):
        print('Start capture')
        self.timer.start(0, self)


    def timerEvent(self, event):
        if (event.timerId() != self.timer.timerId()):
            return
        ret, frame = self.cap.read()
        if ret:
            self.image_data.emit(frame)


    def end_cap(self):
        print("Ending capture")
        self.timer.stop()
        self.cap.release()


    def save_cap(self):
        print("Saving capture")
        _, frame = self.cap.read()
        file_name = '../saved_images/img_' + str(uuid.uuid4()) + '.png'
        cv2.imwrite(file_name, frame)

    
class VideoWidget(QtWidgets.QWidget):


    def __init__(self, parent=None, file_path = '../haarcascade_frontalface_default.xml'):
        super().__init__(parent)
        self.image = QtGui.QImage()
        self.face_cascade = cv2.CascadeClassifier(file_path)
        self.if_face_detect = False


    def image_window(self, image_data):
        if(self.if_face_detect == True):
            faces = self.get_faces(image_data)
            for(x, y, w, h) in faces:
                cv2.rectangle(image_data, (x, y), (x+w, y+h), (0, 255, 0), 2)
        else:
            pass
        self.image = self.get_qimg(image_data)
        self.setFixedSize(self.image.size())
        self.update()


    def get_faces(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # working better with gray imgs
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        return faces
        

    def get_qimg(self, image):
        h, w, ch = image.shape
        bytesPerLine = 3 * w 
        image = QtGui.QImage(image.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
        image = image.rgbSwapped()
        return image


    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)
        self.image = QtGui.QImage()


    def set_on_detect(self):
        self.if_face_detect = True


    def set_off_detect(self):
        self.if_face_detect = False
       
        
