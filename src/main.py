import pygame as pg
from submodule import *

# ____SETUP_____
pg.init()
HEIGHT, WIDTH = 1920 ,1080
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

#___Collors___
white = (255, 255, 255)
red = (255, 0, 0)
black = (0,0,0)
blue = (0, 0, 255)
green = (0, 255, 0)

running = True
while running:
    #___EVENTS___
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    #___RENDER___
    pg.draw.rect(screen, (255,255,0), pg.Rect(50,50,5,50))

    screen.fill(white)


    pg.display.flip()


pg.quit()