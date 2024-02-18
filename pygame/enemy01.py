import pygame as pg
import random as r

class Enemy:
    def __init__(self, SW, SH, PS):
        ES = PS / 2  # Enemy size
        SPEED = 3  # Enemy speed
        self.hp = 2  # Health points
        self.d = 0  # Defense
        self.a = 1  # Attack
        self.s = SPEED  # Speed
        self.i = None  # Enemy image
        try:
            self.i = pg.image.load('enemy.png')  # Load image
            self.i = pg.transform.scale(self.i, (int(ES), int(ES)))  # Scale image
        except FileNotFoundError:
            self.i = pg.Surface((int(ES), int(ES)))  # Fallback to square
            self.i.fill((255, 0, 0))  # Enemy color
        self.r = self.i.get_rect(center=(r.choice([0, SW - int(ES)]), r.choice([0, SH - int(ES)])))  # Enemy rect

    def update(self, player1, player2):
        # Calculate the distance to each player
        dist_to_player1 = ((self.r.x - player1.r.x)**2 + (self.r.y - player1.r.y)**2)**0.5
        dist_to_player2 = ((self.r.x - player2.r.x)**2 + (self.r.y - player2.r.y)**2)**0.5

        # Determine which player is closer
        if dist_to_player1 < dist_to_player2:
            target = player1
        else:
            target = player2

        # Calculate the direction to the target
        dx = target.r.x - self.r.x
        dy = target.r.y - self.r.y
        dist = max(1, (dx**2 + dy**2)**0.5)

        # Move towards the target
        self.r.x += self.s * dx / dist
        self.r.y += self.s * dy / dist

        # Check for collision with the target
        if self.r.colliderect(target.r):
            target.take_damage(self.a)

    def draw(self, sc):
        sc.blit(self.i, self.r)

    def take_damage(self, amt):
        self.hp -= max(0, amt - self.d)
        if self.hp <= 0:
            print("An enemy has been defeated!")
            self.kill()

    def kill(self):
        self.r.x = -100  # Move the enemy off-screen
        self.r.y = -100
        self.hp = 0  # Set the enemy's health points to 0
