from Main_UI import *

class UIFunctions(MainWindow):

    def toggleMenu(self,maxWidth,enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 50


            # SET MAX WIDTH
            if width == 50:
                widthEntended = maxExtend
            else:
                widthEntended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthEntended)
            self.animation.start()