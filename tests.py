import os
import sys
import pyautogui
from PyQt5 import QtCore, QtGui,QtWidgets
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QIcon, QPixmap, QMouseEvent
# from PyQt5.QtWidgets import *

app = QtWidgets.QApplication(sys.argv)

class Controls(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        #Feststellung der aktuellen Bildschirmgröße
        self.screen_width, self.screen_height= pyautogui.size()
        self.statusBar()
        self.setGeometry(0, 0, self.screen_width, self.screen_height)
        self.setWindowTitle('Farbtester')

        self.box1 = QtWidgets.QGroupBox("gb1")
        self.box2 = QtWidgets.QGroupBox("gb2")

        self.ambient = QtWidgets.QRadioButton("Ambientsound")
        self.game_sounds = QtWidgets.QRadioButton("Game Sounds")

        self.v = QtWidgets.QVBoxLayout(self)

        self.v.addWidget(self.box1)



class ColorSlider(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.slider = QtWidgets.QSlider()
        self.slider.setGeometry(QtCore.QRect(950, 40, 122, 720))
        self.slider.setMinimum(0)
        self.slider.setMaximum(255)
        self.slider.setSliderPosition(0)
        self.slider.setTracking(True)
        self.slider.setOrientation(QtCore.Qt.Vertical)
        self.slider.setInvertedAppearance(True)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.slider.setTickInterval(1)




fenster = Controls()

fenster.show()

red = ColorSlider()
red.setWindowTitle('R')
red.slider.setGeometry(QtCore.QRect(1150, 80, 122, fenster.screen_height - 220))
green = ColorSlider()
green.slider.setGeometry(QtCore.QRect(1350, 80, 122, fenster.screen_height - 220))
blue = ColorSlider()
blue.slider.setGeometry(QtCore.QRect(1550, 80, 122, fenster.screen_height - 220))

# red.slider.show()
# green.slider.show()
# blue.slider.show()

fenster.red = QtWidgets.QSlider(fenster)
fenster.red.setGeometry(QtCore.QRect(50, 40, 22, fenster.screen_height - 220))
fenster.red.setMinimum(0)
fenster.red.setMaximum(255)
fenster.red.setSliderPosition(0)
fenster.red.setTracking(True)
fenster.red.setOrientation(QtCore.Qt.Vertical)
fenster.red.setInvertedAppearance(True)
fenster.red.setTickPosition(QtWidgets.QSlider.TicksAbove)
fenster.red.setTickInterval(1)
fenster.red.setObjectName("red")
fenster.red.show()


fenster.red_value = QtWidgets.QLabel(fenster)
fenster.red_value.setGeometry(1000, 100, 100, 50)

fenster.green = QtWidgets.QSlider(fenster)
fenster.green.setGeometry(QtCore.QRect(150, 40, 22, fenster.screen_height - 220))
fenster.green.setMinimum(0)
fenster.green.setMaximum(255)
fenster.green.setSliderPosition(0)
fenster.green.setTracking(True)
fenster.green.setOrientation(QtCore.Qt.Vertical)
fenster.green.setInvertedAppearance(True)
fenster.green.setTickPosition(QtWidgets.QSlider.TicksAbove)
fenster.green.setTickInterval(1)
fenster.green.setObjectName("red")
fenster.green.show()

fenster.green_value = QtWidgets.QLabel(fenster)
fenster.green_value.setGeometry(1000, 200, 100, 50)


fenster.blue = QtWidgets.QSlider(fenster)
fenster.blue.setGeometry(QtCore.QRect(250, 40, 22, fenster.screen_height - 220))
fenster.blue.setMinimum(0)
fenster.blue.setMaximum(255)
fenster.blue.setSliderPosition(0)
fenster.blue.setTracking(True)
fenster.blue.setOrientation(QtCore.Qt.Vertical)
fenster.blue.setInvertedAppearance(True)
fenster.blue.setTickPosition(QtWidgets.QSlider.TicksAbove)
fenster.blue.setTickInterval(1)
fenster.blue.setObjectName("red")
fenster.blue.show()

fenster.blue_value = QtWidgets.QLabel(fenster)
fenster.blue_value.setGeometry(1000, 300, 100, 50)

result = QtWidgets.QLabel(fenster)
result.setGeometry(500, 100, 300, 500)
# result.show()

def show():

    result.setStyleSheet(
        f'background-color: rgb({int(fenster.red.value())},{int(fenster.green.value())},{int(fenster.blue.value())});'
        "border: 2px solid lightGrey;"
        "color: black; "
        "font-size: 9px;"
        "text-align: left; "
    )


    fenster.red_value.setText(f'Rot: {str(fenster.red.value())}')
    fenster.red_value.show()
    fenster.green_value.setText(f'Grün: {str(fenster.green.value())}')
    fenster.green_value.show()
    fenster.blue_value.setText(f'Blau: {str(fenster.blue.value())}')
    fenster.blue_value.show()

    result.show()


fenster.red.valueChanged.connect(show)
fenster.green.valueChanged.connect(show)
fenster.blue.valueChanged.connect(show)



sys.exit(app.exec())