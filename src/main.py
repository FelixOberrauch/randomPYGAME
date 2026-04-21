import pygame as pg
import os
from submodule import *

# ____SETUP____
pg.init()
WIDTH,HEIGHT =  1536,1024
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
script_dir = os.path.dirname(__file__)
bg_path = os.path.join(script_dir, "assets", "Background.jpg")
background = pg.image.load(bg_path)
# ____coordinates____Road____Attackers____
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

# ___Colours___
white = (255, 255, 255)
red = (255, 0, 0)
black = (0,0,0)
blue = (0, 0, 255)
green = (0, 255, 0)
'''____Attackers____Path____
Dieser class "Follower" macht, dass die Attackers den Path folgen der mit ROAD_PATH vorgegeben ist'''
class Follower:
    def __init__(self, path):
        self.path = path
        self.current_point_idx = 0
        self.pos = pg.Vector2(path[0])  # Start at the first point
        self.speed = 3

    def update(self):
        if self.current_point_idx < len(self.path):
            target = pg.Vector2(self.path[self.current_point_idx])
            direction = target - self.pos  # Vector pointing to target
            
            # Check if we are "close enough" to the target
            if direction.length() < self.speed:
                self.pos = target  # Snap to target
                self.current_point_idx += 1  # Move to next point
            else:
                # Normalize makes the vector 1 unit long, then multiply by speed
                direction = direction.normalize()
                self.pos += direction * self.speed

    def draw(self, surface):
        pg.draw.circle(surface, (255, 0, 0), (int(self.pos.x), int(self.pos.y)), 10)

# --- INSTANTIATE ---
# Create one follower object before the loop starts
follower = Follower(ROAD_PATH)

running = True
while running:
    # ___EVENTS___
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    # ___LOGIC___
    follower.update() # This moves the follower toward the next point
    
    # ___RENDER___
    screen.blit(background, (0, 0))

    # Draw the path lines and nodes
    if len(ROAD_PATH) > 1:
        pg.draw.lines(screen, green, False, ROAD_PATH, 3) 
        for p in ROAD_PATH:
            pg.draw.circle(screen, red, p, 5)
    
    # Draw the follower
    follower.draw(screen)

    pg.display.flip()
    clock.tick(60)

pg.quit()
