import pygame as pg
from buildings import Building

class Player1HouseFloor1:
    def __init__(self, SW, SH):
        self.SW = SW
        self.SH = SH
        self.floor_color = (139, 69, 19)  # Brown
        self.buildings = [Building(SW // 2, SH // 2, 50, 50, "Stairs Down")]  # Add buildings here
        self.start_position = (SW // 2, SH - 10)  # Start position south of the stairs
        self.has_enemies = False

    def draw(self, sc):
        # Draw floor
        sc.fill(self.floor_color)
        # Draw buildings
        for building in self.buildings:
            building.draw(sc)

    def at_exit(self, rect):
        for building in self.buildings:
            if building.door.colliderect(rect):
                return building.name
        return None

    def in_river(self, rect):
        return False