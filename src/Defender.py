import pygame as pg
import os

# Placeholder for the texture
pistolguy_img = None

def load_defender_assets():
    global pistolguy_img
    if pistolguy_img is not None:
        return # Already loaded
        
    script_dir = os.path.dirname(__file__)
    pistolguy_path = os.path.join(script_dir, "assets", "Pistolguy.png")
    try:
        # We can only call convert_alpha() after pg.display.set_mode()
        pistolguy_img = pg.image.load(pistolguy_path).convert_alpha()
        pistolguy_img = pg.transform.scale(pistolguy_img, (80, 80))
    except Exception as e:
        print(f"Error loading Pistolguy.png: {e}")
        pistolguy_img = None

def draw_range(screen, pos, radius=100):
    range_surface = pg.Surface((radius * 2, radius * 2), pg.SRCALPHA)
    pg.draw.circle(range_surface, (150, 150, 150, 60), (radius, radius), radius)
    pg.draw.circle(range_surface, (150, 150, 150, 100), (radius, radius), radius, 2)
    screen.blit(range_surface, (pos[0] - radius, pos[1] - radius))

def Defend_1(screen, color, pos):
    global pistolguy_img
    # Lazy load as a fallback
    if pistolguy_img is None:
        load_defender_assets()
        
    if pistolguy_img:
        rect = pistolguy_img.get_rect(center=(int(pos[0]), int(pos[1])))
        screen.blit(pistolguy_img, rect)
    else:
        surface = pg.Surface((30, 30), pg.SRCALPHA)
        pg.draw.circle(surface, (*color, 255), (15, 15), 15)
        screen.blit(surface, (pos[0] - 15, pos[1] - 15))

def Pistolguy(screen, color, pos):
    Defend_1(screen, color, pos)

def Defendgui(pos_x, pos_y, width, height, screen, color, colordef, circle_pos):
    pg.draw.rect(screen, color, pg.Rect(pos_x, pos_y, width, height)) 
    draw_range(screen, circle_pos)
    Defend_1(screen, colordef, circle_pos)
