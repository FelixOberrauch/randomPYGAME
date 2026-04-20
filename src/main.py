import pygame as pg
from submodule import *

# ____SETUP_____
pg.init()
HEIGHT, WIDTH = 1920 ,1080
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
background = pg.image.load("assets/Background.jpg")

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
    screen.fill(background)

    pg.draw.rect(screen, (255,255,0), pg.Rect(100,100,100,50))

    


    pg.display.flip()


pg.quit()