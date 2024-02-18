import pygame as pg
from buildings import Building

class Map02:
    def __init__(self, SW, SH):
        self.SW = SW
        self.SH = SH
        self.has_enemies = False  # New attribute
        # Rest of your code...

        self.grass_color = (0, 255, 0)  # Green
        self.river_color = (0, 0, 255)  # Blue
        self.river_width = SW // 10  # River width is 1/10 of screen width
        self.buildings = [Building(100, 100, 50, 50, "Player 1's House")]  # Add buildings here
        self.start_position = (100 + 25, 100 + 60)  # Start position south of the house

    def draw(self, sc):
        # Draw grass
        sc.fill(self.grass_color)
        # Draw river at the bottom third of the screen
        pg.draw.rect(sc, self.river_color, pg.Rect(0, 2*self.SH // 3, self.SW, self.SH // 3))
        # Draw buildings
        for building in self.buildings:
            building.draw(sc)

    def in_river(self, rect):
        return pg.Rect(0, 2*self.SH // 3, self.SW, self.SH // 3).colliderect(rect)
    def at_exit(self, rect):
        return None