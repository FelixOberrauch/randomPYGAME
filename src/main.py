import pygame as pg
import os
from submodule import *

# ____SETUP_____
pg.init()
WIDTH,HEIGHT =  1536,1024
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
script_dir = os.path.dirname(__file__)
bg_path = os.path.join(script_dir, "assets", "Background.jpg")
background = pg.image.load(bg_path)

ROAD_PATH = [
    (1293,1024),
    (1162,852),
    (1162,803),
    (1225,718),
    (1346,628),
    (1383,500),
    (1300,420),
    (1160,430),
    (1015,500),
    (940,625),
    (875,740),
    (770,810),
    (580,905),
    (340,965),
    (345,900),
    (350,845),
    (370,750),
    (430,685),
    (510,650),
    (630,635),
    (720,600),
    (740,540),
    (700,470),
    (465,380),
    (300,315),
    (275,265),
    (285,210),
    (370,130),
    (475,125),
    (590,170),
    (700,230),
    (830,225),
    (950,180),
    (1055,170),
    (1175,150),
    (1205,50)
]

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
    screen.blit(background, (0, 0))
#    pg.display.flip()
    clock.tick(60)
    
    screen.blit(background, (0, 0))


    if len(ROAD_PATH) > 1:
        pg.draw.lines(screen, (0, 255, 0), False, ROAD_PATH, 3) # Green line
        for p in ROAD_PATH:
            pg.draw.circle(screen, (255, 0, 0), p, 5) # Red dots at turns
    
    pg.display.flip()
    


pg.quit()