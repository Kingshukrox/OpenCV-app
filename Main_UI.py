import sys
import cv2
import os
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent, QTimer)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from UI import Ui_MainWindow

# IMPORT FUNCTIONS
from UI_functons import *
from Blur import *
from detectmask import *
from drowsiness_detect import *


class MainWindow(QMainWindow):
    Selected_File = ""
    isConnect = False

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.vc = ""
        self.isCamOn = False
        self.blur = ImageBlur()
        self.d_mask = Mask_detect()
        self.dro = Drowsiness()
        self.ui.setupUi(self)

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))

        ## All PAGES
        ########################################################################

        # FACE BLUR (PICTURE)
        self.ui.label_Current_page_title.setText(u'FACE BLUR (PICTURE)')
        self.ui.btn_FBP.clicked.connect(lambda: self.CurrentPage(self.ui.Page_FBP, u'FACE BLUR (PICTURE)'))
        self.ui.Btn_FBP_Browse.clicked.connect(self.browsefiles)
        self.ui.Btn_Image_Blur_FBP.clicked.connect(self.ImageBlurCall)

        # FACE BLUR (VIDEO)
        self.ui.btn_FBV.clicked.connect(lambda: self.CurrentPage(self.ui.Page_FBV, u'FACE BLUR (VIDEO)'))
        self.ui.FBV_Detect_Video.clicked.connect(self.VideoBlurCall)
        self.ui.FBV_Stop_Video.clicked.connect(self.Stop_Camera)

        # DETECT MASK
        self.ui.btn_DM.clicked.connect(lambda: self.CurrentPage(self.ui.Page_DM, u'DETECT MASK'))
        self.ui.DM_Detect_Video.clicked.connect(self.VideoDetectMaskCall)
        self.ui.DM_Stop_Video.clicked.connect(self.Stop_Camera)

        # DROWSINESS
        self.ui.btn_DRO.clicked.connect(lambda: self.CurrentPage(self.ui.Page_DRO, u'DROWSINESS'))
        self.ui.DRO_Detect_Video.clicked.connect(self.VideoDrowsiness)
        self.ui.DRO_Stop_Video.clicked.connect(self.Stop_Camera)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## File Browsefiles

    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'c:\\', 'Image files (*.jpg *.png *.jfif)')
        self.ui.FBP_Browse_Path.setText(fname[0])
        self.Selected_File = fname[0]
        print(self.Selected_File)

    ## Current Page Name

    def CurrentPage(self, page, name):
        self.RestPages()
        self.ui.Pages_Widget.setCurrentWidget(page)
        self.ui.label_Current_page_title.setText(name)

    ## Image Blur File

    def ImageBlurCall(self):
        image = ImageBlur.ImageProcessing(self.blur, self.Selected_File)
        self.ui.FBP_Image_Display.setText("")
        display_image = QtGui.QImage(image, image.shape[1], image.shape[0], image.shape[1] * 3,
                                     QtGui.QImage.Format_RGB888)
        self.ui.FBP_Image_Display.setPixmap(QtGui.QPixmap(display_image))

    ## Video Blur File
    def VideoBlurCall(self):
        self.isCamOn = True
        self.ui.FBP_Image_Display.setText("Video is Loading")
        self.vc = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while self.vc.isOpened():
            if self.isCamOn:
                ret, frame = self.vc.read()
                if ret:
                    frame = ImageBlur.VideoBlur(self.blur, frame)
                    self.display_frame(frame, self.ui.FBV_Video_Display)
                    cv2.waitKey()
                else:
                    break
                    print("No Camera Found")
            else:
                break
        self.vc.release()
        cv2.destroyAllWindows()

    ## DetectMask File
    def VideoDetectMaskCall(self):
        cascPath = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
        facecascade = cv2.CascadeClassifier(cascPath)

        model = load_model("mask_recog_ver2.h5")
        self.isCamOn = True
        self.vc = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        while self.vc.isOpened():
            if self.isCamOn:
                ret, frame = self.vc.read()
                if ret:
                    frame = Mask_detect.Detect(self.d_mask, frame, facecascade, model)
                    self.display_frame(frame, self.ui.DM_Video_Display)
                    cv2.waitKey()
                else:
                    break
                    print("No Camera Found")
            else:
                break
        self.vc.release()
        cv2.destroyAllWindows()

    ## Detect Drowsiness
    def VideoDrowsiness(self):
        self.isCamOn = True
        self.ui.FBP_Image_Display.setText("Video is Loading")
        self.vc = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while self.vc.isOpened():
            if self.isCamOn:
                ret, frame = self.vc.read()
                if ret:
                    Drowsiness.Detect(self.dro, frame)
                    self.display_frame(frame, self.ui.DRO_Video_Display)
                    cv2.waitKey()
                else:
                    break
                    print("No Camera Found")

            else:
                break
        self.vc.release()
        cv2.destroyAllWindows()

    ## This Function Displays the Given Video Image to GUI

    def display_frame(self, img, lable):
        qformat = QtGui.QImage.Format_RGB888
        self.ui.FBP_Image_Display.setText("")
        img = QtGui.QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()
        lable.setScaledContents(True)
        lable.setPixmap(QtGui.QPixmap.fromImage(img))
        lable.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

    def Stop_Camera(self):
        self.isCamOn = False

    def RestPages(self):
        self.Selected_File = ""
        self.ui.FBP_Browse_Path.setText("")
        self.ui.FBP_Image_Display.setScaledContents(False)
        self.ui.FBP_Image_Display.setPixmap(QtGui.QPixmap(u":/24x24/Resources/icons/24x24/cil-image-plus.png"))
        self.ui.FBV_Video_Display.setScaledContents(False)
        self.ui.FBV_Video_Display.setPixmap(QtGui.QPixmap(u":/24x24/Resources/icons/24x24/cil-video.png"))
        self.ui.DM_Video_Display.setScaledContents(False)
        self.ui.DM_Video_Display.setPixmap(QtGui.QPixmap(u":/24x24/Resources/icons/24x24/cil-video.png"))
        self.ui.DRO_Video_Display.setScaledContents(False)
        self.ui.DRO_Video_Display.setPixmap(QtGui.QPixmap(u":/24x24/Resources/icons/24x24/cil-video.png"))
        self.Stop_Camera()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
