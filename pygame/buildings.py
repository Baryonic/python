import pygame as pg

class Building:
    def __init__(self, x, y, width, height, name):
        self.name = name
        self.rect = pg.Rect(x, y, width, height)
        self.door = pg.Rect(x, y + height - 10, 20, 10)  # Door at the bottom of the building
        self.spawn_point = (x + width // 2, y + height + 10)  # Spawn point south of the door
        try:
            self.image = pg.image.load(f'{name}.png')  # Load image
            self.image = pg.transform.scale(self.image, (width, height))  # Scale image
        except FileNotFoundError:
            self.image = pg.Surface((width, height))  # Fallback to square
            self.image.fill((255, 255, 255))  # Building color (white)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pg.draw.rect(screen, (139, 69, 19), self.door)  # Draw the door in brown
        if self.image.get_at((0, 0)) == (255, 255, 255):  # If the building is a white square
            font = pg.font.Font(None, 32)  # Choose the font for the text (None means default font)
            text = font.render(self.name, True, (0, 0, 0))  # Create the text (True means anti-aliased)
            screen.blit(text, self.rect)  # Draw the text
