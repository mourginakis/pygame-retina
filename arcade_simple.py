"""
Simple version — no custom shader, just arcade.draw_points()
"""
import math
import arcade

WINDOW_W, WINDOW_H = 1280, 800
NUM_POINTS = 50_000  # Less points because CPU has to update them



class SimpleViewer(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_W, WINDOW_H, "Simple Points", update_rate=1/60)
        self.background_color = (10, 10, 15)
        self.t = 0.0
        
        print(f"Framebuffer: {self.ctx.fbo.width}x{self.ctx.fbo.height}")
        print(f"Rendering {NUM_POINTS:,} points (no shader)")

    def on_update(self, dt):
        self.t += dt

    def on_draw(self):
        self.clear()
        
        # Build point list every frame (this is the slow part)
        points = []
        for i in range(NUM_POINTS):
            frac  = i / NUM_POINTS
            angle = frac * 50.0 * 0.01 + self.t * 0.5
            radius = frac * min(WINDOW_W, WINDOW_H) * 0.45
            
            x = WINDOW_W / 2 + math.cos(angle) * radius
            y = WINDOW_H / 2 + math.sin(angle) * radius
            points.append((x, y))
        
        # Draw all points (Arcade uses its built-in shader)
        arcade.draw_points(points, arcade.color.WHITE, 2)


if __name__ == "__main__":
    SimpleViewer()
    arcade.run()

