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

app = QtWidgets.QApplication(sys.argv)


class Controls(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.statusBar()
        self.breite = 1850
        self.hoehe = 1000
        # self.setGeometry(30, 50, self.breite, self.hoehe)
        self.setWindowTitle('Pictris Controls')

        self.puzzle_start = QPushButton("Puzzle", self)
        self.puzzle_start.setGeometry(170, 330, 130, 20)
        self.puzzle_start.setCheckable(True)
        self.puzzle_start.setStyleSheet(
            ":checked{background: solid red}"
            ":checked{border: 2px solid lightblue}"
            ":!checked{background-color: rgb(255,255,255)}"
            ":!checked{border: 2px solid red}"
            ":!checked{font-size: 10px}"
        )

        self.slider_start = QPushButton("Slider", self)
        self.slider_start.setGeometry(170, 430, 130, 20)
        self.slider_start.setCheckable(True)
        self.slider_start.setStyleSheet(
            ":checked{background: solid lightblue}"
            ":checked{border: 2px solid red}"
            ":!checked{background-color: rgb(255,255,255)}"
            ":!checked{border: 2px solid lightblue}"
            ":!checked{font-size: 10px}"
        )

        self.point_counter = QtWidgets.QLabel(self)
        self.point_counter.setGeometry(QtCore.QRect(170, 40, 47, 13))

screen_width, screen_height= pyautogui.size()
print(f'Width: {screen_width} / Height: {screen_height}')
controlsWindow = Controls()
controlsWindow.setGeometry(0, 0, screen_width, screen_height)

#pygame.init()

FPS = 60
GRAY = (150, 150, 150)

#clock = pygame.time.Clock()

#w und h sind die Werte für Breite und Höhe des Spielfelds
#x und y lokalisieren den game floor auf dem Gesamtbildschirm

w_floor, h_floor = screen_width - screen_width // 4, screen_height - 30
game_x = screen_width - w_floor
game_y = screen_height - h_floor




#backdrop = pygame.image.load(r"C:\Users\User\PycharmProjects\pictris\Grafiken\pictris_backdrop.png")

part_size = 200
alphawert = 255
tolerance = 25
part_anz_init = 3
game_rounds = 0
offset_y = 50
fade_factor = 1.2


game_dir = r"D:\Pictures\Bilderserien\Jahre\2020"

def start(game):
    global spielbild
    global alphawert
    global part_size
    global part_anz
    global game_rounds
    global init
    global grid
    global offset_y
    global GRAY
    global w_floor
    global h_floor
    global screen
    global screen_width
    global screen_heigh
    global full_image_x
    global full_image_y
    global font
    global x_anz
    global y_anz

    RED = (255, 0, 0)
    GRAY = (150, 150, 150)

    make_game_floor(game)

    if init == True:
        spielbild = find_pic()
        part_anz = part_anz_init

    game_rounds += 1
    part_anz = part_anz + game_rounds

    image = resize(spielbild)
    width, height = image.size
    pic = pygame.image.load(r"C:\Users\User\Desktop\tmp_resize.JPG")

    if width > height:
        part_size = width // part_anz
        while height // part_size < 2:
            part_anz += 1
            part_size = width // part_anz
    else:
        part_size = height // part_anz
        while width // part_size < 2:
            part_anz += 1
            part_size = height // part_anz

    full_image_x = (w_floor - width) / 2
    full_image_y = h_floor - height - offset_y
    pic_pos_x = full_image_x

    x_anz = width // part_size
    y_anz = height // part_size

    grid = make_grid(full_image_x, full_image_y, x_anz, y_anz, part_size)

    move = True

    while move == True:
        for pic_pos_y in range (0,full_image_y):
            #screen.blit(backdrop,(0,0))
            screen.fill(GRAY)
            screen.blit(pic, (pic_pos_x, pic_pos_y))
            pygame.display.update()
            # for event in pygame.event.get():
            #     if event.type == pygame.KEYDOWN:
            #         if event.key == pygame.K_LEFT:
            #             pic_pos_x -= 50
            #         if event.key == pygame.K_RIGHT:
            #             pic_pos_x += 50
        move = False
    # while True:
    #     blit_grid(grid, RED)
    #     pygame.display.update()

    if game == "puzzle":
        puzzle()
    elif game == "slider":
        slider()
    return


def resize(file):

    fixed_height = 650
    image = Image.open(file)
    height_percent = (fixed_height / float(image.size[1]))
    width_size = int((float(image.size[0]) * float(height_percent)))
    image = image.resize((width_size, fixed_height), Image.NEAREST)
    image.save(r"C:\Users\User\Desktop\tmp_resize.JPG")

    return(image)

def make_game_floor(game):
    global w_floor
    global h_floor
    global screen
    global screen_width
    global screen_heigh

    game_x = screen_width - w_floor
    game_y = screen_height - h_floor

    os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (game_x, game_y)
    os.environ['SDL_WINDOW_ALWAYS_ON_TOP'] = '%s' % ('SDL_VIDEO_WINDOW')

    screen = pygame.display.set_mode(size=(w_floor, h_floor))
    pygame.display.set_caption(game)

def puzzle():
    global spielbild
    global alphawert
    global game_rounds
    global fade
    global w_floor
    global h_floor
    global init
    global fade_factor
    global partslist
    global GRAY
    global counter
    global fertig
    global font

    partslist = []
    fertig = False

    if init == True:
        counter = 0
        alphawert = 255

    RED = (255, 0, 0)
    #GRAY = (150, 150, 150)

    alphawert = 255
    #pygame.init()

    running = True
    fertig = False

    image = resize(spielbild)
    width, height = image.size

    full_image_x = (w_floor - width) / 2
    full_image_y = h_floor - height - offset_y
    pic_pos_x = full_image_x
    pic_pos_y = full_image_y

    anz_w = width // part_size
    anz_h = height // part_size
    fade = int((alphawert // (anz_h * anz_w))**fade_factor)
    print(f'Breite: {anz_w} Pieces, Höhe: {anz_h} Pieces')
    full_img = pygame.image.load(r"C:\Users\User\Desktop\tmp_resize.JPG")
    full_img.convert()
    #full_image = pygame.Surface((int(width), int(height)))
    full_img.set_alpha(alphawert)

    x = part_size * random.randint(0, anz_w-1)
    y = part_size * random.randint(0, anz_h-1)

    img = pic_parts(x,y)
    part = [img, (x,y)]
    rect = img.get_rect()
    rect.center = w_floor // 2, pic_pos_y // 2
    moving = False
    randlist = []
    zugzahl = 0
    while running:
        #screen = pygame.display.set_mode(size=(w_floor, h_floor))
        full_img.set_alpha(alphawert)
        screen.fill(GRAY)
        screen.blit(full_img, (pic_pos_x,pic_pos_y))
        font = pygame.font.Font(pygame.font.get_default_font(), 36)

        for element in partslist:
            screen.blit(element[0], element[1])

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
                    return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    moving = True

            elif event.type == pygame.MOUSEBUTTONUP:
                zugzahl += 1
                #screen_rect = img.get_rect()
                # print(f'Zugzahl: {zugzahl}')
                print(f'X: {rect.left} Ziel-X = {(x + (w_floor - width) / 2)}')
                print(f'Y: {rect.top}')
                drop_x = rect.left
                ziel_x = int(x+pic_pos_x)
                drop_y = rect.top
                ziel_y = int(y + pic_pos_y)
                if drop_x <= ziel_x + tolerance and drop_x >= ziel_x - tolerance and drop_y <= ziel_y + tolerance and drop_y >= ziel_y - tolerance:
                    # zugzahl += 1
                    part = [img, (int(x+pic_pos_x), int(y + pic_pos_y))]
                    partslist.append(part)
                    randlist.append((x, y))
                    counter += 1
                    print(f'Zugzahl: {zugzahl} / Counter: {counter}')
                    # font = pygame.font.Font(pygame.font.get_default_font(), 36)
                    # text_surface = pygame.font.Font.render(font, f'Hello world {counter}', True, (55, 55, 55))
                    # text_surface = pygame.font.Font.render(font, f'Hello world {counter}', True, (55, 55, 55))
                    # screen.blit(text_surface, dest=(50, 50))
                    # pygame.display.flip()
                    for i in range(0,30):
                        blit_grid(grid, (255,255,255))
                        pygame.display.flip()

                    if len(randlist) == (anz_h * anz_w):
                        #controlsWindow.point_counter.setText(str(counter))
                        #GRAY = (255,255,255)
                        fertig = True
                        init = False
                        text_surface = pygame.font.Font.render(font, f'Punkte: {counter}', True, (55, 55, 55))
                        screen.blit(text_surface, dest=(50, 50))
                        pygame.display.flip()
                        success(6)
                        return
                else:
                    counter -= 1
                    #controlsWindow.point_counter.setText(str(counter))

                if fertig == False:
                    x = part_size * random. randint(0,anz_w-1)
                    y = part_size * random. randint(0,anz_h-1)
                    while (x,y) in randlist:
                        x = part_size * random.randint(0, anz_w-1)
                        y = part_size * random.randint(0, anz_h-1)


                    img = pic_parts(x, y)

                    # part = [img, (x, y)]
                    # partslist.append(part)

                    rect = img.get_rect()
                    rect.center = w_floor // 2, pic_pos_y // 2
                moving = False
                #screen.fill(GRAY)
                #screen.blit(full_image, ((w - width) / 2, h - height))
                #screen.blit(img, rect)
                alphawert -= fade
                if alphawert <= 0:
                    alphawert = 0
                #controlsWindow.point_counter.setText(str(counter))

            elif event.type == pygame.MOUSEMOTION and moving == True:
                if fertig == False:
                    rect.move_ip(event.rel)


        screen.blit(img, rect)

        text_surface = pygame.font.Font.render(font, f'Punkte: {counter}', True, (55, 55, 55))
        screen.blit(text_surface, dest=(50, 50))

        pygame.draw.rect(screen, RED, rect, 1)
        #controlsWindow.point_counter.setText(str(counter))
        blit_grid(grid, RED)
        pygame.display.update()


def slider():
    global w_floor
    global h_floor
    global full_image_x
    global full_image_y
    global x_anz
    global y_anz

    moving = False
    fertig = False

    #Dictonary hat als Key die x,y Position im Grid und als Value das Image i
    # und dessen Koordinaten auf dem Spielfeld
    full_partsdict = {}
    # Dictonary hat als Key die x,y Werte aus full_partsdict und als Value das Image und dessen aktuelle Koordinaten auf dem Spielfeld
    act_pos_dict = {}


    running = True

    full_partsdict = make_full_partsdict(x_anz, y_anz)


    rand_values = []
    for key, value in full_partsdict.items():
        if key == (0,0):
            continue
        rand_x = random.randint(0, x_anz-1)
        rand_y = random.randint(0, y_anz-1)
        randpos = [rand_x, rand_y]
        while randpos in rand_values or randpos == [0, 0]:
            rand_x = random.randint(0, x_anz-1)
            rand_y = random.randint(0, y_anz-1)
            randpos = [rand_x, rand_y]
        rand_values.append(randpos)

        rand_pos_x = full_image_x + rand_x * part_size
        rand_pos_y = full_image_y + rand_y * part_size

        rand_coord = (rand_pos_x, rand_pos_y)

        act_pos_dict[(rand_x, rand_y)] = (value[0], rand_coord)
        #screen.blit(value[0], rand_coord)

    for key, value in act_pos_dict.items():
        screen.blit(value[0], value[1])

    print(x_anz*y_anz)
    for element in rand_values:
        print(element)


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
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(f'Mausposition: {event.pos}')
                pass
                # get mousposition
                eventpos_x, eventpos_y = event.pos
                # find x, y
                x_wert = int(eventpos_x - full_image_x) // part_size
                y_wert = int(eventpos_y - full_image_y) // part_size
                print(f'Coord: {x_wert} / {y_wert}')
                # img rect zuweisen aus dict_actualPosition
                img = act_pos_dict[(x_wert, y_wert)][0]
                rect = img.get_rect()
                rect.center = (full_image_x + x_wert*part_size + part_size//2), (full_image_y + y_wert*part_size + part_size//2)
                print(f'RECT_CENTER: {rect.center}')
                if rect.collidepoint(event.pos):
                    moving = True
                    print("moving")

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

                pygame.display.update()

            elif event.type == pygame.MOUSEBUTTONUP:
                moving = False


                drop_x = rect.left
                drop_y = rect.top
                # find x, y
                x_neu = int(drop_x - full_image_x) // part_size
                y_neu = int(drop_y - full_image_y) // part_size
                print(f'x-neu: {x_neu} / y-neu: {y_neu}')
                if (x_neu, y_neu) == (x_wert, y_wert):
                    pass
                else:
                    #Neue Position im Dict eintragen
                    act_pos_dict[(x_neu, y_neu)] = (act_pos_dict[(x_wert, y_wert)][0],(full_image_x + x_neu*part_size, full_image_y + y_neu*part_size))
                    #Leergezogene Position löschen
                    del act_pos_dict[(x_wert, y_wert)]

                #Ausgabe der neuen Bildversion
                screen.fill(GRAY)
                for key, value in act_pos_dict.items():
                    screen.blit(value[0], value[1])
                    print(f'{key}')

                pygame.display.update()



    return


def pic_parts(x,y):

    pic = pygame.image.load(r"C:\Users\User\Desktop\tmp_resize.JPG")
    w, h = screen_width, screen_height
    screen = pygame.display.set_mode((w, h))
    screen.blit(pic, (0,0))

    # rect = pygame.Rect(x, y, part_size, part_size)
    rect = pygame.Rect(x*part_size, y*part_size, part_size, part_size)
    sub = screen.subsurface(rect)
    screenshot = pygame.Surface((part_size, part_size))
    screenshot.blit(sub, (0, 0))
    part = screenshot
    screen.fill(GRAY)

    return(part)

def make_full_partsdict(anz_x, anz_y):
    global full_image_x
    global full_image_y
    global part_size

    full_partsdict = {}

    for x in range(0, anz_x):
        for y in range(0,anz_y):
            #part = pic_parts(x,y)
            part_pos_x = full_image_x + x * part_size
            part_pos_y = full_image_y + y * part_size
            list_element = make_list_element(x,y, part_pos_x, part_pos_y)
            full_partsdict[(x,y)] = (list_element)

    return(full_partsdict)

def make_list_element(x,y, part_pos_x, part_pos_y):

    part = pic_parts(x, y)
    list_element = [part, (part_pos_x, part_pos_y)]
    return(list_element)


def make_grid(x_init, y_init, x_anz, y_anz, part_size):
    grid = {}

    for x_start in range(0, x_anz+1):
        grid[("h",(x_start, 0))] = [((x_init + (x_start * part_size)),y_init) , ((x_init + (x_start * part_size)), (y_init + (y_anz)*part_size))]

    for y_start in range(0, y_anz+1):
        grid[("v",(0, y_start))] = [(x_init, (y_init + (y_start * part_size))) , ((x_init + (x_anz)*part_size), (y_init + (y_start * part_size)) )]

    for key, value in grid.items():
        print(f'{key}: {value[0]} / {value[1]}')

    return(grid)

def blit_grid(grid, color):

    for key, value in grid.items():
        pygame.draw.line(screen, color, value[0], value[1], 3)
    #     print(f'{key}: {value[0]} / {value[1]}')


def success(anz):
    global partslist

    for element in partslist:
        screen.blit(element[0], element[1])
    for n in range(0, anz):
        for i in range(0, 25):
            blit_grid(grid, (255, 255, 255))
            pygame.display.flip()
        for j in range(0, 25):
            blit_grid(grid, (255, 0, 0))
            pygame.display.flip()


    #sucht nach Zufall ein Bild aus dem Spiuelbildverzeichnis
def find_pic():
    import os

    global game_dir

    full_pic_dict = {}
    file_count = 0

    for root, dirs, files in os.walk(game_dir):
        for file in files:
            if ".png" in file or ".jpg" in file or ".jpeg" in file or ".PNG" in file or ".JPG" in file or ".JPEG" in file:
                file_count += 1
                path = os.path.join(root, file)
                full_pic_dict[file_count] = path


    # print(f'Files: {file_count}')

    daily_pic = random.randint(1, file_count)
    daily_pic_file = full_pic_dict[daily_pic]
    return(daily_pic_file)
def start_game(game):
    global init

    pygame.init()

    # FPS = 60
    # GRAY = (150, 150, 150)

    clock = pygame.time.Clock()
    #controlsWindow.lower()
    init = True
    while True:
        start(game)


if __name__ == '__main__':
    #spielbild = r"C:\Users\User\Desktop\Algarve 75\Algarve 75 740.JPEG"
    # spielbild = find_pic()
    #mouse_move()
    controlsWindow.show()
    controlsWindow.puzzle_start.clicked.connect(lambda: start_game("puzzle"))
    controlsWindow.slider_start.clicked.connect(lambda: start_game("slider"))
    #controlsWindow.point_counter.setText("Punkte")
    #controlsWindow.point_counter.show()
    # init = True
    # while True:
    #     start()

    #pic_parts()


sys.exit(app.exec())
pygame.quit()

