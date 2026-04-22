import pygame as pg
import os

# Placeholder for bullet texture
bullet_img = None

def load_bullet_assets():
    global bullet_img
    if bullet_img is not None:
        return
        
    script_dir = os.path.dirname(__file__)
    bullet_path = os.path.join(script_dir, "assets", "bullet.png")
    try:
        bullet_img = pg.image.load(bullet_path).convert_alpha()
        # Scale bullet to a reasonable size (e.g., 20x10)
        bullet_img = pg.transform.scale(bullet_img, (20, 10))
    except Exception as e:
        print(f"Error loading bullet.png: {e}")
        bullet_img = None

class Follower:
    def __init__(self, path):
        self.path = path
        self.current_point_idx = 0
        self.pos = pg.Vector2(path[0])
        self.speed = 3

    def update(self):
        if self.current_point_idx < len(self.path):
            target = pg.Vector2(self.path[self.current_point_idx])
            direction = target - self.pos
            if direction.length() < self.speed:
                self.pos = target
                self.current_point_idx += 1
            else:
                self.pos += direction.normalize() * self.speed

    def draw(self, surface):
        pg.draw.circle(surface, (255, 0, 0), (int(self.pos.x), int(self.pos.y)), 10)

class Attacker:
    def __init__(self, path):
        self.path = path
        self.current_point_idx = 0
        self.pos = pg.Vector2(path[0])
        self.speed = 1.5
        self.health = 20
        self.max_health = 20
        self.alive = True
        self.radius = 12

    def update(self):
        if not self.alive:
            return
            
        if self.current_point_idx < len(self.path):
            target = pg.Vector2(self.path[self.current_point_idx])
            direction = target - self.pos
            
            if direction.length() < self.speed:
                self.pos = target
                self.current_point_idx += 1
            else:
                self.pos += direction.normalize() * self.speed
        else:
            self.alive = False

    def draw(self, surface):
        if not self.alive:
            return
            
        pg.draw.circle(surface, (200, 0, 0), (int(self.pos.x), int(self.pos.y)), self.radius)
        
        bar_width = 30
        bar_height = 4
        bar_x = self.pos.x - bar_width // 2
        bar_y = self.pos.y - self.radius - 10
        pg.draw.rect(surface, (100, 0, 0), (bar_x, bar_y, bar_width, bar_height))
        
        health_ratio = max(0, self.health / self.max_health)
        pg.draw.rect(surface, (0, 200, 0), (bar_x, bar_y, int(bar_width * health_ratio), bar_height))

class Bullet:
    def __init__(self, start_pos, target_obj):
        self.pos = pg.Vector2(start_pos)
        self.target = target_obj
        self.speed = 12
        self.active = True
        
    def update(self):
        if not self.target or not self.target.alive:
            self.active = False
            return
            
        direction = self.target.pos - self.pos
        if direction.length() < self.speed:
            self.pos = pg.Vector2(self.target.pos)
            self.target.health -= 1
            if self.target.health <= 0:
                self.target.alive = False
            self.active = False
        else:
            self.pos += direction.normalize() * self.speed
            
    def draw(self, surface):
        if not self.active:
            return

        global bullet_img
        if bullet_img is None:
            load_bullet_assets()
            
        direction = self.target.pos - self.pos
        if direction.length() > 0:
            angle = direction.angle_to(pg.Vector2(1, 0))
            if bullet_img:
                # Rotate the bullet texture
                rotated_surf = pg.transform.rotate(bullet_img, angle)
                surface.blit(rotated_surf, rotated_surf.get_rect(center=(int(self.pos.x), int(self.pos.y))))
            else:
                # Fallback to green rectangle
                bullet_surf = pg.Surface((12, 6), pg.SRCALPHA)
                pg.draw.rect(bullet_surf, (0, 255, 0), (0, 0, 12, 6))
                rotated_surf = pg.transform.rotate(bullet_surf, angle)
                surface.blit(rotated_surf, rotated_surf.get_rect(center=(int(self.pos.x), int(self.pos.y))))
