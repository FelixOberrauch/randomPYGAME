import pygame as pg

pg.init()

import pygame as pg

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

