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

        self.filter_loop = QPushButton("Play", self)
        self.filter_loop.setGeometry(170, 330, 130, 20)
        self.filter_loop.setCheckable(True)
        self.filter_loop.setStyleSheet(
            ":checked{background: solid red}"
            ":checked{border: 2px solid lightblue}"
            ":!checked{background-color: rgb(255,255,255)}"
            ":!checked{border: 2px solid red}"
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
fade_factor = 2


game_dir = r"D:\Pictures\Bilderserien\Jahre\2020"

def start():
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
    global font

    RED = (255, 0, 0)
    GRAY = (150, 150, 150)

    #w_floor, h_floor = screen_width - screen_width // 6, screen_height - 30
    game_x = screen_width - w_floor
    game_y = screen_height - h_floor

    os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (game_x, game_y)
    os.environ['SDL_WINDOW_ALWAYS_ON_TOP'] = '%s' % ('SDL_VIDEO_WINDOW')

    screen = pygame.display.set_mode(size=(w_floor, h_floor))
    pygame.display.set_caption("PicTris")

    # font = pygame.font.Font(pygame.font.get_default_font(), 36)
    #
    # number = 12
    #
    # # now print the text
    # text_surface = pygame.font.Font.render(font, f'Hello world {number}', True, (55, 55, 55))
    # screen.blit(text_surface, dest=(50, 50))

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

    x_anz = math.floor(width / part_size)
    y_anz = math.floor(height / part_size)

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

    mouse_move()
    return


def resize(file):

    fixed_height = 650
    image = Image.open(file)
    height_percent = (fixed_height / float(image.size[1]))
    width_size = int((float(image.size[0]) * float(height_percent)))
    image = image.resize((width_size, fixed_height), Image.NEAREST)
    image.save(r"C:\Users\User\Desktop\tmp_resize.JPG")

    return(image)

def mouse_move():
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
    fade = int((alphawert // (anz_h * anz_w))*fade_factor)
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
        screen = pygame.display.set_mode(size=(w_floor, h_floor))
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


def pic_parts(x,y):

    pic = pygame.image.load(r"C:\Users\User\Desktop\tmp_resize.JPG")
    pic_width, pic_height = pic.get_width(), pic.get_height()
    w, h = screen_width, screen_height
    screen = pygame.display.set_mode((w, h))
    screen.blit(pic, (0,0))

    rect = pygame.Rect(x, y, part_size, part_size)
    sub = screen.subsurface(rect)
    screenshot = pygame.Surface((part_size, part_size))
    screenshot.blit(sub, (0, 0))
    part = screenshot
    #screen.blit(backdrop, (0, 0))
    screen.blit(part,(800,pic_width))
    return(part)

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
def start_game():
    global init

    pygame.init()

    # FPS = 60
    # GRAY = (150, 150, 150)

    clock = pygame.time.Clock()
    #controlsWindow.lower()
    init = True
    while True:
        start()


if __name__ == '__main__':
    #spielbild = r"C:\Users\User\Desktop\Algarve 75\Algarve 75 740.JPEG"
    # spielbild = find_pic()
    #mouse_move()
    controlsWindow.show()
    controlsWindow.filter_loop.clicked.connect(start_game)
    #controlsWindow.point_counter.setText("Punkte")
    #controlsWindow.point_counter.show()
    # init = True
    # while True:
    #     start()

    #pic_parts()


sys.exit(app.exec())
pygame.quit()

