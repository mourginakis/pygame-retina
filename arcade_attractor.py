import math
import random

import arcade

# Constants
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
NUM_PARTICLES = 2000
FRICTION      = 0.98
ATTRACTOR_STRENGTH = 0.3


class Particle:
    __slots__ = ('x', 'y', 'vx', 'vy')
    
    def __init__(self, x: float, y: float):
        self.x  = x
        self.y  = y
        self.vx = 0.0
        self.vy = 0.0


class AttractorWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Particle Attractor")
        arcade.set_background_color(arcade.color.BLACK)
        
        self.particles: list[Particle] = []
        self.attractor_x = SCREEN_WIDTH / 2
        self.attractor_y = SCREEN_HEIGHT / 2
        
        # Spawn particles randomly
        for _ in range(NUM_PARTICLES):
            x = random.uniform(0, SCREEN_WIDTH)
            y = random.uniform(0, SCREEN_HEIGHT)
            self.particles.append(Particle(x, y))
    
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.attractor_x = x
        self.attractor_y = y
    
    def on_update(self, delta_time: float):
        ax = self.attractor_x
        ay = self.attractor_y
        
        for p in self.particles:
            # Direction to attractor
            dx = ax - p.x
            dy = ay - p.y
            
            # Distance (avoid division by zero)
            dist = math.sqrt(dx * dx + dy * dy) + 0.1
            
            # Normalize and apply force (inverse distance for smooth feel)
            force = ATTRACTOR_STRENGTH / dist
            p.vx += (dx / dist) * force
            p.vy += (dy / dist) * force
            
            # Apply friction
            p.vx *= FRICTION
            p.vy *= FRICTION
            
            # Update position
            p.x += p.vx
            p.y += p.vy
    
    def on_draw(self):
        self.clear()
        
        # Collect all points for batch drawing
        points = [(p.x, p.y) for p in self.particles]
        
        # Draw all particles as 1-pixel white dots
        arcade.draw_points(points, arcade.color.WHITE, size=1)


def main():
    window = AttractorWindow()
    arcade.run()


if __name__ == "__main__":
    main()

