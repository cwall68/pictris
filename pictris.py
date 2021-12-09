import pygame
import sys
import os
import pyautogui
from PIL import Image
import random
import math


from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QMouseEvent
from PyQt5.QtWidgets import *

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

        self.label_width = 85
        self.label_height = self.label_width
        self.label_start_x = 75
        self.label_start_y = 75
        self.label_space = int(1.5*self.label_width)
        self.button_height = 15
        self.text_height = 40


        self.pic_choice_label = QtWidgets.QLabel(self)
        self.pic_choice_label.setText("Bildauswahl:")
        self.pic_choice_label.setGeometry(self.label_start_x, self.label_start_y - self.label_height , 2*self.label_space + self.label_width, self.label_height)
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
        self.nine_button.setGeometry(self.label_start_x, self.label_start_y + self.label_height + self.button_height, self.label_width, self.button_height)

        self.sixteen_label = QtWidgets.QLabel(self)
        self.sixteen_label_pic_path = os.path.join(graf_dir, "Zahlen 16.jpg")
        self.sixteen_label_pic = QtGui.QPixmap(self.sixteen_label_pic_path)
        self.sixteen_label_pic.scaled(self.label_width, self.label_height)
        self.sixteen_label_pic = QtGui.QPixmap(self.label_width, self.label_height)
        self.sixteen_label.setPixmap(self.sixteen_label_pic)
        self.sixteen_label.setGeometry(self.label_start_x + self.label_space, self.label_start_y, self.label_width,
                                       self.label_height)

        self.sixteen_button = QRadioButton("16er Quadrat", self)
        self.sixteen_button.setGeometry(self.label_start_x + self.label_space, self.label_start_y + self.label_height + self.button_height, self.label_width, self.button_height)

        self.abc_label = QtWidgets.QLabel(self)
        self.abc_label_pic_path = os.path.join(graf_dir, "ABC Puzzle.jpg")
        self.abc_label_pic = QtGui.QPixmap(self.abc_label_pic_path)
        self.abc_label_pic.scaled(self.label_width, self.label_height)
        self.abc_label_pic = QtGui.QPixmap(self.label_width, self.label_height)
        self.abc_label.setPixmap(self.abc_label_pic)
        self.abc_label.setGeometry(self.label_start_x + 2*self.label_space, self.label_start_y, self.label_width,
                                    self.label_height)

        self.abc_button = QRadioButton("ABC Quadrat", self)
        self.abc_button.setGeometry(self.label_start_x + 2*self.label_space, self.label_start_y + self.label_height + self.button_height, self.label_width, self.button_height)

        self.dir_label = QtWidgets.QLabel(self)
        self.dir_label_pic_path = os.path.join(graf_dir,"lieblingsordner.png" )
        self.dir_label_pic = QtGui.QPixmap(self.dir_label_pic_path)
        self.dir_label_pic.scaled(self.label_width, self.label_height)
        self.dir_label_pic = QtGui.QPixmap(self.label_width, self.label_height)
        self.dir_label.setPixmap(self.dir_label_pic)
        self.dir_label.setGeometry(self.label_start_x, int(self.label_start_y + 1.2*self.label_space), self.label_width, self.label_height)

        self.dir_path = QTextEdit(self)
        self.dir_path.setGeometry(self.label_start_x + self.label_space, int(self.label_start_y + 0.5*self.label_height + 1.2 * self.label_space - 0.5*self.text_height),
                                   self.label_width + self.label_space, self.text_height)
        self.dir_path.setText(f'best of puzzles')

        self.dir_button = QRadioButton("Zufallsbild aus Lieblingsordner", self)
        self.dir_button.setGeometry(self.label_start_x, self.label_start_y + int(1.15*self.label_space) + self.label_height + self.button_height, 2*self.label_width, self.button_height)
        self.dir_button.setChecked(True)

        self.pic_label = QtWidgets.QLabel(self)
        self.pic_label_pic_path = os.path.join(graf_dir,"lieblingsbild.png" )
        self.pic_label_pic = QtGui.QPixmap(self.pic_label_pic_path)
        self.pic_label_pic.scaled(self.label_width, self.label_height)
        self.pic_label_pic = QtGui.QPixmap(self.label_width, self.label_height)
        self.pic_label.setPixmap(self.pic_label_pic)
        self.pic_label.setGeometry(self.label_start_x, int(self.label_start_y + 2.4*self.label_space), self.label_width, self.label_height)


        self.pic_path = QTextEdit(self)
        self.pic_path.setGeometry(self.label_start_x + self.label_space, int(self.label_start_y + 2.5*self.label_height + 1.1*self.label_space - 0.5*self.text_height),
                                   self.label_width + self.label_space, self.text_height)

        self.pic_button = QRadioButton("Bild der Wahl", self)
        self.pic_button.setGeometry(self.label_start_x, int(self.label_start_y + 2.4*self.label_space)+ self.label_height + self.button_height, 2*self.label_height, self.button_height)

        self.start_button_height = 40
        self.start_button_space = 2 * self.start_button_height
        self.start_button_y = int(0.5 * self.screen_height)+ 110
        self.start_button_width = 2*self.label_space + self.label_width

        self.start_label = QtWidgets.QLabel(self)
        self.start_label.setText("Spielauswahl:")
        self.start_label.setGeometry(self.label_start_x, self.start_button_y - int(0.8*self.start_button_space), self.start_button_width, self.start_button_height)
        self.start_label.setStyleSheet("font-size: 18px;")

        self.puzzle_start = QPushButton("Puzzle", self)
        self.puzzle_start.setGeometry(self.label_start_x, self.start_button_y, self.start_button_width, self.start_button_height)
        self.puzzle_start.setCheckable(True)
        self.puzzle_start.setStyleSheet(
            ":checked{background: solid lightgreen}"
            ":checked{border: 4px solid red}"
            ":!checked{background-color: rgb(255,255,255)}"
            ":!checked{border: 4px solid lightgreen}"
            ":!checked{font-size: 13px}"
        )

        self.slider_start = QPushButton("Slider", self)
        self.slider_start.setGeometry(self.label_start_x, self.start_button_y + self.start_button_space, self.start_button_width, self.start_button_height)
        self.slider_start.setCheckable(True)
        self.slider_start.setStyleSheet(
            ":checked{background: solid lightblue}"
            ":checked{border: 4px solid red}"
            ":!checked{background-color: rgb(255,255,255)}"
            ":!checked{border: 4px solid lightblue}"
            ":!checked{font-size: 13px}"
        )

        self.pictris_start = QPushButton("Pictris", self)
        self.pictris_start.setGeometry(self.label_start_x, self.start_button_y + 2*self.start_button_space, self.start_button_width, self.start_button_height)
        self.pictris_start.setCheckable(True)
        self.pictris_start.setStyleSheet(
            ":checked{background: solid yellow}"
            ":checked{border: 4px solid red}"
            ":!checked{background-color: rgb(255,255,255)}"
            ":!checked{border: 4px solid yellow}"
            ":!checked{font-size: 13px}"
        )

        #Kontrollbild hinter Spielfeld
        self.pic_control = QtWidgets.QLabel(self)


#Anlegen des Fensters mit den Auswhl- und Kontrollfeldern für das Spiel
controlsWindow = Controls()
screen_width = controlsWindow.screen_width
screen_height = controlsWindow.screen_height
controlsWindow.setGeometry(0, 0, screen_width, screen_height)

pygame.init()
FPS = 60
clock = pygame.time.Clock()

GRAY = (150, 150, 150)
RED = (255, 0, 0)

#Mindestzahl an Teilen auf der längeren Bildkante
part_anz_init = 4
#Zähler für die Verkleinerung der Puzzleteile bei Bildpuzzle
game_rounds = 0
#Bildabstand vom unteren Rand
offset_y = 50
#Fading-Ausgangswert
alphawert_init = 255
#Steuerung der Geschwindigkeit des Hintergrundbildverschwindens bei Puzzle und Pictris
fade_factor = 0.2
#Kachel wartet bei Pictris vor dem Fall
before_fall_init = 750

#w und h sind die Werte für Breite und Höhe des Spielfelds (game floor)
#x und y lokalisieren den game floor auf dem Gesamtbildschirm
#w_floor, h_floor = screen_width - screen_width // 4, screen_height - 30
w_floor, h_floor = screen_width - screen_width // 4, screen_height
game_x = screen_width - w_floor
game_y = screen_height - h_floor - offset_y

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# pic_dir = os.path.join(BASE_DIR,"best of puzzles")
# graf_dir = os.path.join(BASE_DIR,"Grafiken")


def make_game_floor(game):
    global w_floor
    global h_floor
    global game_x
    global game_y
    global screen

    #os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (game_x, game_y)
    #os.environ['SDL_WINDOW_ALWAYS_ON_TOP'] = '%s' % ('SDL_VIDEO_WINDOW')

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
    pygame.display.flip()


def start(game):
    global spielbild
    global fade_factor
    global part_size
    global part_anz
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

    started = False

    #if game == "puzzle" or game == "slider" or game == "pictris":
    if controlsWindow.dir_button.isChecked() == True or controlsWindow.pic_button.isChecked() == True:
        if init == True and replay == False:
            spielbild = find_pic()
            controlsWindow.pic_path.setText(spielbild)
            part_anz = part_anz_init
            game_rounds = 0
        else:
            game_rounds += 1
            part_anz = part_anz + game_rounds

    # elif game == "puzzle 15":
    #     spielbild = r"C:\Users\User\Desktop\pictris\Zahlen gerade.jpg"
    #     part_anz = 4
    #     fade_factor = 0.1
    #     game = "puzzle"
    # elif game == "puzzle ABC":
    #     spielbild = r"C:\Users\User\Desktop\pictris\ABC Puzzle.jpg"
    #     part_anz = 5
    #     fade_factor = 0.1
    #     game = "puzzle"
    elif controlsWindow.nine_button.isChecked() == True:
        spielbild = find_pic()
        part_anz = 3
        #game = "slider"
    elif controlsWindow.sixteen_button.isChecked() == True:
        spielbild = find_pic()
        part_anz = 4
        #game = "slider"
    elif controlsWindow.abc_button.isChecked() == True:
        spielbild = find_pic()
        part_anz = 5
        #game = "slider"

    #Hier wird das oben bestimmte Spielbild in das Spieformat gebracht und in diesem Format als tmp Pic abgelegt
    image = resize(spielbild)
    width, height = image.size
    part_size, part_anz = find_part_size(width, height, part_anz)

    #Bestimmung der Position des Gesamtspielbildes
    full_image_x = (w_floor - width) / 2
    full_image_y = h_floor - height - offset_y

    #Berechnung der horizontalen und vertikalen Teilezahl
    x_anz = width // part_size
    y_anz = height // part_size

    pic = pygame.image.load(r"C:\Users\User\Desktop\tmp_resize.JPG")

    make_game_floor(game)

    control_pic = QtGui.QPixmap(r"C:\Users\User\Desktop\tmp_resize.JPG")
    controlsWindow.pic_control.setGeometry(screen_width - width - offset_y, screen_height - height - offset_y, width, height)
    controlsWindow.pic_control.setPixmap(control_pic)
    controlsWindow.pic_control.show()

    grid = make_grid(full_image_x, full_image_y, x_anz, y_anz, part_size)
    full_partsdict = make_full_partsdict(x_anz, y_anz, game)

    #Hier wird das Spielbild in Position gesenkt
    pic_pos_x = full_image_x
    move = True
    while move == True:
        for pic_pos_y in range (0,full_image_y):
            screen.fill(GRAY)
            screen.blit(pic, (pic_pos_x, pic_pos_y))
            pygame.display.update()
        move = False

    if game_rounds > 0 and game == "puzzle":
        puzzle(full_partsdict, grid)
        return

    if game == "pictris":
        pictris(full_partsdict, grid)
        return

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
            elif event.type == pygame.MOUSEBUTTONUP:
                if game == "puzzle":
                    puzzle(full_partsdict, grid)
                    return
                elif game == "slider":
                    slider(full_partsdict, grid)
                    return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    return


def find_part_size(width, height, part_anz):

    if width > height:
        part_size = width // part_anz
        while height // part_size < 3:
            part_anz += 1
            part_size = width // part_anz
    else:
        part_size = height // part_anz
        while width // part_size < 3:
            part_anz += 1
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


def resize(file):

    fixed_height = 650
    image = Image.open(file)
    height_percent = (fixed_height / float(image.size[1]))
    width_size = int((float(image.size[0]) * float(height_percent)))
    image = image.resize((width_size, fixed_height), Image.NEAREST)
    image.save(r"C:\Users\User\Desktop\tmp_resize.JPG")

    return(image)

zugzahl = 0
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

    act_partsdict = {}

    parts_list = []

    fertig = False

    if init == True:
        counter = 0

    #alpha_step = alphawert_init // (x_anz*y_anz)
    alphawert = alphawert_init

    moving = False

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

    running = True
    #fade = 0.77
    while running:
        screen.fill(GRAY)

        #Ausgabe langsam verblassender Hintergrund
        for key, value in full_partsdict.items():
            if zugzahl == 0:
                value[0].set_alpha(255)
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
                    game_rounds = 0
                    counter = 0
                    init = True
                    replay = False
                    return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    moving = True
                    #print("Buttondown angenommen")


            elif event.type == pygame.MOUSEMOTION and moving == True:
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
                print(f'{x_neu} / {y_neu}')
                if (x_neu < 0 or x_neu > x_anz-1) or (y_neu < 0 or y_neu > y_anz-1):
                    pass
                else:
                    if act_partsdict[x,y][3] == full_partsdict[x_neu, y_neu][3]:
                        coord_neu = x_neu, y_neu
                        parts_list.append(coord_neu)

                        counter += 1

                        for i in range(0,30):
                            blit_grid(grid, (255,255,255))
                            pygame.display.flip()

                        if len(parts_list) == (y_anz * x_anz):
                            fertig = True
                            init = False
                            text_surface = pygame.font.Font.render(font, f'Punkte: {counter}', True, (55, 55, 55))
                            screen.blit(text_surface, dest=(50, 50))
                            for key, value in act_partsdict.items():
                                screen.blit(value[0], value[1])
                            pygame.display.flip()
                            success(6)
                            return
                    else:
                        counter -= 1

                    if fertig == False:
                        x = random. randint(0,x_anz-1)
                        y = random. randint(0,y_anz-1)

                        while (x,y) in parts_list:
                            x = random.randint(0, x_anz-1)
                            y = random.randint(0, y_anz-1)

                        img = act_partsdict[x, y][0]

                        rect = img.get_rect()
                        rect.center = w_floor // 2, full_image_y // 2
                    moving = False

                    # Ausblenden des Hintergrunds (erst schneller, dann langsam
                    #abzug = game_rounds*alpha_step + (alpha_step)**(fade_factor/zugzahl)
                    anz = x_anz*y_anz
                    abzug = (alphawert_init / ((anz - (anz*fade_factor))**0.5) * (zugzahl**0.5))
                    alphawert = alphawert_init - abzug
                    if alphawert <= 8:
                        alphawert = 8
                    print(f'Abzug: {abzug} Alphawert: {alphawert}')

        screen.blit(img, rect)

        text_surface = pygame.font.Font.render(font, f'Punkte: {counter}', True, (55, 55, 55))
        screen.blit(text_surface, dest=(50, 50))

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

    fertig = False
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
                        replay = True
                        game_rounds = -1
                        stop = True
                        fertig = True

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
                                act_partsdict = act_partsdict_old.copy()
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

            punkte = fits - fails

            blit_field(full_partsdict, act_partsdict, alphawert)

            img.set_alpha(255)
            screen.blit(img, (pic_pos_x, pic_pos_y))
            blit_grid(grid, RED)

            text_surface = pygame.font.Font.render(font, f'Punkte: {punkte} von {x_anz * y_anz} aus {parts}', True, (55, 55, 55))
            screen.blit(text_surface, dest=(50, 50))

            pygame.display.update()

            if fertig:
                success(8)
                punkte = 0
                act_partsdict.clear()
                pygame.time.delay(1000)
                stop = True

            if stop:
                break

        move = False

    return(act_partsdict, fertig)

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
                #success(6)
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
    #Wartezeit
    global before_fall_init

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

    screen.fill(GRAY)

    x, y = make_randpos(act_partsdict)
    img = full_partsdict[x, y][0]

    img.set_alpha(255)
    start_pos_x = (full_image_x + int(x_anz * part_size / 2 - part_size / 2))
    start_pos_Y = (full_image_y // 2) - int(part_size / 2)
    screen.blit(img, (start_pos_x, start_pos_Y))

    running = True

    # #Init für korrekt eingepasste Teile
    # fits = 0
    # fails = 0

    while running:
        if not started:
            alphawert = alphawert_init
            blit_field(full_partsdict, act_partsdict, alphawert)
        else:
            alphawert = 55

        # blit_field(full_partsdict, act_partsdict, alphawert)

        if started:
            before_fall = before_fall_init - int(fits*(before_fall_init-550)/(x_anz*y_anz))
            blit_field(full_partsdict, act_partsdict, alphawert)
            img.set_alpha(255)
            start_pos_x = (full_image_x + int(x_anz * part_size / 2 - part_size / 2))
            start_pos_Y = (full_image_y // 2) - int(part_size / 2)
            screen.blit(img, (start_pos_x, start_pos_Y))
            blit_grid(grid, RED)
            pygame.display.update()
            #Kachel wird für spezifizierte Zeit vor Fall gezeigt
            pygame.time.delay(before_fall)

            #Kachelfalldurchlauf
            act_partsdict, fertig= part_fall(img, full_partsdict, x, y, act_partsdict, alphawert)
            if fertig:
                replay = True
                init = False
                started = False
                return

            blit_field(full_partsdict, act_partsdict, alphawert)
            #Neue Kachel erzeugen wenn nicht fertig
            x, y = make_randpos(act_partsdict)
            img = full_partsdict[x, y][0]

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

                if event.key == pygame.K_SPACE:
                    game_rounds = 0
                    counter = 0
                    init = True
                    replay = False
                    started = False
                    return

                if event.key == pygame.K_RETURN:
                    counter = 0
                    punkte = 0
                    alphawert = 55
                    parts = 0
                    fits = 0
                    fails = 0
                    started = True

                    act_partsdict, fertig= part_fall(img, full_partsdict, x, y, act_partsdict, alphawert)

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

replay = False
#Dictionary bewahrt die Zufallskonfiguration des Spielfelds um dieses in gleicher Form wieder spielen zu können
replay_dict = {}

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

    sender = controlsWindow.sender()
    spiel = sender.text()
    print(f'Spiel: {spiel}')

    font = pygame.font.Font(pygame.font.get_default_font(), 36)

    moving = False
    fertig = False
    #Zugzahl
    counter = 0

    # Dictonary hat als Key die x,y Werte aus full_partsdict und als Value das Image und dessen aktuelle Koordinaten auf dem Spielfeld
    act_pos_dict = {}

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
        print(f'Replay {replay}')


    screen.fill(GRAY)
    for key, value in act_pos_dict.items():
        screen.blit(value[0], value[1])
    blit_grid(grid, (255,0,0))
    text_surface = pygame.font.Font.render(font, f'Züge: {counter}', True, (55, 55, 55))
    screen.blit(text_surface, dest=(50, 50))
    pygame.display.flip()


    while running:

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    game_rounds = 0
                    counter = 0
                    init = True
                    replay = False
                    return

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
                elif abs(x_neu - x_wert) > 1 and not ((spiel == "Slider ABC") or (spiel == "Slider Pix")):
                    pass
                elif abs(y_neu - y_wert) > 1 and not ((spiel == "Slider ABC") or (spiel == "Slider Pix")):
                    pass
                elif (abs(x_neu - x_wert) + abs(y_neu - y_wert)) > 1 and not ((spiel == "Slider ABC") or (spiel == "Slider Pix")):
                    pass

                else:
                    #Neue Position und Feldordnungswert im Dict eintragen
                    feldordnungswert = y_neu*x_anz + x_neu
                    act_pos_dict[(x_neu, y_neu)] = (act_pos_dict[(x_wert, y_wert)][0],(full_image_x + x_neu*part_size, full_image_y + y_neu*part_size), feldordnungswert, act_pos_dict[(x_wert, y_wert)][3])
                    #Leergezogene Position löschen
                    del act_pos_dict[(x_wert, y_wert)]
                    counter += 1

                #Ausgabe der neuen Bildversion
                screen.fill(GRAY)
                for key, value in act_pos_dict.items():
                    screen.blit(value[0], value[1])

                #Check ob Spiel abgeschlossen
                i = 1
                for key, value in dict(sorted(act_pos_dict.items(), key=lambda x: x[1][2])).items():
                    print(f'<index: {i} Wert: {value[3]}')
                    if value[3] == i:
                        #Check alle Werte in der richtigen Reihenfolge und Feld unten rechts leer
                        if i == (x_anz*y_anz - 1) and ((x_anz-1, y_anz-1) not in act_pos_dict.keys()):
                            text_surface = pygame.font.Font.render(font, f'Züge: {counter}', True, (55, 55, 55))
                            screen.blit(text_surface, dest=(50, 50))
                            pygame.display.flip()
                            success(6)
                            replay = True
                            return
                        else:
                            i +=1
                    else:
                        break

                text_surface = pygame.font.Font.render(font, f'Züge: {counter}', True, (55, 55, 55))
                screen.blit(text_surface, dest=(50, 50))

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
    print(f'N2: {n2}')
    print(f'Parity-Ziel: {parity_goal}')
    print(f'Parity-Start: {parity_start}')

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

    if loesbar:
        print("lösbar")
    else:
        print("unlösbar")

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

    pic = pygame.image.load(r"C:\Users\User\Desktop\tmp_resize.JPG")
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


def success(anz):
    global partslist

    for n in range(0, anz):
        for i in range(0, 25):
            blit_grid(grid, (255, 255, 255))
            pygame.display.flip()
        for j in range(0, 25):
            blit_grid(grid, (255, 0, 0))
            pygame.display.flip()


    #sucht nach Zufall ein Bild aus dem Spielbildverzeichnis
def find_pic():

    if controlsWindow.dir_button.isChecked() == True:
        dir_text = controlsWindow.dir_path.toPlainText()
        if dir_text.startswith('"') and dir_text.endswith('"'):
            select_dir = dir_text[1:-1]
            if select_dir == "best of puzzles":
                select_dir = os.path.join(BASE_DIR,"best of puzzles")
        else:
            if dir_text == "":
                select_pic_file = r"C:\Users\User\PycharmProjects\pictris\Grafiken\lieblingsordner.png"
            else:
                select_dir = dir_text

        if dir_text != "":
            full_pic_dict = {}
            file_count = 0
            for root, dirs, files in os.walk(select_dir):
                for file in files:
                    if ".png" in file or ".jpg" in file or ".jpeg" in file or ".PNG" in file or ".JPG" in file or ".JPEG" in file:
                        file_count += 1
                        path = os.path.join(root, file)
                        full_pic_dict[file_count] = path

            select_pic = random.randint(1, file_count)
            select_pic_file = full_pic_dict[select_pic]

    elif controlsWindow.pic_button.isChecked() == True:
        pic_text = controlsWindow.pic_path.toPlainText()
        if pic_text != "":
            if pic_text.startswith('"') and pic_text.endswith('"'):
                select_pic_file = pic_text[1:-1]
            else:
                select_pic_file = pic_text
        else:
            select_pic_file = r"C:\Users\User\PycharmProjects\pictris\Grafiken\lieblingsbild.png"

    elif controlsWindow.nine_button.isChecked() == True:
        select_pic_file = r"C:\Users\User\PycharmProjects\pictris\Quadrate\Zahlen 9.jpg"

    elif controlsWindow.sixteen_button.isChecked() == True:
        select_pic_file = r"C:\Users\User\PycharmProjects\pictris\Quadrate\Zahlen 16.jpg"

    elif controlsWindow.abc_button.isChecked() == True:
        select_pic_file = r"C:\Users\User\PycharmProjects\pictris\Quadrate\ABC Puzzle.jpg"

    return(select_pic_file)

def show_fullparts(full_partsdict):
    for key, value in full_partsdict.items():
        #print(f'Publikations_Ordnung: {key} / {value[1]}, Wert: {value[3]}')
        screen.blit(value[0], value[1])
    pygame.display.flip()

def start_game(game):
    global init
    global replay

    uncheck(game)

    init = True
    replay = False
    while True:
        start(game)


if __name__ == '__main__':
    controlsWindow.show()
    controlsWindow.dir_label.show()
    controlsWindow.puzzle_start.clicked.connect(lambda: start_game("puzzle"))
    controlsWindow.slider_start.released.connect(lambda: start_game("slider"))
    controlsWindow.pictris_start.released.connect(lambda: start_game("pictris"))
    controlsWindow.nine_button.toggled.connect(controlsWindow.pic_control.hide)
    controlsWindow.sixteen_button.toggled.connect(controlsWindow.pic_control.hide)
    controlsWindow.abc_button.toggled.connect(controlsWindow.pic_control.hide)
    controlsWindow.dir_button.toggled.connect(controlsWindow.pic_control.hide)
    controlsWindow.pic_button.toggled.connect(controlsWindow.pic_control.hide)


#pygame.quit()
sys.exit(app.exec())
pygame.quit()

