import pygame as pg
import random as r

class Player1:
    def __init__(self, x, y, PS):
        self.hp = 10  # Health points
        self.d = 1  # Defense
        self.a = 1  # Attack
        self.s = 5  # Speed
        self.i = None  # Player image
        try:
            self.i = pg.image.load('player1.png')  # Load image
            self.i = pg.transform.scale(self.i, (PS, PS))  # Scale image
        except FileNotFoundError:
            self.i = pg.Surface((PS, PS))  # Fallback to square
            self.i.fill((0, 255, 255))  # Player color
        self.r = self.i.get_rect(center=(x, y))  # Player rect

    def update(self, game_map):
        new_rect = self.r.copy()
        k = pg.key.get_pressed()
        if k[pg.K_a]:
            new_rect.x -= self.s
        if k[pg.K_d]:
            new_rect.x += self.s
        if k[pg.K_w]:
            new_rect.y -= self.s
        if k[pg.K_s]:
            new_rect.y += self.s
        if not game_map.in_river(new_rect):
            self.r = new_rect

    def draw(self, sc):
        sc.blit(self.i, self.r)

    def take_damage(self, amt):
        self.hp -= max(0, amt - self.d)
        if self.hp <= 0:
            print("Player 1 died! Retry?")


class Player2(Player1):
    def update(self, game_map):
        new_rect = self.r.copy()
        k = pg.key.get_pressed()
        if k[pg.K_LEFT]:
            new_rect.x -= self.s
        if k[pg.K_RIGHT]:
            new_rect.x += self.s
        if k[pg.K_UP]:
            new_rect.y -= self.s
        if k[pg.K_DOWN]:
            new_rect.y += self.s
        if not game_map.in_river(new_rect):
            self.r = new_rect

    def take_damage(self, amt):
        self.hp -= max(0, amt - self.d)
        if self.hp <= 0:
            print("Player 2 died! Retry?")