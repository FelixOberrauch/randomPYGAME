import pygame as pg
import os
from pygame.draw import circle
from submodule import *
from Defender import *

# ____SETUP____
pg.init()
WIDTH,HEIGHT =  1536,1024
screen = pg.display.set_mode((WIDTH, HEIGHT))
load_defender_assets()
load_bullet_assets()
clock = pg.time.Clock()
script_dir = os.path.dirname(__file__)
bg_path = os.path.join(script_dir, "assets", "Background.jpg")
background = pg.image.load(bg_path)
CIRCLE_ORIGIN = pg.math.Vector2(1500, 30)
circle_def = CIRCLE_ORIGIN.copy()
zombie_walking_path = os.path.join(script_dir, "assets", "zombie_walking.png")
zombie_walking_image = pg.image.load(zombie_walking_path)

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
Defenders = []

# ___Colours___
white = (255, 255, 255)
red = (255, 0, 0)
black = (0,0,0)
blue = (0, 0, 255)
green = (0, 255, 0)
brown = (181, 122, 0)

# ___INSTANTIATE___
health_pl = 200
attackers = []
spawn_queue = 0
current_round = 0
round_start = False
current_attacker_health = 20
last_spawn_time = 0
spawn_delay = 100  # 100 milliseconds between spawns
drag_offset = pg.math.Vector2(0,0)
bullets = []
last_shot_time = 0
rect_gui = pg.Rect(1468,0,200,1024)
dragging = False
running = True
zombie_walking_path = os.path.join(script_dir, "assets", "zombie_walking.png")
zombie_walking_image = pg.image.load(zombie_walking_path).convert_alpha()
zombie_walking_image = pg.transform.scale(zombie_walking_image, (80, 80))
i = 2

# ___Text___
font = pg.font.SysFont('arial', 24)

while running:
    # ___EVENTS___
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pg.math.Vector2(event.pos)
                if rect_gui.collidepoint(event.pos) and (mouse_pos - circle_def).length() <= 40:
                    dragging = True
                    drag_offset = mouse_pos - circle_def
        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1 and dragging:
                if not rect_gui.collidepoint(pg.mouse.get_pos()):
                    Defenders.append(circle_def.copy())
                dragging = False
                circle_def = CIRCLE_ORIGIN.copy()
    
    # ___LOGIC___
    # Spawn attackers from queue
    if spawn_queue > 0:
        current_time = pg.time.get_ticks()
        if current_time - last_spawn_time > spawn_delay:
            attackers.append(Attacker(ROAD_PATH, health=current_attacker_health))
            spawn_queue -= 1
            last_spawn_time = current_time
    
    # Update attackers
    for attacker in attackers[:]:
        attacker.update()
        if not attacker.alive:
            attackers.remove(attacker)
    
    # Update bullets
    for bullet in bullets[:]:
        bullet.update()
        if not bullet.active:
            bullets.remove(bullet)
            
    # Defenders shoot
    current_time = pg.time.get_ticks()
    if current_time - last_shot_time > 500: # Every 0.5 seconds
        for def_pos in Defenders:
            # Find a target in range
            target = None
            for enemy in attackers:
                if enemy.alive and (def_pos - enemy.pos).length() < 100:
                    target = enemy
                    break # Just target the first one in range
            
            if target:
                bullets.append(Bullet(def_pos, target))
        last_shot_time = current_time

    # Round progression
    if not attackers and spawn_queue == 0:
        if i == 0:
            current_round += 1
        else:
            i -= 1
        # Start next round
        if current_round <= 40:
            spawn_queue = current_round
        elif current_round <= 60:
            spawn_queue = 40
            current_attacker_health *= 1.5
        elif current_round <= 80:
            spawn_queue = 50
            current_attacker_health *= 50 
        # Optional: reset last_spawn_time to trigger immediate first spawn
        last_spawn_time = pg.time.get_ticks() - spawn_delay
        
    if dragging:
        circle_def.x = pg.mouse.get_pos()[0] - drag_offset.x
        circle_def.y = pg.mouse.get_pos()[1] - drag_offset.y
   
    # ___RENDER___
    screen.blit(background, (0, 0))
    # Draw placed defenders
    for def_pos in Defenders:
        draw_range(screen, def_pos)
        Defend_1(screen, red, def_pos)
    # Draw Health and Round
    draw_text(f"Health: {health_pl}", 10, 5,font,screen)
    draw_text(f"Round: {current_round}", 200, 5,font,screen)
    # Draw bullets
    for bullet in bullets:
        bullet.draw(screen)
        
    Defendgui(1468, 0, 200, 1024, screen, brown, red, circle_def)
    # Draw all attackers
    for attacker in attackers:
        attacker.draw(screen, zombie_walking_image)

    pg.display.update()
    clock.tick(60)

pg.quit()
