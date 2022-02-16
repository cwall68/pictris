import pygame
import sys
import os
import pyautogui
from PIL import Image
import random
import math
from math import ceil


from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import ctypes
from ctypes import wintypes


app = QtWidgets.QApplication(sys.argv)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pic_dir = os.path.join(BASE_DIR,"best of puzzles")
graf_dir = os.path.join(BASE_DIR,"Grafiken")


class Controls(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        #Feststellung der aktuellen Bildschirmgröße
        self.screen_width, self.screen_height= pyautogui.size()
        self.statusBar()
        self.setGeometry(0, 0, self.screen_width, self.screen_height)
        self.setWindowTitle('Pictris Controls')

        self.label_width = int(self.screen_width/22.5)
        self.label_height = self.label_width
        self.controls_space_width = int(0.25*self.screen_width)
        self.controls_elements_width = 4*self.label_width
        self.label_start_x = int((self.controls_space_width - self.controls_elements_width)/2)
        self.label_start_y = int(self.screen_height/15)
        self.label_space = int(1.5*self.label_width)
        self.button_height = int(self.screen_height/80)
        self.text_height = int(self.screen_height/30)

        # Bildauswahl
        self.pic_choice_label = QtWidgets.QLabel(self)
        self.pic_choice_label.setText("Bildauswahl:")
        self.pic_choice_label.setGeometry(self.label_start_x, int(self.label_start_y - 0.8*self.label_height) , 2*self.label_space + self.label_width, self.label_height)
        self.pic_choice_label.setStyleSheet("font-size: 18px;")


        self.nine_label = QtWidgets.QLabel(self)
        self.nine_label_pic_path = os.path.join(graf_dir, "Zahlen 9.jpg")
        self.nine_label_pic = QtGui.QPixmap(self.nine_label_pic_path)
        self.nine_label_pic.scaled(self.label_width, self.label_height)
        self.nine_label_pic = QtGui.QPixmap(self.label_width, self.label_height)
        self.nine_label.setPixmap(self.nine_label_pic)
        self.nine_label.setGeometry(self.label_start_x, self.label_start_y, self.label_width,
                                    self.label_height)

        self.nine_button = QRadioButton("9er Quadrat", self)
        self.nine_button.setGeometry(self.label_start_x, self.label_start_y + int(0.9*self.label_height) + self.button_height, self.label_width, self.button_height)

        self.sixteen_label = QtWidgets.QLabel(self)
        self.sixteen_label_pic_path = os.path.join(graf_dir, "Zahlen 16.jpg")
        self.sixteen_label_pic = QtGui.QPixmap(self.sixteen_label_pic_path)
        self.sixteen_label_pic.scaled(self.label_width, self.label_height)
        self.sixteen_label_pic = QtGui.QPixmap(self.label_width, self.label_height)
        self.sixteen_label.setPixmap(self.sixteen_label_pic)
        self.sixteen_label.setGeometry(self.label_start_x + self.label_space, self.label_start_y, self.label_width,
                                       self.label_height)

        self.sixteen_button = QRadioButton("16er Quadrat", self)
        self.sixteen_button.setGeometry(self.label_start_x + self.label_space, self.label_start_y + int(0.9*self.label_height) + self.button_height, self.label_width, self.button_height)

        self.abc_label = QtWidgets.QLabel(self)
        self.abc_label_pic_path = os.path.join(graf_dir, "ABC Puzzle.jpg")
        self.abc_label_pic = QtGui.QPixmap(self.abc_label_pic_path)
        self.abc_label_pic.scaled(self.label_width, self.label_height)
        self.abc_label_pic = QtGui.QPixmap(self.label_width, self.label_height)
        self.abc_label.setPixmap(self.abc_label_pic)
        self.abc_label.setGeometry(self.label_start_x + 2*self.label_space, self.label_start_y, self.label_width,
                                    self.label_height)

        self.abc_button = QRadioButton("ABC Quadrat", self)
        self.abc_button.setGeometry(self.label_start_x + 2*self.label_space, self.label_start_y + int(0.9*self.label_height) + self.button_height, self.label_width, self.button_height)

        self.dir_label = QtWidgets.QLabel(self)
        self.dir_label_pic_path = os.path.join(graf_dir,"lieblingsordner.png" )
        self.dir_label_pic = QtGui.QPixmap(self.dir_label_pic_path)
        self.dir_label_pic.scaled(self.label_width, self.label_height)
        self.dir_label_pic = QtGui.QPixmap(self.label_width, self.label_height)
        self.dir_label.setPixmap(self.dir_label_pic)
        self.dir_label.setGeometry(self.label_start_x, int(self.label_start_y + 1*self.label_space), self.label_width, self.label_height)

        self.dir_path = QTextEdit(self)
        self.dir_path.setGeometry(self.label_start_x + self.label_space, int(self.label_start_y + 0.5*self.label_height + self.label_space - 0.5*self.text_height),
                                   self.label_width + self.label_space, self.text_height)
        self.dir_path.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dir_path.setText(f'best of puzzles')

        self.dir_button = QRadioButton("Zufallsbild aus Lieblingsordner", self)
        self.dir_button.setGeometry(self.label_start_x, self.label_start_y + self.label_space + int(0.9*self.label_height) + self.button_height, 2*self.label_width, self.button_height)
        self.dir_button.setChecked(True)

        self.pic_label = QtWidgets.QLabel(self)
        self.pic_label_pic_path = os.path.join(graf_dir,"lieblingsbild.png" )
        self.pic_label_pic = QtGui.QPixmap(self.pic_label_pic_path)
        self.pic_label_pic.scaled(self.label_width, self.label_height)
        self.pic_label_pic = QtGui.QPixmap(self.label_width, self.label_height)
        self.pic_label.setPixmap(self.pic_label_pic)
        self.pic_label.setGeometry(self.label_start_x, int(self.label_start_y + 2*self.label_space), self.label_width, self.label_height)


        self.pic_path = QTextEdit(self)
        self.pic_path.setGeometry(self.label_start_x + self.label_space, int(self.label_start_y + 2.1*self.label_height + self.label_space - 0.5*self.text_height),
                                   self.label_width + self.label_space, self.text_height)
        self.pic_path.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.pic_button = QRadioButton("Bild der Wahl", self)
        self.pic_button.setGeometry(self.label_start_x, int(self.label_start_y + 2*self.label_space)+ int(0.9*self.label_height) + self.button_height, 2*self.label_height, self.button_height)


        # Dimensionen der Spielbuttons
        self.start_button_height = 40
        self.start_button_space = int(1.5 * self.start_button_height)
        self.start_button_y = int(0.5 * self.screen_height) + int(4.2*self.start_button_space) + 15
        self.start_button_width = 2*self.label_space + self.label_width

        # Spielwahl
        self.start_label = QtWidgets.QLabel(self)
        self.start_label.setText("Einzel-Spielauswahl:")
        self.start_label.setGeometry(self.label_start_x, self.start_button_y - int(0.8*self.start_button_space), self.start_button_width, self.start_button_height)
        self.start_label.setStyleSheet("font-size: 18px;")

        self.puzzle_start = QPushButton("Puzzle", self)
        self.puzzle_start.setGeometry(self.label_start_x, self.start_button_y-10, self.start_button_width, self.start_button_height)
        self.puzzle_start.setCheckable(True)
        self.puzzle_start.setStyleSheet(
            ":checked{background: solid lightgreen}"
            ":checked{border: 4px solid red}"
            ":!checked{background-color: rgb(255,255,255)}"
            ":!checked{border: 4px solid lightgreen}"
            ":!checked{font-size: 13px}"
        )

        self.blind = QCheckBox("blind", self)
        self.blind.setGeometry(self.label_start_x, self.start_button_y + int(0.6*self.start_button_space), 2*self.label_width, self.button_height)
        self.blind.setAutoExclusive(False)
        self.blind.setChecked(False)

        self.slider_start = QPushButton("Slider", self)
        self.slider_start.setGeometry(self.label_start_x, self.start_button_y + int(1.1*self.start_button_space), self.start_button_width, self.start_button_height)
        self.slider_start.setCheckable(True)
        self.slider_start.setStyleSheet(
            ":checked{background: solid lightblue}"
            ":checked{border: 4px solid red}"
            ":!checked{background-color: rgb(255,255,255)}"
            ":!checked{border: 4px solid lightblue}"
            ":!checked{font-size: 13px}"
        )

        self.shuffle = QCheckBox("Shuffle", self)
        self.shuffle.setGeometry(self.label_start_x, self.start_button_y + int(1.85*self.start_button_space), 2*self.label_width, self.button_height)
        self.shuffle.setAutoExclusive(False)
        self.shuffle.setChecked(False)

        self.pictris_start = QPushButton("Pictris", self)
        self.pictris_start.setGeometry(self.label_start_x, self.start_button_y + int(2.3*self.start_button_space), self.start_button_width, self.start_button_height)
        self.pictris_start.setCheckable(True)
        self.pictris_start.setStyleSheet(
            ":checked{background: solid yellow}"
            ":checked{border: 4px solid red}"
            ":!checked{background-color: rgb(255,255,255)}"
            ":!checked{border: 4px solid yellow}"
            ":!checked{font-size: 13px}"
        )

        # GT-Mode
        self.gt_mode = False
        self.gt_offset = 2*self.start_button_height
        self.gt_button_size = 3 * self.start_button_height

        self.start_label = QtWidgets.QLabel(self)
        self.start_label.setText("GT-Mode:")
        self.start_label.setGeometry(self.label_start_x, int(0.5 * self.screen_height) - self.gt_offset, self.start_button_width, self.start_button_height)
        self.start_label.setStyleSheet("font-size: 18px;")

        self.gt_start = QPushButton("Start", self)
        self.gt_start.setGeometry(self.label_start_x + self.gt_button_size, int(0.5 * self.screen_height) - self.start_button_height, self.gt_button_size, self.gt_button_size)
        self.gt_start.setCheckable(True)
        self.gt_start.setStyleSheet(
            ":checked{background: rgb(190,255,190)}"
            ":checked{border: 10px solid lightblue}"
            f':checked{{border-radius: {self.gt_button_size/2}}}'
            ":checked{color: black}"
            ":!checked{background-color: red}"
            ":!checked{border: 10px solid black}"
            f':!checked{{border-radius: {self.gt_button_size/2}}}'            
            ":!checked{font-size: 15px}"
            ":!checked{font-weight: bold}"            
            ":!checked{color: white}"
        )

        self.player_label = QtWidgets.QLabel(self)
        self.player_label.setText("Spieler:")
        self.player_label.setGeometry(QtCore.QRect(self.label_start_x + int(1.1 * self.label_space),
                                             int(0.5 * self.screen_height) - int(1.2*self.gt_offset),
                                             int(self.start_button_width / 4),
                                             self.start_button_height - 15))
        self.player_label.setStyleSheet("font-size: 12px;"
                               "font-weight: bold;")

        self.player = QtWidgets.QComboBox(self)
        self.player.setGeometry(QtCore.QRect(self.label_start_x + int(1.1*self.label_space), int(0.5 * self.screen_height) - self.gt_offset+10, int(self.start_button_width/4),
                             self.start_button_height-15))
        self.player.setEditable(True)
        self.player.setObjectName("Spieler")

        self.race_flag = QtWidgets.QLabel(self)
        self.race_flag_pic_path = os.path.join(graf_dir, "race_start")
        self.race_flag_pic = QtGui.QPixmap(self.race_flag_pic_path)
        self.race_flag_pic.scaled(self.label_width, self.label_height)
        self.race_flag_pic = QtGui.QPixmap(self.label_width, self.label_height)
        self.race_flag.setPixmap(self.race_flag_pic)
        self.race_flag.setGeometry(self.label_start_x + int(2.3*self.gt_button_size), int(0.5 * self.screen_height) - self.gt_offset - 15, self.label_width,
                                    self.label_height)

        #Rundenvorwahl (rpg = rounds per game)
        self.rpg_label = QtWidgets.QLabel(self)
        self.rpg_label.setText("Runden je Spiel:")
        self.rpg_label.setGeometry(self.label_start_x, int(0.5 * self.screen_height - self.start_button_height/2), int(self.start_button_width/3 - 10),
                             self.start_button_height-10)
        self.rpg_label.setStyleSheet("font-size: 12px;"
                                     "font-weight: bold;"
                                     )

        self.rpg = QSpinBox(self)
        self.rpg.setRange(1, 5)
        self.rpg.setWrapping(True)
        self.rpg.setPrefix("Runden = ")
        self.rpg.setStyleSheet("font-size: 12px;"
                               "font-weight: bold;")
        self.rpg.setGeometry(self.label_start_x, int(0.5 * self.screen_height) + 8, int(self.start_button_width/3 - 10),
                             self.start_button_height-15)

        self.gt_onoff_label = QtWidgets.QLabel(self)
        self.gt_onoff_label.setText("GT an/aus")
        self.gt_onoff_label.setGeometry(QtCore.QRect(self.label_start_x + int(1.2 * self.label_space),
                                             int(0.5 * self.screen_height) + int(0.9*self.label_height),
                                             int(self.start_button_width / 4),
                                             self.start_button_height - 15))
        self.gt_onoff_label.setStyleSheet("font-size: 10px;")

        #Hall of Fame Komponenten
        self.call_h_o_f = QPushButton("Hall of Fame", self)
        self. call_h_o_f.setGeometry(self.label_start_x, int(0.5 * self.screen_height) + int(0.9*self.label_height), int(self.start_button_width/3 ),
                             self.start_button_height-15)

        self.fame_save = QPushButton("Save to Fame", self)
        self. fame_save.setGeometry(self.label_start_x + int(2.1*self.gt_button_size)-15, int(0.5 * self.screen_height) + int(0.9*self.label_height), int(self.start_button_width/3 ),
                             self.start_button_height-15)

        #Gesamtpunkte
        self.fullpoints_label = QtWidgets.QLabel(self)
        self.fullpoints_label.setText("Ergebnis-Punkte:")
        self.fullpoints_label.setGeometry(self.label_start_x + int(2.1*self.gt_button_size), int(0.5 * self.screen_height - self.start_button_height/2), int(self.start_button_width/3 ),
                             self.start_button_height-10)
        self.fullpoints_label.setStyleSheet("font-size: 12px;"
                                            "font-weight: bold;"
                                            )

        self.fullpoints = QtWidgets.QLabel(self)
        # self.fullpoints.setText("000 Punkte")
        self.fullpoints.setStyleSheet("font-size: 18px;"
                               "font-weight: bold;")
        self.fullpoints.setGeometry(self.label_start_x + int(2.1*self.gt_button_size), int(0.5 * self.screen_height) + 4, int(self.start_button_width/3 - 10),
                             self.start_button_height-10)


        # Timer
        # Set the necessary variables
        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.count = '00'
        self.startWatch = False

        # Create label to display the watch
        self.timer_label = QLabel(self)
        # Set geometry for the label
        self.timer_label.setGeometry(self.label_start_x + int(2.1*self.gt_button_size),
                                     int(0.5 * self.screen_height) - self.gt_offset, self.label_width + 20,
                                     self.label_height - 30)

        # Create timer object
        timer = QTimer(self)
        # Add a method with the timer
        timer.timeout.connect(self.showCounter)
        # Call start() method to modify the timer value
        timer.start(100)

        #Counter
        self.counter_y = int(0.5 * self.screen_height) + 2 * self.label_height - 5

        self.counter_label = QtWidgets.QLabel(self)
        self.counter_label.setText("Runden \ Punkte:")
        self.counter_label.setGeometry(self.label_start_x, self.counter_y-35, self.start_button_width, self.start_button_height)
        self.counter_label.setStyleSheet("font-size: 18px;")

        self.counter_window = QtWidgets.QLabel(self)
        self.counter_window_path = os.path.join(graf_dir, "fenster")
        self.counter_window_pic = QtGui.QPixmap(self.counter_window_path)
        self.counter_window_pic.scaled(self.start_button_width, int(self.label_height/2))
        self.counter_window_pic = QtGui.QPixmap(self.start_button_width, int(self.label_height/2))
        self.counter_window.setPixmap(self.counter_window_pic)
        self.counter_window.setGeometry(self.label_start_x,
                                   self.counter_y+4, self.start_button_width,
                                   int(self.label_height/2))

        self.counter_start = self.label_start_x+32
        self.counter_space = 32
        self.counter_2_counter = 112
        self.counter_1_1 = QtWidgets.QLabel(self)
        self.counter_1_1.setText('<h2 style="color:white">' + "0" + '</h2>')
        self.counter_1_1.setGeometry(self.counter_start,
                                        self.counter_y, 50,
                                        50)
        self.counter_1_2 = QtWidgets.QLabel(self)
        self.counter_1_2.setText('<h2 style="color:white">' + "00" + '</h2>')
        self.counter_1_2.setGeometry(self.counter_start + self.counter_space,
                                        self.counter_y, 50,
                                        50)

        self.counter_2_1 = QtWidgets.QLabel(self)
        self.counter_2_1.setText('<h2 style="color:white">' + "0" + '</h2>')
        self.counter_2_1.setGeometry(self.counter_start + self.counter_2_counter,
                                        self.counter_y, 50,
                                        50)
        self.counter_2_2 = QtWidgets.QLabel(self)
        self.counter_2_2.setText('<h2 style="color:white">' + "00" + '</h2>')
        self.counter_2_2.setGeometry(self.counter_start + self.counter_2_counter +self.counter_space,
                                        self.counter_y, 50,
                                        50)

        self.counter_3_1 = QtWidgets.QLabel(self)
        self.counter_3_1.setText('<h2 style="color:white">' + "0" + '</h2>')
        self.counter_3_1.setGeometry(self.counter_start + 2*self.counter_2_counter,
                                        self.counter_y, 50,
                                        50)
        self.counter_3_2 = QtWidgets.QLabel(self)
        self.counter_3_2.setText('<h2 style="color:white">' + "00" + '</h2>')
        self.counter_3_2.setGeometry(self.counter_start + 2*self.counter_2_counter +self.counter_space,
                                        self.counter_y, 50,
                                        50)


        # Sound Controls
        self.ambient = QCheckBox("Ambient Sound", self)
        self.ambient.setGeometry(self.label_start_x, self.screen_height - self.start_button_space, 2*self.label_width, self.button_height)
        self.ambient.setAutoExclusive(False)
        self.ambient.setChecked(True)

        self.game_sounds = QCheckBox("Spiel Sounds", self)
        self.game_sounds.setGeometry(self.label_start_x + 3*self.label_width, self.screen_height - self.start_button_space, 2*self.label_width, self.button_height)
        self.game_sounds.setAutoExclusive(False)
        self.game_sounds.setChecked(True)

        self.end_all = QPushButton("Ende", self)
        self.end_all.setGeometry(self.label_start_x + int(1.5*self.label_width), self.screen_height - int(1.1*self.start_button_space), self.label_width, 2*self.button_height)
        self.end_all.setCheckable(True)


        #Kontrollbild hinter Spielfeld
        self.pic_control = QtWidgets.QLabel(self)


        self.game_back2front = QPushButton("Spiel zurück in Vordergrund", self)
        self.game_back2front.setStyleSheet("font-size: 12px;"
                                            "font-weight: bold;")
        self.game_back2front.setGeometry(int(self.screen_width/2), self.label_height, 3*self.label_width, int(self.label_height/4))
        self.game_back2front.hide()


    def showCounter(self):
        # Check the value of startWatch  variable to start or stop the Stop Watch
        if self.startWatch:
            # Increment counter by 1
            self.counter += 1

            # Count and set the time counter value
            cnt = int((self.counter / 10 - int(self.counter / 10)) * 10)
            self.count = '0' + str(cnt)

            # Set the second value
            if int(self.counter / 10) < 10:
                self.second = '0' + str(int(self.counter / 10))
            else:
                self.second = str(int(self.counter / 10))
                # Set the minute value
                if self.counter / 10 == 60.0:
                    #self.second == '00'
                    self.counter = 0
                    min = int(self.minute) + 1
                    if min < 10:
                        self.minute = '0' + str(min)
                    else:
                        self.minute = str(min)

        # Merge the mintue, second and count values
        text = self.minute + ':' + self.second + ':' + self.count
        # Display the stop watch values in the label
        self.timer_label.setText('<h1 style="color:red">' + text + '</h1>')


    def timer_reset(self):
        self.startWatch = False
        # Reset all counter variables
        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.count = '00'
        # Set the initial values for the stop watch
        self.timer_label.setText(str(self.counter))


class HallOfFame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.screen_width, self.screen_height = pyautogui.size()
        self.width = int(self.screen_width/4)
        self.height = int(self.screen_height/2.5)
        #self.statusBar()
        self.setGeometry(0, 0, self.width, self.height)
        self.setWindowTitle('Hall of Fame')
        # layout = QVBoxLayout()
        # self.label_1 = QLabel("Ein-Runden-Rekorde")
        # layout.addWidget(self.label_1)
        # self.label_2 = QLabel("Zwei-Runden-Rekorde")
        # layout.addWidget(self.label_2)
        # self.label_3 = QLabel("Drei-Runden-Rekorde")
        # layout.addWidget(self.label_3)
        # self.setLayout(layout)
        # self.label_4 = QLabel("Vier-Runden-Rekorde")
        # layout.addWidget(self.label_4)



#Anlegen des Fensters mit den Auswhl- und Kontrollfeldern für das Spiel
controlsWindow = Controls()
screen_width = controlsWindow.screen_width
screen_height = controlsWindow.screen_height
controlsWindow.setGeometry(0, 0, screen_width, screen_height)

fameWindow = HallOfFame()
# fameWindow.show()

controlsWindow.timer_label.hide()

# pygame.init()

clock = pygame.time.Clock()

FPS = 60

GRAY = (200, 200, 200)

RED = (255, 0, 0)
#Spielname, Runden, Punkte, Max-Punkte
gt_game_list = [["puzzle", 0, 0, 0], ["slider", 0, 0, 0], ["pictris", 0 ,0, 0]]

#Mindestzahl an Teilen auf der längeren Bildkante
part_anz_min = 4
#Bildabstand vom unteren Rand
offset_y = 55
#Fading-Ausgangswert
alphawert_init = 255
#Steuerung der Geschwindigkeit des Hintergrundbildverschwindens bei Puzzle und Pictris
fade_factor = 0.3
#Kachel wartet bei Pictris vor dem Fall
before_fall_init = 1500
#Zähler für die Verkleinerung der Puzzleteile bei Bildpuzzle und Berechnung der game_id bei GT
game_rounds = 0
# Replay sorgt bei Slider für erneutes Spiel mit gleicher Ausganglage
replay = False

started = False

gt_stop = False

#Bringt das jeweilige Spiel zum Ende
abbruch = False

#Dictionary bewahrt die Zufallskonfiguration des Spielfelds um dieses (vgl replay) in gleicher Form wieder spielen zu können
replay_dict = {}

zugzahl = 0

w_floor, h_floor = screen_width - screen_width // 4, screen_height
game_x = screen_width - w_floor
game_y = screen_height - h_floor - offset_y

pygame.init()

pygame.mixer.music.load(r"Sounds\02 - Abiding Love.mp3")
#Parameter -1 für Dauerschleife
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0)

kachelpasst = pygame.mixer.Sound(r"Sounds\salamisound-3402567-tischglocke-einmal.mp3")
kachelplop = pygame.mixer.Sound(r"Sounds\245645__unfa__cartoon-pop-clean.wav")
kachelfalsch = pygame.mixer.Sound(r"Sounds\salamisound-4681975-kleine-hupe-einmal-kurz.mp3")


font_2 = pygame.font.Font(pygame.font.get_default_font(), 15)
text_surface_3 = pygame.font.Font.render(font_2, f'Abbruch mit Leertaste', True, (55, 55, 55))

def make_game_floor(game):
    global w_floor
    global h_floor
    global game_x
    global game_y
    global screen

    game = "have fun"

    screen = pygame.display.set_mode(size=(w_floor, h_floor))
    screen.fill(GRAY)
    #sorgt dafür, dass das pygame Fenster immer on Top ist (Parameter -1)
    hwnd = pygame.display.get_wm_info()['window']
    user32 = ctypes.WinDLL("user32")
    user32.SetWindowPos.restype = wintypes.HWND
    user32.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, wintypes.INT, wintypes.INT, wintypes.INT,
                                    wintypes.INT, wintypes.UINT]
    user32.SetWindowPos(hwnd, -1, game_x, 0, w_floor, h_floor, 0x0001)

    pygame.display.set_caption(game)
    pygame.display.update()


def start_playing(game):
    global spielbild
    global fade_factor
    global part_size
    global part_anz
    global part_anz_init
    global part_anz_min
    global game_rounds
    global init
    global grid
    global offset_y
    global GRAY
    global RED
    global w_floor
    global h_floor
    global screen
    global screen_width
    global screen_height
    global full_image_x
    global full_image_y
    global font
    global x_anz
    global y_anz
    global replay
    global started
    global fertig
    global gt_stop
    global abbruch
    global gt_game_list
    global planned_rounds

    if init == True and replay == False:
        spielbild = find_pic()
        controlsWindow.pic_path.setText(spielbild)
        part_anz_init = part_anz_min
        game_rounds = 1
    else:
        game_rounds += 1

    if controlsWindow.gt_mode and ceil(game_rounds / planned_rounds) - 1 == len(gt_game_list):
        screen.fill(GRAY)
        pygame.display.update()
        #gt_stop = True
        controlsWindow.startWatch = False
        pygame.mixer.music.fadeout(2000)
        #pygame.mixer.music.set_volume(0)
        return

    if controlsWindow.gt_mode:
        game_id = ceil(game_rounds / planned_rounds) - 1
        print(f'game_id: {game_id}')
        gt_game_list[game_id][1] += 1
        game = gt_game_list[game_id][0]
        uncheck(game)

    if controlsWindow.nine_button.isChecked() == True:
        part_anz = 3

    elif controlsWindow.sixteen_button.isChecked() == True:
        part_anz = 4

    elif controlsWindow.abc_button.isChecked() == True:
        part_anz = 5

    elif controlsWindow.pic_button.isChecked() == True or controlsWindow.dir_button.isChecked() == True:
        if controlsWindow.gt_mode:
            part_anz = part_anz_init + gt_game_list[game_id][1] - 1
        else:
            part_anz = part_anz_init + game_rounds -1

    #Hier wird das oben bestimmte Spielbild in das Spieformat gebracht und in diesem Format als tmp Pic abgelegt
    try:
        image = resize(spielbild)
    except:
        return
    width, height = image.size
    part_size, part_anz = find_part_size(width, height, part_anz)

    #Bestimmung der Position des Gesamtspielbildes
    full_image_x = (w_floor - width) / 2
    full_image_y = h_floor - height - offset_y

    #Berechnung der horizontalen und vertikalen Teilezahl
    x_anz = width // part_size
    y_anz = height // part_size

    pic = pygame.image.load(r"tmp_resize.JPG")

    make_game_floor(game)

    control_pic = QtGui.QPixmap(r"tmp_resize.JPG")
    controlsWindow.pic_control.setGeometry(screen_width - width - offset_y, screen_height - height - offset_y, width, height)
    controlsWindow.pic_control.setPixmap(control_pic)
    controlsWindow.pic_control.show()
    controlsWindow.game_back2front.show()

    grid = make_grid(full_image_x, full_image_y, x_anz, y_anz, part_size)
    full_partsdict = make_full_partsdict(x_anz, y_anz, game)
    font_2 = pygame.font.Font(pygame.font.get_default_font(), 15)
    text_surface_2 = pygame.font.Font.render(font_2, f'Bildwechsel mit Leertaste', True, (55, 55, 55))

    if game_rounds == 1:
        #Hier wird das Spielbild in Position gesenkt
        pic_pos_x = full_image_x
        move = True
        while move == True:
            for pic_pos_y in range (0,full_image_y):

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if move:
                                if controlsWindow.gt_mode:
                                    gt_game_list[game_id][1] -= 1
                                pygame.mixer.music.set_volume(0)
                                return
                            else:
                                pass

                screen.fill(GRAY)
                screen.blit(pic, (pic_pos_x, pic_pos_y))
                if controlsWindow.dir_button.isChecked() == True:
                    screen.blit(text_surface_2, dest=(controlsWindow.screen_width/3, controlsWindow.screen_height - 50))
                pygame.display.update()
                pygame.time.delay(10)
            move = False
            started = True

            if controlsWindow.gt_mode == True:
                controlsWindow.race_flag.hide()
                controlsWindow.timer_label.show()
                controlsWindow.startWatch = True
                controlsWindow.showCounter()
                if controlsWindow.dir_button.isChecked() == True:
                    controlsWindow.pic_button.setChecked(True)
               # controlsWindow.rpg.setDisabled(True)

    if game == "puzzle":
        count = puzzle(full_partsdict, grid)

        if count != None:
            #print(count)
            #gt_game_list[0][1] = gt_game_list[0][1] + 1
            gt_game_list[0][2] = gt_game_list[0][2] + count
            gt_game_list[0][3] = gt_game_list[0][3] + (x_anz*y_anz)
            if controlsWindow.gt_mode:
                controlsWindow.counter_1_1.setText(f'<h1 style="color:white"> {gt_game_list[0][1]} </h1>')
            else:
                controlsWindow.counter_1_1.setText(f'<h1 style="color:white"> {game_rounds} </h1>')

            controlsWindow.counter_1_2.setText(f'<h1 style="color:white"> {gt_game_list[0][2]} </h1>')
        else:
            if controlsWindow.gt_mode:
                game_counter_init()
            else:
                controlsWindow.counter_1_1.setText(f'<h1 style="color:white"> 0 </h1>')
                controlsWindow.counter_1_2.setText(f'<h1 style="color:white"> 00 </h1>')

        if gt_stop or abbruch:
            screen.fill(GRAY)
            pygame.display.update()
            game_counter_init()
            pygame.mixer.music.set_volume(0)
            return

        return

    if game == "slider":
        count = slider(full_partsdict, grid)

        if count != None:
            gt_game_list[1][2] = gt_game_list[1][2] + count
            gt_game_list[1][3] = gt_game_list[1][3] + (x_anz*y_anz)-1
            if controlsWindow.gt_mode:
                controlsWindow.counter_2_1.setText(f'<h1 style="color:white"> {gt_game_list[1][1]} </h1>')
            else:
                controlsWindow.counter_2_1.setText(f'<h1 style="color:white"> {game_rounds} </h1>')

            controlsWindow.counter_2_2.setText(f'<h1 style="color:white"> {gt_game_list[1][2]} </h1>')
        else:
            if controlsWindow.gt_mode:
                game_counter_init()
            else:
                controlsWindow.counter_2_1.setText(f'<h1 style="color:white"> 0 </h1>')
                controlsWindow.counter_2_2.setText(f'<h1 style="color:white"> 00 </h1>')
        return

    if game == "pictris":
        count = pictris(full_partsdict, grid)

        if count != None:
            gt_game_list[2][2] = gt_game_list[2][2] + count
            gt_game_list[2][3] = gt_game_list[2][3] + (x_anz*y_anz)
            if controlsWindow.gt_mode:
                controlsWindow.counter_3_1.setText(f'<h1 style="color:white"> {gt_game_list[2][1]} </h1>')
            else:
                controlsWindow.counter_3_1.setText(f'<h1 style="color:white"> {game_rounds} </h1>')

            controlsWindow.counter_3_2.setText(f'<h1 style="color:white"> {gt_game_list[2][2]} </h1>')
        else:
            if controlsWindow.gt_mode:
                game_counter_init()
            else:
                controlsWindow.counter_3_1.setText(f'<h1 style="color:white"> 0 </h1>')
                controlsWindow.counter_3_2.setText(f'<h1 style="color:white"> 00 </h1>')
        return

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

#setzt die Zähler in der game_list auf Null und schreibt dies in die Ausgabe
def game_counter_init():
    global gt_game_list
    #
    # gt_game_list = [["puzzle", 0, 0], ["slider", 0, 0], ["pictris", 0, 0]]

    gt_game_list[0][1] = 0
    gt_game_list[0][2] = 0
    gt_game_list[0][3] = 0
    # controlsWindow.counter_1_1.setText(f'<h1 style="color:white"> {gt_game_list[0][1]} </h1>')
    # controlsWindow.counter_1_2.setText(f'<h1 style="color:white"> {gt_game_list[0][2]} </h1>')
    gt_game_list[1][1] = 0
    gt_game_list[1][2] = 0
    gt_game_list[1][3] = 0
    # controlsWindow.counter_2_1.setText(f'<h1 style="color:white"> {gt_game_list[1][1]} </h1>')
    # controlsWindow.counter_2_2.setText(f'<h1 style="color:white"> {gt_game_list[1][2]} </h1>')
    gt_game_list[2][1] = 0
    gt_game_list[2][2] = 0
    gt_game_list[2][3] = 0
    # controlsWindow.counter_3_1.setText(f'<h1 style="color:white"> {gt_game_list[2][1]} </h1>')
    # controlsWindow.counter_3_2.setText(f'<h1 style="color:white"> {gt_game_list[2][2]} </h1>')

    controlsWindow.counter_1_1.setText(f'<h1 style="color:white"> 0 </h1>')
    controlsWindow.counter_1_2.setText(f'<h1 style="color:white"> 00 </h1>')

    controlsWindow.counter_2_1.setText(f'<h1 style="color:white"> 0 </h1>')
    controlsWindow.counter_2_2.setText(f'<h1 style="color:white"> 00 </h1>')

    controlsWindow.counter_3_1.setText(f'<h1 style="color:white"> 0 </h1>')
    controlsWindow.counter_3_2.setText(f'<h1 style="color:white"> 00 </h1>')

    controlsWindow.fullpoints.setText("")


def find_part_size(width, height, part_anz):
    global part_anz_init

    if width > height:
        part_size = width // part_anz
        while height // part_size < 3:
            part_anz += 1
            part_anz_init += 1
            part_size = width // part_anz
    else:
        part_size = height // part_anz
        while width // part_size < 3:
            part_anz += 1
            part_anz_init += 1
            part_size = height // part_anz

    return(part_size, part_anz)

def uncheck(game):

    controlsWindow.puzzle_start.setChecked(False)
    controlsWindow.slider_start.setChecked(False)
    controlsWindow.pictris_start.setChecked(False)
    if game == "puzzle":
        controlsWindow.puzzle_start.setChecked(True)
    elif game == "slider":
        controlsWindow.slider_start.setChecked(True)
    elif game == "pictris":
        controlsWindow.pictris_start.setChecked(True)


def game_sounds():
    if controlsWindow.game_sounds.isChecked() == True:
        kachelpasst.set_volume(1)
        kachelplop.set_volume(1)
        kachelfalsch.set_volume(1)
    else:
        kachelpasst.set_volume(0)
        kachelplop.set_volume(0)
        kachelfalsch.set_volume(0)

def ambient_sound():
    if controlsWindow.ambient.isChecked() == True:
        #game_ambient.set_volume(0.1)
        pygame.mixer.music.set_volume(0.1)
    else:
        #game_ambient.set_volume(0)
        pygame.mixer.music.set_volume(0)


def resize(file):

    fixed_height = 650
    image = Image.open(file)
    height_percent = (fixed_height / float(image.size[1]))
    width_size = int((float(image.size[0]) * float(height_percent)))
    image = image.resize((width_size, fixed_height), Image.NEAREST)
    image.save(r"tmp_resize.JPG")

    return(image)


abbruch = False
def puzzle(full_partsdict, grid):
    global alphawert_init
    global game_rounds
    global fade
    global w_floor
    global h_floor
    global x_anz
    global y_anz
    global init
    global fade_factor
    global partslist
    global GRAY
    global RED
    global counter
    global fertig
    global font
    global replay
    global zugzahl
    global gt_stop
    global started
    global abbruch



    act_partsdict = {}

    parts_list = []

    fertig = False

    #if init == True:
    counter = 0

    #alpha_step = alphawert_init // (x_anz*y_anz)
    alphawert = alphawert_init

    sliding = False

    zugzahl = 0

    font = pygame.font.Font(pygame.font.get_default_font(), 36)

    fertig = False

    act_partsdict = make_full_partsdict(x_anz, y_anz,"puzzle")

    #Bestimmung der Koordinaten der oberen linken Ecke des Spielbilds
    full_image_x= full_partsdict[0, 0][1][0]
    full_image_y = full_partsdict[0,0][1][1]

    screen.fill(GRAY)
    x = random.randint(0, x_anz-1)
    y = random.randint(0, y_anz-1)
    img = act_partsdict[x,y][0]
    img.set_alpha(255)
    rect = img.get_rect()
    rect.center = w_floor // 2, full_image_y // 2

    pygame.display.flip()

    #pygame.mixer.Sound.play(game_ambient)
    # pygame.mixer.music.play(-1)

    running = True
    while running:
        if gt_stop == True:
            break
            #return(counter)
        screen.fill(GRAY)

        ambient_sound()
        game_sounds()

        #Ausgabe langsam verblassender Hintergrund oder blank bei "blind-mode"
        if controlsWindow.blind.isChecked() == True:
            alphawert = 0
            alpha = 0
        else:
            alpha = 255
        for key, value in full_partsdict.items():
            if zugzahl == 0:
                value[0].set_alpha(alpha)
                screen.blit(value[0], value[1])
            else:
                value[0].set_alpha(alphawert)
                screen.blit(value[0], value[1])
        #Ausgabe korrekter Puzzelteile
        for key, value in act_partsdict.items():
            if key in parts_list:
                value[0].set_alpha(255)
                screen.blit(value[0], value[1])

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    if started and not controlsWindow.gt_mode:
                        fertig = True
                        game_rounds = 0
                        counter = 0
                        init = True
                        replay = False
                        started = False
                        fertig = True
                        abbruch = True
                        pygame.mixer.music.set_volume(0)
                        return
                    else:
                        pass

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    sliding = True
                    #print("Buttondown angenommen")


            elif event.type == pygame.MOUSEMOTION and sliding == True:
                if fertig == False:
                    rect.move_ip(event.rel)
                    #Kachel in den Grenzen des Spielfelds halten
                    if rect.x < full_image_x:
                        rect.x = full_image_x
                    if rect.x > (full_image_x + (x_anz-1)*part_size):
                        rect.x = (full_image_x + (x_anz-1)*part_size)
                    if rect.y < 0:
                        rect.y = 0
                    if rect.y > (full_image_y + (y_anz-1)*part_size):
                        rect.y = (full_image_y + (y_anz-1)*part_size)

            elif event.type == pygame.MOUSEBUTTONUP:
                zugzahl += 1

                # wo wurde das Teil abgelegt
                drop_x, drop_y = rect.center

                # find Ablage x, y
                x_neu = int(drop_x - full_image_x) // part_size
                y_neu = int(drop_y - full_image_y) // part_size
                #print(f'{x_neu} / {y_neu}')
                if (x_neu < 0 or x_neu > x_anz-1) or (y_neu < 0 or y_neu > y_anz-1):
                    pass
                else:
                    if act_partsdict[x,y][3] == full_partsdict[x_neu, y_neu][3]:
                        coord_neu = x_neu, y_neu
                        parts_list.append(coord_neu)
                        success(1)

                        counter += 1

                        for i in range(0,30):
                            blit_grid(grid, (255,255,255))
                            pygame.display.flip()

                        if len(parts_list) == (y_anz * x_anz):
                            fertig = True
                            init = False
                            #text_surface = pygame.font.Font.render(font, f'Punkte: {counter}', True, (55, 55, 55))
                            #screen.blit(text_surface, dest=(50, 50))
                            for key, value in act_partsdict.items():
                                screen.blit(value[0], value[1])
                            text_surface = pygame.font.Font.render(font, f'Punkte: {counter} von {x_anz*y_anz}', True, (55, 55, 55))
                            screen.blit(text_surface, dest=(50, 50))
                            pygame.display.flip()
                            success(6)
                            #counter = 0
                            return(counter)
                    else:
                        counter -= 1
                        pygame.mixer.Sound.play(kachelfalsch)
                        if controlsWindow.blind.isChecked() == True:
                            screen.fill(GRAY)
                            for key, value in act_partsdict.items():
                                if key in parts_list:
                                    value[0].set_alpha(75)
                                    screen.blit(value[0], value[1])
                            blit_grid(grid, (255,255,0))
                            full_partsdict[x_neu, y_neu][0].set_alpha(255)
                            screen.blit(full_partsdict[x_neu, y_neu][0], full_partsdict[x_neu, y_neu][1])
                            pygame.display.flip()
                            pygame.time.delay(1100)
                            for key, value in act_partsdict.items():
                                value[0].set_alpha(255)


                    if fertig == False:
                        x = random. randint(0,x_anz-1)
                        y = random. randint(0,y_anz-1)

                        while (x,y) in parts_list:
                            x = random.randint(0, x_anz-1)
                            y = random.randint(0, y_anz-1)

                        img = act_partsdict[x, y][0]

                        rect = img.get_rect()
                        rect.center = w_floor // 2, full_image_y // 2
                    sliding = False

                    # Ausblenden des Hintergrunds (erst schneller, dann langsam
                    #abzug = game_rounds*alpha_step + (alpha_step)**(fade_factor/zugzahl)
                    anz = x_anz*y_anz
                    abzug = ((alphawert_init / ((anz - (anz*fade_factor))**0.5) * (zugzahl**0.5)))
                    alphawert = alphawert_init - abzug
                    if alphawert <= 5:
                        alphawert = 5
                    #print(f'Zugzahl: {zugzahl}  Abzug: {abzug}  Alphawert: {alphawert}')

        if gt_stop:
            return

        screen.blit(img, rect)

        text_surface = pygame.font.Font.render(font, f'Punkte: {counter} von {x_anz * y_anz}', True, (55, 55, 55))
        screen.blit(text_surface, dest=(50, 50))

        # font_2 = pygame.font.Font(pygame.font.get_default_font(), 15)
        # text_surface_3 = pygame.font.Font.render(font_2, f'Abbruch mit Leertaste', True, (55, 55, 55))
        if not controlsWindow.gt_mode:
            screen.blit(text_surface_3, dest=(controlsWindow.screen_width / 3, controlsWindow.screen_height - 50))

        pygame.draw.rect(screen, RED, rect, 1)

        blit_grid(grid, RED)
        pygame.display.update()


def part_fall(img, full_partsdict, x, y, act_partsdict, alphawert):
    global x_anz
    global y_anz
    global part_size
    global full_image_x
    global full_image_y
    global game_rounds
    global replay
    global fits
    global fails
    global punkte
    global parts
    global init
    global started
    global abbruch

    fertig = False
    abbruch = False
    parts += 1

    blit_field(full_partsdict, act_partsdict, alphawert)
    text_surface = pygame.font.Font.render(font, f'Punkte: {punkte} von {x_anz*y_anz}', True, (55, 55, 55))
    screen.blit(text_surface, dest=(50, 50))
    #pygame.display.flip()

    # Hier wird das Spielteil gesenkt
    start_pos_x = (full_image_x + int(x_anz*part_size/2 - part_size/2))
    start_pos_Y = (full_image_y // 2) - int(part_size / 2)

    pic_pos_x = start_pos_x
    max_pos_y = full_partsdict[x_anz-1, y_anz-1][1][1]

    move = True

    x_change = 0

    while move == True:
        for pic_pos_y in range(start_pos_Y, max_pos_y+1):
            stop = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_SPACE:
                        if started and not controlsWindow.gt_mode:
                            fertig = False
                            game_rounds = 0
                            counter = 0
                            init = True
                            replay = False
                            started = False
                            abbruch = True
                            pygame.mixer.music.set_volume(0)
                        else:
                            pass

                    if event.key == pygame.K_RIGHT:
                        x_change += 1
                        pic_pos_x_old = pic_pos_x
                        pic_pos_x = full_image_x + math.floor((pic_pos_x + part_size - full_image_x) / part_size) * part_size
                        x_act = (pic_pos_x - full_image_x) / part_size
                        y_act = math.floor((pic_pos_y - full_image_y) // part_size)
                        if x_act > x_anz-1:
                            pic_pos_x = pic_pos_x_old
                        elif (x_act, y_act) in act_partsdict.keys() or(x_act, y_act+1) in act_partsdict.keys():
                            pic_pos_x = pic_pos_x_old
                    if event.key == pygame.K_LEFT:
                        x_change += 1
                        pic_pos_x_old = pic_pos_x
                        pic_pos_x = full_image_x + math.ceil((pic_pos_x - part_size - full_image_x) / part_size) * part_size
                        x_act = (pic_pos_x - full_image_x) / part_size
                        y_act = math.floor((pic_pos_y - full_image_y) // part_size)
                        if x_act < 0:
                            pic_pos_x = pic_pos_x_old
                        elif (x_act, y_act) in act_partsdict.keys() or(x_act, y_act+1) in act_partsdict.keys():
                            pic_pos_x = pic_pos_x_old

                    if event.key == pygame.K_UP:
                        #Funktioniert nur wenn rechtzeitig vor Eintritt ins Spielfeld gedrückt
                        if (full_image_y - (pic_pos_y + part_size)) > 0:
                            #Check ob passende Kachel weggedrückt
                            fits_old = fits
                            act_partsdict_old = act_partsdict.copy()
                            for x_check in range(0, x_anz):

                                pic_pos_x = full_image_x + x_check*part_size
                                for y_check in range(0,y_anz):
                                    pic_pos_y = full_image_y + y_check*part_size
                                    stop, fertig, act_partsdict = place_check(x, y, pic_pos_x, pic_pos_y, x_change,
                                                                                  full_partsdict, act_partsdict, alphawert)

                                    if fits > fits_old:
                                        # print("zu schnell gedrückt")
                                        # print(f'fits: {fits} / fits_old: {fits_old}')
                                        # print(f'x_check: {x_check} / y_check: {y_check}')

                                        break
                                    else:
                                        y_check += 1
                                        # print(f'fits: {fits} / fits_old: {fits_old}')
                                        # print(f'x_check: {x_check} / y_check: {y_check}')


                                if fits > fits_old:
                                    break
                                else:
                                    x_check += 1

                            if fits > fits_old:
                                fits = fits_old
                                fails += 1
                                pygame.mixer.Sound.play(kachelfalsch)
                                act_partsdict = act_partsdict_old.copy()
                            else:
                                pygame.mixer.Sound.play(kachelplop)
                            fertig = False
                            stop = True

                    if event.key == pygame.K_DOWN:
                        for pic_pos_y in range(full_image_y, (full_image_y + y_anz*part_size)):
                            # Check bei jedem vollen y-Wert
                            fits_old = fits
                            if ((pic_pos_y - full_image_y) % part_size) == 0:
                                stop, fertig, act_partsdict = place_check(x, y, pic_pos_x, pic_pos_y, x_change, full_partsdict, act_partsdict, alphawert)

                                if stop:
                                    if fits == fits_old:
                                        fails += 1
                                    break
                            pic_pos_y += 1


            # Check bei jedem vollen y-Wert
            if not stop:
                if ((pic_pos_y - full_image_y) % part_size) == 0:
                    fits_old = fits
                    stop, fertig, act_partsdict = place_check(x, y, pic_pos_x, pic_pos_y, x_change, full_partsdict, act_partsdict, alphawert)
                    if stop:
                        #Abzug wg ohne Treffer durchgelaufen
                        if fits == fits_old:
                            fails += 1
                            if not abbruch:
                                pygame.mixer.Sound.play(kachelfalsch)

            punkte = fits - fails

            blit_field(full_partsdict, act_partsdict, alphawert)

            img.set_alpha(255)
            screen.blit(img, (pic_pos_x, pic_pos_y))
            blit_grid(grid, RED)

            text_surface = pygame.font.Font.render(font, f'Punkte: {punkte} von {x_anz * y_anz} aus {parts}', True, (55, 55, 55))
            screen.blit(text_surface, dest=(50, 50))

            if not controlsWindow.gt_mode:
                screen.blit(text_surface_3, dest=(controlsWindow.screen_width / 3, controlsWindow.screen_height - 50))

            pygame.display.update()

            if fertig:
                success(8)
                #punkte = 0
                act_partsdict.clear()
                pygame.time.delay(1000)
                stop = True

            if stop:
                break

        move = False

    return(act_partsdict, fertig, punkte)

#prüft ob die Kachel kollidiert und wenn ja ob sie an passender Stelle liegt
def place_check(x, y, pic_pos_x, pic_pos_y, x_change, full_partsdict, act_partsdict, alphawert):
    global fits
    global fails

    stop = False
    fertig = False

    x_act = math.floor((pic_pos_x - full_image_x) / part_size)
    y_act = math.floor((pic_pos_y - full_image_y) / part_size)

    # Wenn Sprite nicht auf Feld ausgerichtet oder durch Bewegung dazu eingenordet wurde
    if (x_anz % 2) == 0 and x_change == 0:
        # wenn Sprite mittig über Grid-Linie startet und mit der einen oder anderen Hälfte eine Kollision verursacht
        if ((x_act, y_act + 1) in act_partsdict.keys() or (
        x_act + 1, y_act + 1) in act_partsdict.keys()) or y_act == y_anz - 1:
            stop = True

    # Kollision oder unterer Rand erreicht?
    if ((x_act, y_act + 1) in act_partsdict.keys()) or (y_act + 1 == y_anz):
        #Kollision mit oberster Reihe (kann nix passen)
        if y_act < 0:
            stop = True
        # passt?
        elif full_partsdict[x_act, y_act][3] == full_partsdict[x, y][3]:
            act_partsdict[x, y] = full_partsdict[x, y]
            stop = True
            fits += 1

            if len(act_partsdict) == len(full_partsdict):
                fertig = True
            else:
                success(1)
        # passt nicht, nur Kollision
        else:
            stop = True

    return(stop, fertig, act_partsdict)


def blit_field(full_partsdict, act_partsdict, alphawert):
    screen.fill(GRAY)
    for key, value in full_partsdict.items():
        value[0].set_alpha(alphawert)
        screen.blit(value[0], value[1])
    for key, value in act_partsdict.items():
        value[0].set_alpha(255)
        screen.blit(value[0], value[1])

def pictris(full_partsdict, grid):
    global spielbild
    global alphawert_init
    global game_rounds
    global w_floor
    global h_floor
    global x_anz
    global y_anz
    global init
    global RED
    global fertig
    global font
    global replay
    global fits
    global fails
    global punkte
    global parts
    global before_fall_init
    global started
    global abbruch

    act_partsdict = {}

    fertig = False

    if init == True:
        counter = 0
        punkte = 0
        parts = 0
        fits = 0
        fails = 0

    moving = False
    started = False

    font = pygame.font.Font(pygame.font.get_default_font(), 36)

    running = True
    while running:
        if abbruch:
            return
        if not started:
            counter = 0
            punkte = 0
            alphawert = 45
            parts = 0
            fits = 0
            fails = 0
            started = True

            screen.fill(GRAY)

            x, y = make_randpos(act_partsdict)
            img = full_partsdict[x, y][0]

            before_fall = before_fall_init - int(fits * (before_fall_init - 150) / (x_anz * y_anz))

            blit_field(full_partsdict, act_partsdict, alphawert)
            img.set_alpha(255)
            start_pos_x = (full_image_x + int(x_anz * part_size / 2 - part_size / 2))
            start_pos_Y = (full_image_y // 2) - int(part_size / 2)
            screen.blit(img, (start_pos_x, start_pos_Y))
            blit_grid(grid, RED)
            if not controlsWindow.gt_mode:
                screen.blit(text_surface_3, dest=(controlsWindow.screen_width / 3, controlsWindow.screen_height - 50))
            pygame.display.update()

            # Kachel wird für spezifizierte Zeit vor Fall gezeigt
            pygame.time.delay(before_fall)

            act_partsdict, fertig, punkte = part_fall(img, full_partsdict, x, y, act_partsdict, alphawert)

            x, y = make_randpos(act_partsdict)
            img = full_partsdict[x, y][0]

        else:
            alphawert = 45

        if started:
            before_fall = before_fall_init - int(fits*(before_fall_init-150)/(x_anz*y_anz))
            blit_field(full_partsdict, act_partsdict, alphawert)
            img.set_alpha(255)
            start_pos_x = (full_image_x + int(x_anz * part_size / 2 - part_size / 2))
            start_pos_Y = (full_image_y // 2) - int(part_size / 2)
            screen.blit(img, (start_pos_x, start_pos_Y))
            blit_grid(grid, RED)

            if not controlsWindow.gt_mode:
                screen.blit(text_surface_3, dest=(controlsWindow.screen_width / 3, controlsWindow.screen_height - 50))

            pygame.display.update()
            #Kachel wird für spezifizierte Zeit vor Fall gezeigt
            pygame.time.delay(before_fall)

            #Kachelfalldurchlauf
            act_partsdict, fertig, punkte= part_fall(img, full_partsdict, x, y, act_partsdict, alphawert)
            if fertig:
                replay = True
                init = False
                started = False
                #game_ambient.set_volume(0)
                #start_playing("pictris")
                return(punkte)

            blit_field(full_partsdict, act_partsdict, alphawert)
            #Neue Kachel erzeugen wenn nicht fertig
            x, y = make_randpos(act_partsdict)
            img = full_partsdict[x, y][0]

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

                if event.key == pygame.K_SPACE:
                    if started and not controlsWindow.gt_mode:
                        fertig = True
                        game_rounds = 0
                        counter = 0
                        punkte = 0
                        parts = 0
                        fits = 0
                        fails = 0
                        init = True
                        replay = False
                        started = False
                        abbruch = True
                        pygame.mixer.music.set_volume(0)
                        return
                    else:
                        pass

                if event.key == pygame.K_RETURN:
                    counter = 0
                    punkte = 0
                    alphawert = 45
                    parts = 0
                    fits = 0
                    fails = 0
                    started = True
                    pygame.time.delay(before_fall_init)

                    pygame.mixer.music.set_volume(0.1)

                    act_partsdict, fertig, punkte= part_fall(img, full_partsdict, x, y, act_partsdict, alphawert)

                    x, y = make_randpos(act_partsdict)
                    img = full_partsdict[x, y][0]

        img.set_alpha(255)
        screen.blit(img, (start_pos_x, start_pos_Y))
        blit_grid(grid, RED)
        pygame.display.update()

# Sucht aus den noch unbenutzten Kacheln das nächste Angebot aus
def make_randpos(act_partsdict):

    x = random.randint(0, x_anz - 1)
    y = random.randint(0, y_anz - 1)
    while (x, y) in act_partsdict.keys():
        x = random.randint(0, x_anz - 1)
        y = random.randint(0, y_anz - 1)

    return(x,y)

#Kopiert das Vollbild-Dictionary auf das Arbeits-Dictionary
def copy_full_partsdict(full_partsdict):
    act_partsdict = {}

    for key, value in full_partsdict.items():
        act_partsdict[key] = full_partsdict[key]

    return(act_partsdict)


def slider(full_partsdict, grid):
    global w_floor
    global h_floor
    global full_image_x
    global full_image_y
    global x_anz
    global y_anz
    global part_anz
    global replay
    global replay_dict
    global init
    global started
    global abbruch

    sender = controlsWindow.sender()
    spiel = sender.text()
    #print(f'Spiel: {spiel}')

    font = pygame.font.Font(pygame.font.get_default_font(), 36)

    moving = False
    fertig = False
    #Zugzahl
    counter = 0

    # Dictonary hat als Key die x,y Werte aus full_partsdict und als Value das Image und dessen aktuelle Koordinaten auf dem Spielfeld
    act_pos_dict = {}
    # Wird mit initialem Bild befüllt zum Check ob Slider-Teil passt
    check_pos_dict = {}

    running = True

    if replay == False:
        replay_dict = {}
        lösbar = False
        while lösbar == False:
            rand_values = []
            # Aus den Bildteilen ein Puzzle machen
            for key, value in full_partsdict.items():
                #letztes Feld leer lassen
                if key == (x_anz-1,y_anz-1):
                    continue

                rand_x = random.randint(0, x_anz-1)
                rand_y = random.randint(0, y_anz-1)
                randpos = [rand_x, rand_y]

                #Vermeidung von Koordinaten-Dopplern
                while randpos in rand_values or randpos == [0, 0]:
                    rand_x = random.randint(0, x_anz-1)
                    rand_y = random.randint(0, y_anz-1)
                    randpos = [rand_x, rand_y]

                #Ordnungsnummer des Zufallsquadrats
                rand_order = rand_y * x_anz + rand_x + 1
                rand_values.append(randpos)

                rand_pos_x = full_image_x + rand_x * part_size
                rand_pos_y = full_image_y + rand_y * part_size

                rand_coord = (rand_pos_x, rand_pos_y)

                act_pos_dict[(rand_x, rand_y)] = (value[0], rand_coord, rand_order, value[3])
                replay_dict[(rand_x, rand_y)] = (value[0], rand_coord, rand_order, value[3])

            lösbar = check_solvability(act_pos_dict, x_anz, y_anz)

    else:
        act_pos_dict = replay_dict.copy()
        #print(f'Replay {replay}')

    if controlsWindow.shuffle.isChecked() == True:
        counter_name = "Punkte"
    else:
        counter_name = "Züge"


    screen.fill(GRAY)
    for key, value in act_pos_dict.items():
        screen.blit(value[0], value[1])
        check_pos_dict[key] = (value[0], value[1])
    blit_grid(grid, (255,0,0))
    text_surface = pygame.font.Font.render(font, f'{counter_name}: {counter}', True, (55, 55, 55))
    screen.blit(text_surface, dest=(50, 50))
    pygame.display.flip()

    #pygame.mixer.Sound.play(game_ambient)
    #pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)

    while running:
        if controlsWindow.shuffle.isChecked() == True:
            counter_name = "Punkte"
        else:
            counter_name = "Züge"

        game_sounds()
        ambient_sound()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    # game_rounds = 1
                    # counter = 0
                    # init = True
                    # replay = False
                    # return
                    if started and not controlsWindow.gt_mode:
                        fertig = True
                        game_rounds = 0
                        counter = 0
                        init = True
                        replay = False
                        started = False
                        fertig = True
                        abbruch = True
                        pygame.mixer.music.set_volume(0)
                        return
                    else:
                        pass

            elif event.type == pygame.MOUSEBUTTONDOWN:
                eventpos_x, eventpos_y = event.pos
                # find x, y
                x_wert = int(eventpos_x - full_image_x) // part_size
                y_wert = int(eventpos_y - full_image_y) // part_size
                #print(f'Coord: {x_wert} / {y_wert}')
                #Absturz bei Klick in leeres Feld verhindern
                if (x_wert, y_wert) not in act_pos_dict.keys():
                    pass
                else:
                    # img rect zuweisen aus dict_actualPosition
                    img = act_pos_dict[(x_wert, y_wert)][0]
                    rect = img.get_rect()
                    rect.center = (full_image_x + x_wert*part_size + part_size//2), (full_image_y + y_wert*part_size + part_size//2)

                    if rect.collidepoint(event.pos):
                        moving = True

            elif event.type == pygame.MOUSEMOTION and moving == True:
                if fertig == False:
                    rect.move_ip(event.rel)
                    # Kachel in den Grenzen des Spielfelds halten
                    if rect.x < full_image_x:
                        rect.x = full_image_x
                    if rect.x > (full_image_x + (x_anz - 1) * part_size):
                        rect.x = (full_image_x + (x_anz - 1) * part_size)
                    if rect.y < full_image_y:
                        rect.y = full_image_y
                    if rect.y > (full_image_y + (y_anz - 1) * part_size):
                        rect.y = (full_image_y + (y_anz - 1) * part_size)

                screen.fill(GRAY)
                screen.blit(img, rect)

                for key, value in act_pos_dict.items():
                    if key == (x_wert, y_wert):
                        continue
                    else:
                        screen.blit(value[0], value[1])

                blit_grid(grid, (255, 0, 0))
                pygame.display.update()

            elif event.type == pygame.MOUSEBUTTONUP:
                moving = False

                #wo wurde das Teil abgelegt
                drop_x, drop_y = rect.center

                # finde x, y
                x_neu = int(drop_x - full_image_x) // part_size
                y_neu = int(drop_y - full_image_y) // part_size

                # Nicht auf besetzte Felder ablegen
                if (x_neu, y_neu) in act_pos_dict.keys():
                    pass
                # Nicht außerhalb des Spielfelds ablegen
                elif x_neu < 0 or x_neu >= x_anz:
                    pass
                elif y_neu < 0 or y_neu >= y_anz:
                    pass
                #Nur auf angrenzendes leeres Feld ablegen
                elif abs(x_neu - x_wert) > 1 and controlsWindow.shuffle.isChecked() == False:
                    pass
                elif abs(y_neu - y_wert) > 1 and controlsWindow.shuffle.isChecked() == False:
                    pass
                elif (abs(x_neu - x_wert) + abs(y_neu - y_wert)) > 1 and controlsWindow.shuffle.isChecked() == False:
                    pass

                else:
                    #Neue Position und Feldordnungswert im Dict eintragen
                    feldordnungswert = y_neu*x_anz + x_neu
                    act_pos_dict[(x_neu, y_neu)] = (act_pos_dict[(x_wert, y_wert)][0],(full_image_x + x_neu*part_size, full_image_y + y_neu*part_size), feldordnungswert, act_pos_dict[(x_wert, y_wert)][3])
                    #Leergezogene Position löschen
                    del act_pos_dict[(x_wert, y_wert)]

                    if controlsWindow.shuffle.isChecked() == True:
                        #check ob x_neu,y_neu korrekte Position ist
                        if act_pos_dict[x_neu, y_neu][3] == full_partsdict[x_neu, y_neu][3]:
                            success(1)
                            counter += 1
                        else:
                            counter -= 1
                    else:
                        counter += 1

                # #Ausgabe der neuen Bildversion
                # screen.fill(GRAY)
                # for key, value in act_pos_dict.items():
                #     screen.blit(value[0], value[1])



                #Check ob Spiel abgeschlossen
                i = 1
                for key, value in dict(sorted(act_pos_dict.items(), key=lambda x: x[1][2])).items():
                    #print(f'<index: {i} Wert: {value[3]}')
                    if value[3] == i:
                        #Check alle Werte in der richtigen Reihenfolge und Feld unten rechts leer
                        if i == (x_anz*y_anz - 1) and ((x_anz-1, y_anz-1) not in act_pos_dict.keys()):
                            if controlsWindow.shuffle.isChecked() == False:
                                text_surface = pygame.font.Font.render(font, f'{counter_name}: {counter} ', True,(55, 55, 55))
                            else:
                                text_surface = pygame.font.Font.render(font, f'Punkte: {counter} von {(x_anz * y_anz) - 1}',
                                                                       True, (55, 55, 55))
                            screen.blit(text_surface, dest=(50, 50))
                            pygame.display.flip()
                            success(6)
                            pygame.time.delay(1100)

                            if controlsWindow.dir_button.isChecked() == True or controlsWindow.pic_button.isChecked() == True:
                                replay = False
                                init = False
                            else:
                                replay = True
                                init = False
                            return(counter)
                        else:
                            i +=1
                    else:
                        break

                #Ausgabe der neuen Bildversion
                screen.fill(GRAY)
                for key, value in act_pos_dict.items():
                    screen.blit(value[0], value[1])

                if controlsWindow.shuffle.isChecked() == False:
                    text_surface = pygame.font.Font.render(font, f'{counter_name}: {counter} ', True, (55, 55, 55))
                else:
                    text_surface = pygame.font.Font.render(font, f'Punkte: {counter} von {(x_anz * y_anz)-1}', True, (55, 55, 55))

                screen.blit(text_surface, dest=(50, 50))

                if not controlsWindow.gt_mode:
                    screen.blit(text_surface_3, dest=(controlsWindow.screen_width / 3, controlsWindow.screen_height - 50))

                blit_grid(grid, (255, 0, 0))
                pygame.display.update()

        if moving == False:
            # Ausgabe der neuen Bildversion
            screen.fill(GRAY)
            for key, value in act_pos_dict.items():
                screen.blit(value[0], value[1])

            if controlsWindow.shuffle.isChecked() == False:
                text_surface = pygame.font.Font.render(font, f'{counter_name}: {counter} ', True, (55, 55, 55))
            else:
                text_surface = pygame.font.Font.render(font, f'Punkte: {counter} von {(x_anz * y_anz) - 1}', True,
                                                       (55, 55, 55))
            screen.blit(text_surface, dest=(50, 50))

            if not controlsWindow.gt_mode:
                screen.blit(text_surface_3,
                            dest=(controlsWindow.screen_width / 3, controlsWindow.screen_height - 50))

            blit_grid(grid, (255, 0, 0))
            pygame.display.update()

    return

# Hier wird nach dem "Parity-Verfahren" (siehe Wikipedia zu 15-Puzzle) die Lösbarkeit der Teile-Verteilung geprüft
def check_solvability(act_pos_dict, x_anz, y_anz):

    n2 = 0
    for key, value in dict(sorted(act_pos_dict.items(), key=lambda x: x[1][2])).items():
        # Wobei x[1] für Value steht (x[0] wäre der key) und der zweite Wert in der eckigen Klamer die Position in der Value-Liste bezeichnet
        # hier wird demgemäß nach Ordnungsposition sortiert
        # print(f'Ordnung: {value[2]}, Wert: {value[3]}')
        order = value[2]
        reference = value[3]
        count = 1
        #single_count = 0
        for key, value in dict(sorted(act_pos_dict.items(), key=lambda x: x[1][2])).items():
            if count >= order - 1:
                break
            if value[3] > reference:
                n2 += 1
                #single_count += 1
            count += 1

    #Ausgangspunkt Leerfeld in Zeile 1 auf 0/0 und Durcheinander = n2
    n1_start = 1
    parity_start = n1_start + n2
    #Ziel: Leerfeld im letzten Feld, n2 = 0
    n1_goal = y_anz
    parity_goal = n1_goal
    #print(f'N2: {n2}')
    #print(f'Parity-Ziel: {parity_goal}')
    #print(f'Parity-Start: {parity_start}')

    #if (x_anz == 3 and y_anz == 4):
    if ((parity_start % 2) == 0 and (parity_goal % 2) == 0) or ((parity_start % 2) != 0 and (parity_goal % 2) != 0):
        loesbar = True
        #Sonderlocke bei nicht-quadratischen Spielfeldern
        if (x_anz % 2) != 0 and (y_anz % 2) == 0:
            loesbar = False
    else:
        loesbar = False
        # Sonderlocke bei nicht-quadratischen Spielfeldern
        if (x_anz % 2) != 0 and (y_anz % 2) == 0:
            loesbar = True

    # if loesbar:
        #print("lösbar")
    # else:
        #print("unlösbar")

    return(loesbar)


#erzeugt ein Dictionary aller Teile mit x,y Koordinaten im Grid als Key und [surface, (part_pos_x, part_pos_y), Position in Reihenfolge im Grid, Wert] als Value
def make_full_partsdict(anz_x, anz_y,game):
    global full_image_x
    global full_image_y
    global part_size

    full_partsdict = {}

    order = 1
    value = 1
    for y in range(0, anz_y):
        for x in range(0,anz_x):
            #part = pic_parts(x,y)
            part_pos_x = full_image_x + x * part_size
            part_pos_y = full_image_y + y * part_size
            list_element = make_list_element(x,y, part_pos_x, part_pos_y, order, value, game)
            full_partsdict[(x,y)] = (list_element)
            order += 1
            value += 1

    return(full_partsdict)


def make_list_element(x,y, part_pos_x, part_pos_y, order, value, game):
    part = make_pic_part(x, y, game)
    list_element = [part, (part_pos_x, part_pos_y), order, value]
    return(list_element)


def make_pic_part(x, y, game):
    global w_floor
    global screen_height
    global part_size

    pic = pygame.image.load(r"tmp_resize.JPG")
    w, h = w_floor, screen_height
    screen = pygame.display.set_mode((w, h))
    screen.blit(pic, (0,0))

    rect = pygame.Rect(x * part_size, y * part_size, part_size, part_size)

    sub = screen.subsurface(rect)
    screenshot = pygame.Surface((part_size, part_size))
    screenshot.blit(sub, (0, 0))
    part = screenshot
    screen.fill(GRAY)

    return(part)


def make_grid(x_init, y_init, x_anz, y_anz, part_size):
    grid = {}

    for x_start in range(0, x_anz+1):
        grid[("h",(x_start, 0))] = [((x_init + (x_start * part_size)),y_init) , ((x_init + (x_start * part_size)), (y_init + (y_anz)*part_size))]

    for y_start in range(0, y_anz+1):
        grid[("v",(0, y_start))] = [(x_init, (y_init + (y_start * part_size))) , ((x_init + (x_anz)*part_size), (y_init + (y_start * part_size)) )]

    return(grid)

def blit_grid(grid, color):

    for key, value in grid.items():
        pygame.draw.line(screen, color, value[0], value[1], 3)
    #     print(f'{key}: {value[0]} / {value[1]}')

#Versteckt das Kontrollbild beim Bildwechsel und bringt das Spielfeld wieder nach vorn
def after_toggle():
    if controlsWindow.gt_start.isChecked() == False:
        controlsWindow.pic_control.hide()
    make_game_floor("have fun")


#Blinken und Klingeln bei Erfolg
def success(anz):
    global partslist

    for n in range(0, anz):
        for i in range(0, 25):
            blit_grid(grid, (255, 255, 255))
            pygame.display.flip()
        for j in range(0, 25):
            blit_grid(grid, (255, 0, 0))
            pygame.display.flip()

        pygame.mixer.Sound.play(kachelpasst)


    #sucht nach Zufall ein Bild aus dem Spielbildverzeichnis
select_pic_list = []
def find_pic():
    global select_pic_list

    if controlsWindow.dir_button.isChecked() == True:
        dir_text = controlsWindow.dir_path.toPlainText()
        if dir_text == "":
            select_pic_file = r"Grafiken\lieblingsordner.png"
        elif dir_text.startswith('"') and dir_text.endswith('"'):
            select_dir = dir_text[1:-1]
            if select_dir == "best of puzzles":
                select_dir = os.path.join(BASE_DIR,"best of puzzles")
        else:
            select_dir = dir_text
        if os.path.isdir(select_dir):
            full_pic_dict = {}
            file_count = 0
            for root, dirs, files in os.walk(select_dir):
                for file in files:
                    if ".png" in file or ".jpg" in file or ".jpeg" in file or ".PNG" in file or ".JPG" in file or ".JPEG" in file:
                        file_count += 1
                        path = os.path.join(root, file)
                        full_pic_dict[file_count] = path

            while True:
                select_pic = random.randint(1, file_count)
                if select_pic in select_pic_list:
                    pass
                else:
                    select_pic_list.append(select_pic)
                    select_pic_file = full_pic_dict[select_pic]
                    if len(select_pic_list) == file_count:
                        select_pic_list.clear()
                    break
        else:
            select_pic_file = r"Grafiken\lieblingsordner.png"

    elif controlsWindow.pic_button.isChecked() == True:
        pic_text = controlsWindow.pic_path.toPlainText()
        if pic_text != "":
            if pic_text.startswith('"') and pic_text.endswith('"'):
                select_pic = pic_text[1:-1]
            else:
                select_pic = pic_text
            if os.path.isfile(select_pic):
                select_pic_file = select_pic
            else:
                select_pic_file = r"Grafiken\lieblingsbild.png"
        else:
            select_pic_file = r"Grafiken\lieblingsbild.png"

    elif controlsWindow.nine_button.isChecked() == True:
        select_pic_file = r"Quadrate\Zahlen 9.jpg"

    elif controlsWindow.sixteen_button.isChecked() == True:
        select_pic_file = r"Quadrate\Zahlen 16.jpg"

    elif controlsWindow.abc_button.isChecked() == True:
        select_pic_file = r"Quadrate\ABC Puzzle.jpg"

    #print(select_pic_file)
    return(select_pic_file)

def show_fullparts(full_partsdict):
    for key, value in full_partsdict.items():
        #print(f'Publikations_Ordnung: {key} / {value[1]}, Wert: {value[3]}')
        screen.blit(value[0], value[1])
    pygame.display.flip()

def rpg_value():
    global started
    global planned_rounds
    global game

    if controlsWindow.gt_start.isChecked() == True:
    # if started:
        controlsWindow.rpg.setValue(planned_rounds)
        make_game_floor(gt_game_list[0])
    else:
        planned_rounds = controlsWindow.rpg.value()
        make_game_floor(gt_game_list[0])

    return(planned_rounds)

planned_rounds = rpg_value()

def start_gt():
    global gt_stop
    global abbruch
    global gt_game_list
    global planned_rounds
    global init
    global replay

    #if controlsWindow.gt_mode == False:
    if controlsWindow.gt_start.isChecked() == True:
        init = True
        replay = False
        abbruch = False
        gt_stop = False
        controlsWindow.gt_mode = True
        controlsWindow.gt_start.setText("Stop")
        controlsWindow.shuffle.setChecked(True)

        controlsWindow.puzzle_start.setEnabled(False)
        controlsWindow.slider_start.setEnabled(False)
        controlsWindow.pictris_start.setEnabled(False)


        start_game(gt_game_list[0][0])
    #elif controlsWindow.gt_mode == True:
    elif controlsWindow.gt_start.isChecked() == False:
        #wird gebraucht damit nach GT-Ende direkter Neustart funktioniert
        # if controlsWindow.gt_mode and ceil(game_rounds / planned_rounds) - 1 == len(gt_game_list):
        #     gt_stop = False
        #     abbruch = False
        #     controlsWindow.gt_mode = False
        #     controlsWindow.dir_button.setChecked(True)
        # else:
        #     gt_stop = True

        gt_stop = True
        abbruch = True
        #controlsWindow.gt_mode = False
        controlsWindow.dir_button.setChecked(True)

        controlsWindow.puzzle_start.setEnabled(True)
        controlsWindow.slider_start.setEnabled(True)
        controlsWindow.pictris_start.setEnabled(True)


        controlsWindow.gt_mode = False
        controlsWindow.timer_label.hide()
        controlsWindow.race_flag.show()
        controlsWindow.startWatch = False
        controlsWindow.timer_reset()
        controlsWindow.gt_start.setText("Start")
        #controlsWindow.gt_start.setToolTip("Für GT-Mode hier Klicken")
        game_counter_init()
        controlsWindow.pic_control.hide()
        controlsWindow.shuffle.setChecked(False)
        pygame.mixer.music.set_volume(0)
        uncheck("abbruch")
        screen.fill(GRAY)
        pygame.display.update()



def init_start(game):
    if controlsWindow.gt_start.isChecked() == True:
        if game == "puzzle":
            controlsWindow.puzzle_start.setChecked(False)
        elif game == "slider":
            controlsWindow.slider_start.setChecked(False)
        elif game == "pictris":
            controlsWindow.pictris_start.setChecked(False)
        make_game_floor(game)
        return
    else:
        start_game(game)


def start_game(game):
    global init
    global replay
    global gt_stop
    global game_rounds
    global planned_rounds
    global started
    global fertig
    global abbruch
    global game_list
    global part_anz_init
    global part_anz_min
    global full_partsdict
    global act_partsdict
    global result_percent
    global result_points

    uncheck(game)
    game_counter_init()

    started = False
    fertig = False
    init = True
    replay = False
    game_rounds = 0
    abbruch = False

    while True:
        if controlsWindow.gt_mode and ceil(game_rounds / planned_rounds) - 1 == len(gt_game_list):
            controlsWindow.startWatch = False

            result_points = gt_game_list[0][2] + gt_game_list[1][2] + gt_game_list[2][2]
            max_points = gt_game_list[0][3] + gt_game_list[1][3] + gt_game_list[2][3]
            controlsWindow.fullpoints.setText(str(result_points) + "  von " + str(max_points))

            result_percent = int((result_points / max_points) * 100)
            controlsWindow.gt_start.setText(str(result_percent) + " %")

            controlsWindow.rpg.setEnabled(True)
            uncheck("abbruch")
            part_anz_init = part_anz_min
            started = False
            fertig = False
            init = True
            replay = False
            game_rounds = 0
            controlsWindow.pic_control.hide()
            screen.fill(GRAY)
            pygame.display.update()
            break

        elif gt_stop or abbruch:
            gt_stop = False
            abbruch = False
            game_counter_init()
            part_anz_init = part_anz_min
            started = False
            fertig = False
            init = True
            replay = False
            game_rounds = 0
            uncheck("abbruch")
            controlsWindow.dir_button.setChecked(True)
            controlsWindow.rpg.setEnabled(True)
            controlsWindow.fullpoints.setText("")
            controlsWindow.pic_control.hide()
            screen.fill(GRAY)
            pygame.display.update()
            break

        else:
            start_playing(game)

def make_contender_line(i):
    global contenders

    hbox_contenders = QHBoxLayout()

    label_result_name = QtWidgets.QLabel()
    label_result_name.setMinimumSize(QSize(40, 20))
    label_result_name.setMaximumSize(QSize(40, 20))
    label_result_rounds = QtWidgets.QLabel()
    label_result_rounds.setMaximumSize(QSize(40, 20))
    label_result_rounds.setMinimumSize(QSize(40, 20))
    label_result_percent = QtWidgets.QLabel()
    label_result_percent.setMaximumSize(QSize(40, 20))
    label_result_percent.setMinimumSize(QSize(40, 20))
    label_result_points = QtWidgets.QLabel()
    label_result_points.setMaximumSize(QSize(40, 20))
    label_result_points.setMinimumSize(QSize(40, 20))
    label_result_time = QtWidgets.QLabel()
    label_result_time.setMaximumSize(QSize(60, 20))
    label_result_time.setMinimumSize(QSize(60, 20))
    label_result_pic = QtWidgets.QLabel()
    label_result_pic.setMaximumSize(QSize(180, 20))
    label_result_pic.setMinimumSize(QSize(180, 20))

    label_result_name.setText(contenders[i][0])
    label_result_rounds.setText(str(contenders[i][1]))
    label_result_percent.setText(str(contenders[i][2]))
    label_result_points.setText(str(contenders[i][3]))
    label_result_time.setText(str(contenders[i][4]))
    label_result_pic.setText(contenders[i][5])

    hbox_contenders.addWidget(label_result_name)
    hbox_contenders.addWidget(label_result_rounds)
    hbox_contenders.addWidget(label_result_percent)
    hbox_contenders.addWidget(label_result_points)
    hbox_contenders.addWidget(label_result_time)
    hbox_contenders.addWidget(label_result_pic)

    return(hbox_contenders)

def make_fame_window():
    global contenders

    #print(contenders)

    fameWindow.formLayout = QFormLayout()
    fameWindow.groupbox = QGroupBox("Strasse der Besten")

    hbox_labels = QHBoxLayout()

    label_name = QtWidgets.QLabel("Spieler")
    label_name.setMaximumSize(QSize(40, 20))
    label_rounds = QtWidgets.QLabel("Runden")
    label_rounds.setMaximumSize(QSize(40, 20))
    label_percent = QtWidgets.QLabel("Prozent")
    label_percent.setMaximumSize(QSize(40, 20))
    label_points = QtWidgets.QLabel("Punkte")
    label_points.setMaximumSize(QSize(40, 20))
    label_time = QtWidgets.QLabel("Zeit")
    label_time.setMaximumSize(QSize(60, 20))
    label_pic = QtWidgets.QLabel("Bild")
    label_pic.setMaximumSize(QSize(180, 20))

    hbox_labels.addWidget(label_name)
    hbox_labels.addWidget(label_rounds)
    hbox_labels.addWidget(label_percent)
    hbox_labels.addWidget(label_points)
    hbox_labels.addWidget(label_time)
    hbox_labels.addWidget(label_pic)

    fameWindow.formLayout.addRow(hbox_labels)

    for i in range(len(contenders)):
        hbox_line = make_contender_line(i)
        fameWindow.formLayout.addRow(hbox_line)
        print(f'contender {i}')

    fameWindow.groupbox.setLayout(fameWindow.formLayout)

    scroll = QScrollArea()
    scroll.setWidget(fameWindow.groupbox)
    scroll.setWidgetResizable(True)
    scroll.setFixedHeight(fameWindow.width)
    scroll.setFixedWidth(fameWindow.height)

    fameWindow.layout = QVBoxLayout()
    fameWindow.layout.addWidget(scroll)
    fameWindow.layoutexists = True

    fameWindow.setLayout(fameWindow.layout)


def clear_fame():

    for label in fameWindow.groupbox.findChildren(QtWidgets.QLabel):
        label.deleteLater()
    fameWindow.layout.deleteLater()
    # fameWindow.layoutexists = False
    fameWindow.close()
    fameWindow.destroy()

contenders = []
contenders.append(["ds", 1, 77, 12,"01:33:09", "best of puzzles\IMG_4556.jpeg"])
def save_fame():
    global contenders
    global result_percent
    global spielbild
    global gt_game_list
    global result_points
    global fame_show

    try:
        gt_result = []
        name = controlsWindow.player.currentText()
        gt_result.append(name)
        rounds = gt_game_list[2][1]
        gt_result.append(rounds)
        gt_result.append(result_percent)
        points = result_points
        gt_result.append(points)
        doc = QtGui.QTextDocument()
        doc.setHtml(controlsWindow.timer_label.text())
        time = doc.toPlainText()
        print(time)
        gt_result.append(time)
        gt_result.append(spielbild)

        contenders.append(gt_result)

    except:
        pass

    try:
        clear_fame()
        fame_show = False
        print("geschlossen")
    except:
        pass

    make_game_floor()


fame_show = False
def show_h_o_f():
    global fame_show

    if fame_show == False:
        make_fame_window()
        fameWindow.show()
        fame_show = True
    elif fame_show == True:
        clear_fame()
        fame_show = False


if __name__ == '__main__':
    controlsWindow.show()
    controlsWindow.puzzle_start.released.connect(lambda: init_start("puzzle"))
    controlsWindow.slider_start.released.connect(lambda: init_start("slider"))
    controlsWindow.pictris_start.released.connect(lambda: init_start("pictris"))
    controlsWindow.nine_button.toggled.connect(after_toggle)
    controlsWindow.sixteen_button.toggled.connect(after_toggle)
    controlsWindow.abc_button.toggled.connect(after_toggle)
    controlsWindow.dir_button.toggled.connect(after_toggle)
    controlsWindow.pic_button.toggled.connect(after_toggle)
    controlsWindow.ambient.toggled.connect(make_game_floor)
    controlsWindow.game_sounds.toggled.connect(make_game_floor)
    controlsWindow.shuffle.toggled.connect(make_game_floor)
    controlsWindow.blind.toggled.connect(make_game_floor)
    controlsWindow.rpg.valueChanged.connect(rpg_value)
    controlsWindow.gt_start.clicked.connect(start_gt)
    controlsWindow.end_all.clicked.connect(lambda: sys.exit(0))
    controlsWindow.game_back2front.clicked.connect(make_game_floor)
    controlsWindow.fame_save.clicked.connect(save_fame)
    controlsWindow.call_h_o_f.clicked.connect(show_h_o_f)


#pygame.quit()
sys.exit(app.exec())
pygame.quit()

