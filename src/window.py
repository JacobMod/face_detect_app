import sys

from capture import *


class Window(QtWidgets.QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle("VideoStreamApp")
        #self.setWindowIcon(QtGui.QIcon('opencvlogo.png'))

        self.capture = Capture()
        self.video_widget = VideoWidget()
        
        image_window = self.video_widget.image_window
        self.capture.image_data.connect(image_window)

        self.add_buttons()
        self.set_layout()

        
    def add_buttons(self):

        
        self.start_cap_button = QtWidgets.QPushButton("Start capture")
        self.face_detect_on_button = QtWidgets.QPushButton("Face detection on")
        self.face_detect_off_button = QtWidgets.QPushButton("Face detection off")
        self.quit_app_button = QtWidgets.QPushButton("Quit app")
        self.save_cap_button = QtWidgets.QPushButton("Save capture")
        self.start_cap_button.clicked.connect(self.capture.start_cap)
        self.quit_app_button.clicked.connect(self.close_app)
        self.save_cap_button.clicked.connect(self.capture.save_cap)
        self.face_detect_on_button.clicked.connect(self.video_widget.set_on_detect)
        self.face_detect_off_button.clicked.connect(self.video_widget.set_off_detect)

    def set_layout(self):

        
        buttons_layout = QtWidgets.QHBoxLayout()
        
        buttons_layout.addWidget(self.start_cap_button)
        buttons_layout.addWidget(self.save_cap_button)
        buttons_layout.addWidget(self.face_detect_on_button)
        buttons_layout.addWidget(self.face_detect_off_button)
        buttons_layout.addWidget(self.quit_app_button)
               
        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(buttons_layout)
        layout.addWidget(self.video_widget)
                    
        self.setLayout(layout)

        
    def close_app(self):
        question = QtWidgets.QMessageBox.question(self, 'Extract', 'Do you really want to quit?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if question == QtWidgets.QMessageBox.Yes:
            print("Closing app")
            self.capture.cap.release()
            cv2.destroyAllWindows()
            sys.exit()
        else:
            pass


    
