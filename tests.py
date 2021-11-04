import pygame
import sys
import os
import pyautogui
from PIL import Image
import random
import time

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

        self.slider9_start = QPushButton("Slider 9", self)
        self.slider9_start.setGeometry(170, 430, 130, 20)
        self.slider9_start.setCheckable(True)
        self.slider9_start.setStyleSheet(
            ":checked{background: solid lightblue}"
            ":checked{border: 2px solid red}"
            ":!checked{background-color: rgb(255,255,255)}"
            ":!checked{border: 2px solid lightblue}"
            ":!checked{font-size: 10px}"
        )

        self.slider15_start = QPushButton("Slider 15", self)
        self.slider15_start.setGeometry(170, 480, 130, 20)
        self.slider15_start.setCheckable(True)
        self.slider15_start.setStyleSheet(
            ":checked{background: solid lightblue}"
            ":checked{border: 2px solid red}"
            ":!checked{background-color: rgb(255,255,255)}"
            ":!checked{border: 2px solid lightblue}"
            ":!checked{font-size: 10px}"
        )

        self.sliderpix_start = QPushButton("Slider pix", self)
        self.sliderpix_start.setGeometry(170, 530, 130, 20)
        self.sliderpix_start.setCheckable(True)
        self.sliderpix_start.setStyleSheet(
            ":checked{background: solid lightblue}"
            ":checked{border: 2px solid red}"
            ":!checked{background-color: rgb(255,255,255)}"
            ":!checked{border: 2px solid lightblue}"
            ":!checked{font-size: 10px}"
        )

        self.pic_label = QtWidgets.QLabel()

        self.point_counter = QtWidgets.QLabel(self)
        self.point_counter.setGeometry(QtCore.QRect(170, 40, 47, 13))

screen_width, screen_height= pyautogui.size()
#print(f'Width: {screen_width} / Height: {screen_height}')
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

part_size = 200
alphawert = 255
tolerance = 25
part_anz_init = 4
game_rounds = 0
offset_y = 50
fade_factor = 1.4


game_dir = r"D:\Pictures\Bilderserien\Jahre"

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
    global screen_height
    global full_image_x
    global full_image_y
    global font
    global x_anz
    global y_anz

    RED = (255, 0, 0)
    GRAY = (150, 150, 150)

    if game == "puzzle" or game == "slider":
        if init == True:
            #spielbild = r"D:\Pictures\Bilderserien\Alphabet\26 zeichen\26work\26_finfin-1.jpg"
            spielbild = find_pic()
            # if game == "puzzle":
            #     part_anz = part_anz_init
            # else:
            #     part_anz = 5
            part_anz = part_anz_init
            game_rounds = 0
        else:
            game_rounds += 1
            part_anz = part_anz + game_rounds
    elif game == "slider 9":
        spielbild = r"C:\Users\User\Desktop\pictris\Zahlen ungerade.jpg"
        part_anz = 3
        game = "slider"
    elif game == "slider 15":
        spielbild = r"C:\Users\User\Desktop\pictris\Zahlen gerade.jpg"
        part_anz = 4
        game = "slider"

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

    control_pic = QtGui.QPixmap(r"C:\Users\User\Desktop\tmp_resize.JPG")
    controlsWindow.pic_label.setGeometry(screen_width - width - offset_y, screen_height - height - offset_y, width, height)
    controlsWindow.pic_label.setPixmap(control_pic)
    controlsWindow.pic_label.show()

    make_game_floor(game)

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
        move = False


    if game == "puzzle":
        puzzle()
    elif game == "slider":
        #time.sleep(5)
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
    #os.environ['SDL_WINDOW_ALWAYS_ON_TOP'] = '%s' % ('SDL_VIDEO_WINDOW')

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

    img = pic_parts(x,y, "puzzle")
    part = [img, (x,y)]
    rect = img.get_rect()
    rect.center = w_floor // 2, pic_pos_y // 2
    moving = False
    randlist = []
    zugzahl = 0

    while running:

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


            elif event.type == pygame.MOUSEMOTION and moving == True:
                if fertig == False:
                    rect.move_ip(event.rel)

            elif event.type == pygame.MOUSEBUTTONUP:
                zugzahl += 1

                #print(f'X: {rect.left} Ziel-X = {(x + (w_floor - width) / 2)}')
                #print(f'Y: {rect.top}')
                drop_x = rect.left
                ziel_x = int(x+pic_pos_x)
                drop_y = rect.top
                ziel_y = int(y + pic_pos_y)
                if drop_x <= ziel_x + tolerance and drop_x >= ziel_x - tolerance and drop_y <= ziel_y + tolerance and drop_y >= ziel_y - tolerance:
                    part = [img, (int(x+pic_pos_x), int(y + pic_pos_y))]
                    partslist.append(part)
                    randlist.append((x, y))
                    counter += 1
                    #print(f'Zugzahl: {zugzahl} / Counter: {counter}')

                    for i in range(0,30):
                        blit_grid(grid, (255,255,255))
                        pygame.display.flip()

                    if len(randlist) == (anz_h * anz_w):
                        fertig = True
                        init = False
                        text_surface = pygame.font.Font.render(font, f'Punkte: {counter}', True, (55, 55, 55))
                        screen.blit(text_surface, dest=(50, 50))
                        for element in partslist:
                            screen.blit(element[0], element[1])
                        pygame.display.flip()
                        success(6)
                        return
                else:
                    counter -= 1

                if fertig == False:
                    x = part_size * random. randint(0,anz_w-1)
                    y = part_size * random. randint(0,anz_h-1)
                    while (x,y) in randlist:
                        x = part_size * random.randint(0, anz_w-1)
                        y = part_size * random.randint(0, anz_h-1)

                    img = pic_parts(x, y, "puzzle")

                    rect = img.get_rect()
                    rect.center = w_floor // 2, pic_pos_y // 2
                moving = False

                alphawert -= fade
                if alphawert <= 0:
                    alphawert = 0



        screen.blit(img, rect)

        text_surface = pygame.font.Font.render(font, f'Punkte: {counter}', True, (55, 55, 55))
        screen.blit(text_surface, dest=(50, 50))

        pygame.draw.rect(screen, RED, rect, 1)

        blit_grid(grid, RED)
        pygame.display.update()


def slider():
    global w_floor
    global h_floor
    global full_image_x
    global full_image_y
    global x_anz
    global y_anz
    global part_anz

    moving = False
    fertig = False

    #Dictonary hat als Key die x,y Position im Grid und als Value das Image i
    # und dessen Koordinaten auf dem Spielfeld
    full_partsdict = {}
    # Dictonary hat als Key die x,y Werte aus full_partsdict und als Value das Image und dessen aktuelle Koordinaten auf dem Spielfeld
    act_pos_dict = {}


    running = True

    full_partsdict = make_full_partsdict(x_anz, y_anz, "slider")
    grid = make_grid(full_image_x, full_image_y, x_anz, y_anz, part_size)

    unlösbar = True
    while unlösbar == True:
        rand_values = []
        for key, value in full_partsdict.items():
            # print(f'Ordnung: {value[2]}, Wert: {value[3]}')
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
            #rand_order = rand_x+1 + (rand_y) * x_anz
            rand_order = rand_y * x_anz + rand_x + 1
            rand_values.append(randpos)

            rand_pos_x = full_image_x + rand_x * part_size
            rand_pos_y = full_image_y + rand_y * part_size

            rand_coord = (rand_pos_x, rand_pos_y)

            act_pos_dict[(rand_x, rand_y)] = (value[0], rand_coord, rand_order, value[3])
            #print(f'{key[0]}/{key[1]} Erzeugungs_Ordnung: {rand_order} / {rand_coord} Wert: {value[3]}')
            #screen.blit(value[0], rand_coord)
        #for key, value in dict(sorted(act_pos_dict.items(), key=lambda x: x[1][2])).items():
            #print(f'{key[0]}/{key[1]} Sortierte_Ordnung: {value[2]}, Wert: {value[3]}')

        #Paritäts-Check auf Lösbarkeit
        n1 = 0
        for key, value in dict(sorted(act_pos_dict.items(),key=lambda x: x[1][2])).items():
            # Wobei x[1] für Value steht (x[0] wäre der key) und der zweite Wert in der eckigen Klamer die Position in der Value-Liste bezeichnet
            #print(f'Ordnung: {value[2]}, Wert: {value[3]}')
            order = value[2]
            reference = value[3]
            count = 1
            single_count = 0
            for key, value in dict(sorted(act_pos_dict.items(), key=lambda x: x[1][2])).items():
                if count >= order-1:
                    break
                if value[3] > reference:
                    n1 +=1
                    single_count += 1
                count += 1
            #print(f'Wert: {value[3]} -> {single_count}')


        print(f'N1: {n1}')
        n = y_anz
        parity = n + n1
        print(f'Parity: {parity}')
        if ((y_anz % 2) == 0 and (parity % 2) != 0) or ((y_anz % 2) != 0 and (parity % 2) != 0):
            # print("unlösbar")
            # unlösbar = True
            print("lösbar")
            unlösbar = False
        else:
            # print("lösbar")
            # unlösbar = False
            print("unlösbar")
            unlösbar = True


    for key, value in act_pos_dict.items():
        #print(f'Publikations_Ordnung: {value[2]} / {value[1]}, Wert: {value[3]}')
        screen.blit(value[0], value[1])
    blit_grid(grid, (255,0,0))


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
                #print(f'Mausposition: {event.pos}')
                #pass
                # get mousposition
                eventpos_x, eventpos_y = event.pos
                # find x, y
                x_wert = int(eventpos_x - full_image_x) // part_size
                y_wert = int(eventpos_y - full_image_y) // part_size
                #print(f'Coord: {x_wert} / {y_wert}')
                #Absturz bei Klick in leeres Feld verhindern
                if (x_wert, y_wert) not in act_pos_dict.keys():
                    print("leeres Feld")
                else:
                    # img rect zuweisen aus dict_actualPosition
                    img = act_pos_dict[(x_wert, y_wert)][0]
                    rect = img.get_rect()
                    rect.center = (full_image_x + x_wert*part_size + part_size//2), (full_image_y + y_wert*part_size + part_size//2)
                    #print(f'RECT_CENTER: {rect.center}')
                    if rect.collidepoint(event.pos):
                        moving = True
                        #print("moving")

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

                # find x, y
                x_neu = int(drop_x - full_image_x) // part_size
                y_neu = int(drop_y - full_image_y) // part_size

                # Nur auf angrenzende leere Felder ablegen
                if (x_neu, y_neu) in act_pos_dict.keys():
                    pass
                elif x_neu < 0 or x_neu > x_anz:
                    pass
                elif y_neu < 0 or y_neu > y_anz:
                    pass
                elif abs(x_neu - x_wert) > 1:
                    pass
                elif abs(y_neu - y_wert) > 1:
                    pass
                elif (abs(x_neu - x_wert) + abs(y_neu - y_wert)) > 1:
                    pass
                else:
                    #Neue Position und Feldordnungswert im Dict eintragen
                    feldordnungswert = y_neu*x_anz + x_neu
                    act_pos_dict[(x_neu, y_neu)] = (act_pos_dict[(x_wert, y_wert)][0],(full_image_x + x_neu*part_size, full_image_y + y_neu*part_size), feldordnungswert, act_pos_dict[(x_wert, y_wert)][3])
                    #Leergezogene Position löschen
                    del act_pos_dict[(x_wert, y_wert)]

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
                            pygame.display.flip()
                            success(6)
                            return
                        else:
                            i +=1
                    else:
                        break

                blit_grid(grid, (255, 0, 0))
                pygame.display.update()



    return


def pic_parts(x,y,game):
    global w_floor

    pic = pygame.image.load(r"C:\Users\User\Desktop\tmp_resize.JPG")
    w, h = screen_width - (screen_width - w_floor), screen_height
    screen = pygame.display.set_mode((w, h))
    screen.blit(pic, (0,0))

    if game == "puzzle":
        rect = pygame.Rect(x, y, part_size, part_size)
    if game == "slider":
        rect = pygame.Rect(x*part_size, y*part_size, part_size, part_size)
    sub = screen.subsurface(rect)
    screenshot = pygame.Surface((part_size, part_size))
    screenshot.blit(sub, (0, 0))
    part = screenshot
    screen.fill(GRAY)

    return(part)

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
    part = pic_parts(x, y,game)
    list_element = [part, (part_pos_x, part_pos_y), order, value]
    return(list_element)


def make_grid(x_init, y_init, x_anz, y_anz, part_size):
    grid = {}

    for x_start in range(0, x_anz+1):
        grid[("h",(x_start, 0))] = [((x_init + (x_start * part_size)),y_init) , ((x_init + (x_start * part_size)), (y_init + (y_anz)*part_size))]

    for y_start in range(0, y_anz+1):
        grid[("v",(0, y_start))] = [(x_init, (y_init + (y_start * part_size))) , ((x_init + (x_anz)*part_size), (y_init + (y_start * part_size)) )]

    #for key, value in grid.items():
        #print(f'{key}: {value[0]} / {value[1]}')

    return(grid)

def blit_grid(grid, color):

    for key, value in grid.items():
        pygame.draw.line(screen, color, value[0], value[1], 3)
    #     print(f'{key}: {value[0]} / {value[1]}')


def success(anz):
    global partslist

    # for element in partslist:
    #     screen.blit(element[0], element[1])
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
    clock = pygame.time.Clock()

    init = True
    while True:
        start(game)


if __name__ == '__main__':
    #spielbild = r"C:\Users\User\Desktop\Algarve 75\Algarve 75 740.JPEG"
    # spielbild = find_pic()

    controlsWindow.show()
    controlsWindow.puzzle_start.clicked.connect(lambda: start_game("puzzle"))
    controlsWindow.slider9_start.clicked.connect(lambda: start_game("slider 9"))
    controlsWindow.slider15_start.clicked.connect(lambda: start_game("slider 15"))
    controlsWindow.sliderpix_start.clicked.connect(lambda: start_game("slider"))

    # init = True
    # while True:
    #     start()

    #pic_parts()


sys.exit(app.exec())
pygame.quit()

