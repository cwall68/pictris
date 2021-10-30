import pygame
import sys

screen = pygame.display.set_mode((1000, 900))
clock = pygame.time.Clock()


def grab(x, y, w, h):
    "Grab a part of the screen"
    # get the dimension of the surface
    rect = pygame.Rect(x, y, w, h)
    # copy the part of the screen
    sub = screen.subsurface(rect)
    # create another surface with dimensions
    # This is done to unlock the screen surface
    # Unlock screen surface here:
    screenshot = pygame.Surface((w, h))
    screenshot.blit(sub, (0, 0))
    return screenshot


def blit(part, x, y):
    screen.blit(part, (x, y))



def quit():
    pygame.quit()
    sys.exit()


def start():
    parts = {}
    dif = 50
    x = 100
    y = 100
    # shows half the screen
    blit(face, 0, 0)
    #blit(backdrop,0,0)
    # and the other half copied
    for i in range (0,10):
        teil = grab(i*100, 400, 100, 100)
        name = "part"+str(i)
        parts[name] = teil


    for key, value in parts.items():
        print(key)
    #blit(sub, 100, 100)
    for key, value in parts.items():
        y = 0
        part = value

        while y < 750:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit()
                    if event.key == pygame.K_LEFT:
                        x -= dif
                    if event.key == pygame.K_RIGHT:
                        x += dif
                    if event.key == pygame.K_DOWN:
                        y = 750
            y += 1
            blit(backdrop, 0, 0)
            blit(part, x, y)
            pygame.display.update()
            clock.tick(60)
        else:
            blit(backdrop, 0, 0)
            pygame.display.update()
            continue



# 119 x 175
face = pygame.image.load(r"C:\Users\User\Desktop\tmp_resize.JPG")
backdrop = pygame.image.load(r"C:\Users\User\PycharmProjects\pictris\Grafiken\pictris_backdrop.png")

start()