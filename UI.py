# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QSize(800, 800))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgba(45, 45, 45, 255);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_bar = QFrame(self.centralwidget)
        self.Top_bar.setObjectName(u"Top_bar")
        self.Top_bar.setMinimumSize(QSize(0, 40))
        self.Top_bar.setMaximumSize(QSize(16777215, 40))
        self.Top_bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_bar.setFrameShape(QFrame.NoFrame)
        self.Top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMinimumSize(QSize(50, 40))
        self.frame_toggle.setMaximumSize(QSize(50, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;\n"
"qproperty-icon: url(:/24x24/Resources/icons/24x24/cil-list.png)")

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ProjectTitle = QLabel(self.frame_top)
        self.ProjectTitle.setObjectName(u"ProjectTitle")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ProjectTitle.setFont(font)
        self.ProjectTitle.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.ProjectTitle)


        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(50, 0))
        self.frame_left_menu.setMaximumSize(QSize(50, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(0, 7, 27);\n"
"padding-left: 2px;")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menu = QFrame(self.frame_left_menu)
        self.frame_top_menu.setObjectName(u"frame_top_menu")
        self.frame_top_menu.setAutoFillBackground(False)
        self.frame_top_menu.setFrameShape(QFrame.NoFrame)
        self.frame_top_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menu)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 0)
        self.btn_FBP = QPushButton(self.frame_top_menu)
        self.btn_FBP.setObjectName(u"btn_FBP")
        self.btn_FBP.setMinimumSize(QSize(200, 40))
        self.btn_FBP.setMaximumSize(QSize(200, 40))
        self.btn_FBP.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/Resources/icons/24x24/cil-image1.png);\n"
"	background-position:left center;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: none;	\n"
"	background-repeat: none;\n"
"	padding-left: 50px;\n"
"	Text-align:left;\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_FBP)

        self.btn_FBV = QPushButton(self.frame_top_menu)
        self.btn_FBV.setObjectName(u"btn_FBV")
        self.btn_FBV.setMinimumSize(QSize(200, 40))
        self.btn_FBV.setMaximumSize(QSize(200, 40))
        self.btn_FBV.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/Resources/icons/24x24/cil-video.png);\n"
"	background-position:left center;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: none;\n"
"	background-repeat: none;\n"
"	padding-left: 50px;\n"
"	Text-align:left;\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_FBV)

        self.btn_DM = QPushButton(self.frame_top_menu)
        self.btn_DM.setObjectName(u"btn_DM")
        self.btn_DM.setMinimumSize(QSize(200, 40))
        self.btn_DM.setMaximumSize(QSize(200, 40))
        font1 = QFont()
        font1.setPointSize(6)
        self.btn_DM.setFont(font1)
        self.btn_DM.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/Resources/icons/24x24/cil-mood-good.png);\n"
"	background-position:left center;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: none;\n"
"	background-repeat: none;\n"
"	padding-left: 50px;\n"
"	Text-align:left;\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_DM.setIconSize(QSize(40, 40))
        self.btn_DM.setAutoRepeat(False)

        self.verticalLayout_4.addWidget(self.btn_DM)

        self.btn_DRO = QPushButton(self.frame_top_menu)
        self.btn_DRO.setObjectName(u"btn_DRO")
        self.btn_DRO.setMinimumSize(QSize(200, 40))
        self.btn_DRO.setMaximumSize(QSize(200, 40))
        self.btn_DRO.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/Resources/icons/24x24/cil-wifi-signal-0.png);\n"
"	background-position: left center;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: none;\n"
"	background-repeat: none;\n"
"	padding-left: 50px;\n"
"	Text-align: left;\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_DRO.setIconSize(QSize(40, 40))
        self.btn_DRO.setAutoRepeat(False)
        self.btn_DRO.setFlat(False)

        self.verticalLayout_4.addWidget(self.btn_DRO)


        self.verticalLayout_3.addWidget(self.frame_top_menu, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu, 0, Qt.AlignHCenter)

        self.frame_page = QFrame(self.Content)
        self.frame_page.setObjectName(u"frame_page")
        self.frame_page.setFrameShape(QFrame.StyledPanel)
        self.frame_page.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_page)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Top_Menu = QFrame(self.frame_page)
        self.Top_Menu.setObjectName(u"Top_Menu")
        self.Top_Menu.setMinimumSize(QSize(0, 20))
        self.Top_Menu.setMaximumSize(QSize(16777215, 20))
        self.Top_Menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Menu.setFrameShape(QFrame.StyledPanel)
        self.Top_Menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Top_Menu)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 5, 0)
        self.label_Current_page_title = QLabel(self.Top_Menu)
        self.label_Current_page_title.setObjectName(u"label_Current_page_title")
        font2 = QFont()
        font2.setPointSize(6)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_Current_page_title.setFont(font2)
        self.label_Current_page_title.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_Current_page_title.setTextFormat(Qt.RichText)
        self.label_Current_page_title.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_Current_page_title)


        self.verticalLayout_5.addWidget(self.Top_Menu)

        self.Content_Page = QFrame(self.frame_page)
        self.Content_Page.setObjectName(u"Content_Page")
        self.Content_Page.setFrameShape(QFrame.StyledPanel)
        self.Content_Page.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.Content_Page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Pages_Widget = QStackedWidget(self.Content_Page)
        self.Pages_Widget.setObjectName(u"Pages_Widget")
        self.Page_FBP = QWidget()
        self.Page_FBP.setObjectName(u"Page_FBP")
        self.verticalLayout_8 = QVBoxLayout(self.Page_FBP)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 0, 5, 0)
        self.label_title = QLabel(self.Page_FBP)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMinimumSize(QSize(0, 20))
        self.label_title.setMaximumSize(QSize(16777215, 40))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_title.setFont(font3)
        self.label_title.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_title.setTextFormat(Qt.RichText)
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_title)

        self.Fileframe = QFrame(self.Page_FBP)
        self.Fileframe.setObjectName(u"Fileframe")
        self.Fileframe.setMinimumSize(QSize(0, 40))
        self.Fileframe.setMaximumSize(QSize(16777215, 40))
        self.Fileframe.setFrameShape(QFrame.NoFrame)
        self.Fileframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.Fileframe)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.FBP_Browse_Path = QLineEdit(self.Fileframe)
        self.FBP_Browse_Path.setObjectName(u"FBP_Browse_Path")
        self.FBP_Browse_Path.setMinimumSize(QSize(0, 30))
        self.FBP_Browse_Path.setMaximumSize(QSize(16777215, 30))
        self.FBP_Browse_Path.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.FBP_Browse_Path)

        self.Btn_FBP_Browse = QPushButton(self.Fileframe)
        self.Btn_FBP_Browse.setObjectName(u"Btn_FBP_Browse")
        self.Btn_FBP_Browse.setMinimumSize(QSize(150, 40))
        self.Btn_FBP_Browse.setMaximumSize(QSize(150, 40))
        self.Btn_FBP_Browse.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);	\n"
"	border: 0px solid;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.Btn_FBP_Browse)

        self.Btn_Image_Blur_FBP = QPushButton(self.Fileframe)
        self.Btn_Image_Blur_FBP.setObjectName(u"Btn_Image_Blur_FBP")
        self.Btn_Image_Blur_FBP.setMinimumSize(QSize(150, 40))
        self.Btn_Image_Blur_FBP.setMaximumSize(QSize(150, 40))
        self.Btn_Image_Blur_FBP.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);	\n"
"	border: 0px solid;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.Btn_Image_Blur_FBP)


        self.verticalLayout_8.addWidget(self.Fileframe)

        self.FBP_Content = QFrame(self.Page_FBP)
        self.FBP_Content.setObjectName(u"FBP_Content")
        self.FBP_Content.setFrameShape(QFrame.StyledPanel)
        self.FBP_Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.FBP_Content)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.FBP_Image_Display = QLabel(self.FBP_Content)
        self.FBP_Image_Display.setObjectName(u"FBP_Image_Display")
        self.FBP_Image_Display.setMinimumSize(QSize(0, 0))
        self.FBP_Image_Display.setMaximumSize(QSize(16777215, 16777215))
        self.FBP_Image_Display.setFrameShadow(QFrame.Plain)
        self.FBP_Image_Display.setPixmap(QPixmap(u":/24x24/Resources/icons/24x24/cil-image-plus.png"))
        self.FBP_Image_Display.setScaledContents(False)
        self.FBP_Image_Display.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.FBP_Image_Display)


        self.verticalLayout_8.addWidget(self.FBP_Content)

        self.Pages_Widget.addWidget(self.Page_FBP)
        self.Page_FBV = QWidget()
        self.Page_FBV.setObjectName(u"Page_FBV")
        self.verticalLayout_10 = QVBoxLayout(self.Page_FBV)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 0, 5, 0)
        self.label_title_FBP = QLabel(self.Page_FBV)
        self.label_title_FBP.setObjectName(u"label_title_FBP")
        self.label_title_FBP.setMinimumSize(QSize(0, 40))
        self.label_title_FBP.setMaximumSize(QSize(16777215, 40))
        self.label_title_FBP.setFont(font3)
        self.label_title_FBP.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_title_FBP.setTextFormat(Qt.RichText)
        self.label_title_FBP.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_title_FBP)

        self.FBV_Video_frame = QFrame(self.Page_FBV)
        self.FBV_Video_frame.setObjectName(u"FBV_Video_frame")
        self.FBV_Video_frame.setMinimumSize(QSize(0, 40))
        self.FBV_Video_frame.setMaximumSize(QSize(16777215, 40))
        self.FBV_Video_frame.setFrameShape(QFrame.NoFrame)
        self.FBV_Video_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.FBV_Video_frame)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.FBV_Detect_Video = QPushButton(self.FBV_Video_frame)
        self.FBV_Detect_Video.setObjectName(u"FBV_Detect_Video")
        self.FBV_Detect_Video.setMinimumSize(QSize(0, 40))
        self.FBV_Detect_Video.setMaximumSize(QSize(16777215, 40))
        self.FBV_Detect_Video.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);	\n"
"	border: 0px solid;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_7.addWidget(self.FBV_Detect_Video)

        self.FBV_Stop_Video = QPushButton(self.FBV_Video_frame)
        self.FBV_Stop_Video.setObjectName(u"FBV_Stop_Video")
        self.FBV_Stop_Video.setMinimumSize(QSize(0, 40))
        self.FBV_Stop_Video.setMaximumSize(QSize(16777215, 40))
        self.FBV_Stop_Video.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);	\n"
"	border: 0px solid;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_7.addWidget(self.FBV_Stop_Video)


        self.verticalLayout_10.addWidget(self.FBV_Video_frame)

        self.FBV_Video_Display = QLabel(self.Page_FBV)
        self.FBV_Video_Display.setObjectName(u"FBV_Video_Display")
        self.FBV_Video_Display.setPixmap(QPixmap(u":/24x24/Resources/icons/24x24/cil-video.png"))
        self.FBV_Video_Display.setScaledContents(False)
        self.FBV_Video_Display.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.FBV_Video_Display)

        self.Pages_Widget.addWidget(self.Page_FBV)
        self.Page_DM = QWidget()
        self.Page_DM.setObjectName(u"Page_DM")
        self.verticalLayout_9 = QVBoxLayout(self.Page_DM)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 0, 5, 0)
        self.label_title_DM = QLabel(self.Page_DM)
        self.label_title_DM.setObjectName(u"label_title_DM")
        self.label_title_DM.setMinimumSize(QSize(0, 40))
        self.label_title_DM.setMaximumSize(QSize(16777215, 40))
        self.label_title_DM.setFont(font3)
        self.label_title_DM.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_title_DM.setTextFormat(Qt.RichText)
        self.label_title_DM.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_title_DM)

        self.DM_VIdeo_frame = QFrame(self.Page_DM)
        self.DM_VIdeo_frame.setObjectName(u"DM_VIdeo_frame")
        self.DM_VIdeo_frame.setMinimumSize(QSize(0, 40))
        self.DM_VIdeo_frame.setMaximumSize(QSize(16777215, 40))
        self.DM_VIdeo_frame.setFrameShape(QFrame.StyledPanel)
        self.DM_VIdeo_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.DM_VIdeo_frame)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.DM_Detect_Video = QPushButton(self.DM_VIdeo_frame)
        self.DM_Detect_Video.setObjectName(u"DM_Detect_Video")
        self.DM_Detect_Video.setMinimumSize(QSize(0, 40))
        self.DM_Detect_Video.setMaximumSize(QSize(16777215, 40))
        self.DM_Detect_Video.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);	\n"
"	border: 0px solid;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_8.addWidget(self.DM_Detect_Video)

        self.DM_Stop_Video = QPushButton(self.DM_VIdeo_frame)
        self.DM_Stop_Video.setObjectName(u"DM_Stop_Video")
        self.DM_Stop_Video.setMinimumSize(QSize(0, 40))
        self.DM_Stop_Video.setMaximumSize(QSize(16777215, 40))
        self.DM_Stop_Video.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);	\n"
"	border: 0px solid;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_8.addWidget(self.DM_Stop_Video)


        self.verticalLayout_9.addWidget(self.DM_VIdeo_frame)

        self.DM_Video_Display = QLabel(self.Page_DM)
        self.DM_Video_Display.setObjectName(u"DM_Video_Display")
        self.DM_Video_Display.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.DM_Video_Display.setPixmap(QPixmap(u":/24x24/Resources/icons/24x24/cil-video.png"))
        self.DM_Video_Display.setScaledContents(False)
        self.DM_Video_Display.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.DM_Video_Display)

        self.Pages_Widget.addWidget(self.Page_DM)
        self.Page_DRO = QWidget()
        self.Page_DRO.setObjectName(u"Page_DRO")
        self.verticalLayout_11 = QVBoxLayout(self.Page_DRO)
        self.verticalLayout_11.setSpacing(7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 0, 5, 0)
        self.label_title_DRO = QLabel(self.Page_DRO)
        self.label_title_DRO.setObjectName(u"label_title_DRO")
        self.label_title_DRO.setMinimumSize(QSize(0, 40))
        self.label_title_DRO.setMaximumSize(QSize(16777215, 40))
        self.label_title_DRO.setFont(font3)
        self.label_title_DRO.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_title_DRO.setTextFormat(Qt.RichText)
        self.label_title_DRO.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_title_DRO)

        self.frame = QFrame(self.Page_DRO)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.DRO_Detect_Video = QPushButton(self.frame)
        self.DRO_Detect_Video.setObjectName(u"DRO_Detect_Video")
        self.DRO_Detect_Video.setMinimumSize(QSize(0, 40))
        self.DRO_Detect_Video.setMaximumSize(QSize(16777215, 40))
        self.DRO_Detect_Video.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);	\n"
"	border: 0px solid;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_9.addWidget(self.DRO_Detect_Video)

        self.DRO_Stop_Video = QPushButton(self.frame)
        self.DRO_Stop_Video.setObjectName(u"DRO_Stop_Video")
        self.DRO_Stop_Video.setMinimumSize(QSize(0, 40))
        self.DRO_Stop_Video.setMaximumSize(QSize(16777215, 40))
        self.DRO_Stop_Video.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);	\n"
"	border: 0px solid;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_9.addWidget(self.DRO_Stop_Video)


        self.verticalLayout_11.addWidget(self.frame)

        self.DRO_Video_Display = QLabel(self.Page_DRO)
        self.DRO_Video_Display.setObjectName(u"DRO_Video_Display")
        self.DRO_Video_Display.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.DRO_Video_Display.setTextFormat(Qt.AutoText)
        self.DRO_Video_Display.setPixmap(QPixmap(u":/24x24/Resources/icons/24x24/cil-video.png"))
        self.DRO_Video_Display.setScaledContents(False)
        self.DRO_Video_Display.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.DRO_Video_Display)

        self.Pages_Widget.addWidget(self.Page_DRO)

        self.verticalLayout_6.addWidget(self.Pages_Widget)


        self.verticalLayout_5.addWidget(self.Content_Page)

        self.Bottom_Menu = QFrame(self.frame_page)
        self.Bottom_Menu.setObjectName(u"Bottom_Menu")
        self.Bottom_Menu.setMinimumSize(QSize(0, 20))
        self.Bottom_Menu.setMaximumSize(QSize(16777215, 20))
        self.Bottom_Menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Bottom_Menu.setFrameShape(QFrame.StyledPanel)
        self.Bottom_Menu.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.Bottom_Menu)


        self.horizontalLayout_2.addWidget(self.frame_page)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages_Widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText("")
        self.ProjectTitle.setText(QCoreApplication.translate("MainWindow", u"PROJECT TITLE", None))
        self.btn_FBP.setText(QCoreApplication.translate("MainWindow", u"FACE BLUR (PICTURE)", None))
        self.btn_FBV.setText(QCoreApplication.translate("MainWindow", u"FACE BLUR (VIDEO)", None))
        self.btn_DM.setText(QCoreApplication.translate("MainWindow", u"DETECT MASK", None))
        self.btn_DRO.setText(QCoreApplication.translate("MainWindow", u"DROWSINESS", None))
        self.label_Current_page_title.setText(QCoreApplication.translate("MainWindow", u"CURRENT PAGE NAME", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"FACE BLUR (PICTURE)", None))
        self.Btn_FBP_Browse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.Btn_Image_Blur_FBP.setText(QCoreApplication.translate("MainWindow", u"Image Blur", None))
        self.FBP_Image_Display.setText("")
        self.label_title_FBP.setText(QCoreApplication.translate("MainWindow", u"FACE BLUR (VIDEO)", None))
        self.FBV_Detect_Video.setText(QCoreApplication.translate("MainWindow", u"Open Camera", None))
        self.FBV_Stop_Video.setText(QCoreApplication.translate("MainWindow", u"Stop Video", None))
        self.FBV_Video_Display.setText("")
        self.label_title_DM.setText(QCoreApplication.translate("MainWindow", u"DETECT MASK", None))
        self.DM_Detect_Video.setText(QCoreApplication.translate("MainWindow", u"Open Camera", None))
        self.DM_Stop_Video.setText(QCoreApplication.translate("MainWindow", u"Stop Camera", None))
        self.DM_Video_Display.setText("")
        self.label_title_DRO.setText(QCoreApplication.translate("MainWindow", u"DROWSINESS", None))
        self.DRO_Detect_Video.setText(QCoreApplication.translate("MainWindow", u"Open Camera", None))
        self.DRO_Stop_Video.setText(QCoreApplication.translate("MainWindow", u"Stop Camera", None))
        self.DRO_Video_Display.setText("")
    # retranslateUi

