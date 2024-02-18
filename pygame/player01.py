import pygame as pg

class Player1:
    def __init__(self, x, y, PS):
        self.x = x
        self.y = y
        self.s = 5  # Speed
        self.PS = PS  # Player size
        self.hp = 100  # Initialize health points
        try:
            self.image = pg.image.load('player1.png')  # Load image
            self.image = pg.transform.scale(self.image, (PS, PS))  # Scale image
        except FileNotFoundError:
            self.image = pg.Surface((PS, PS))  # Fallback to square
            self.image.fill((255, 255, 0))  # Player color (yellow)
        self.r = self.image.get_rect()
        self.r.x = x
        self.r.y = y

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
    def draw(self, screen):
        screen.blit(self.image, self.r)
