import pygame as pg
import random as r
from player01 import Player1
from player02 import Player2
from enemy01 import Enemy



class Map:
    def __init__(self, SW, SH):
        self.SW = SW
        self.SH = SH
        self.grass_color = (0, 255, 0)  # Green
        self.river_color = (0, 0, 255)  # Blue
        self.river_width = SW // 10  # River width is 1/10 of screen width

    def draw(self, sc):
        # Draw grass
        sc.fill(self.grass_color)
        # Draw river in the middle
        pg.draw.rect(sc, self.river_color, pg.Rect(self.SW // 2 - self.river_width // 2, 0, self.river_width, self.SH))
        # Draw bridge
        bridge_width = self.river_width
        bridge_height = self.SH // 10
        bridge_color = (139, 69, 19)  # Brown
        pg.draw.rect(sc, bridge_color, pg.Rect(self.SW // 2 - bridge_width // 2, self.SH // 2 - bridge_height // 2, bridge_width, bridge_height))

    def in_river(self, rect):
        return pg.Rect(self.SW // 2 - self.river_width // 2, 0, self.river_width, self.SH).colliderect(rect)

