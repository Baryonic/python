import pygame as pg
from map01 import Map
from player01 import Player1
from player02 import Player2
from enemy01 import Enemy
from map02 import Map02
from player1house import Player1House
from player1housefloor1 import Player1HouseFloor1

# Initialize game
pg.init()
info = pg.display.Info()
screen_width, screen_height = info.current_w, info.current_h
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()

player_size = 50  # Player size

# Create game objects
game_map = Map02(screen_width, screen_height)
inside_house = False  # Flag to check if the player is inside the house
player1 = Player1(game_map.river_width/2 - player_size, screen_height/2, player_size)
player2 = Player2(screen_width - game_map.river_width/2 + player_size, screen_height/2, player_size)
enemies = [Enemy(screen_width, screen_height, player_size) for _ in range(10)]

running = True
while running:
    pg.event.pump()

    # Update game state
    player1.update(game_map)
    player2.update(game_map)
    
    # Handle enemy logic only if the current map has enemies
    if game_map.has_enemies:
        for enemy in enemies:
            enemy.update(player1, player2)

    # Draw everything
    game_map.draw(screen)
    player1.draw(screen)
    player2.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)

    # Update the display
    pg.display.flip()

    # Check for game over
    if player1.hp <= 0:
        print("Player 2 is the winner!")
        running = False
    elif player2.hp <= 0:
        print("Player 1 is the winner!")
        running = False

    # Check if Player 1 is at a door
    for building in game_map.buildings:
        if building.door.colliderect(player1.r):
            inside_house = True
            game_map = Player1House(screen_width, screen_height)
            player1.r.x, player1.r.y = game_map.start_position  # Set player's position
            break

    # Check if Player 1 is at the stairs
    exit_building = game_map.at_exit(player1.r)
    if exit_building is not None:
        if exit_building == "Stairs":
            game_map = Player1HouseFloor1(screen_width, screen_height)
        elif exit_building == "Door":
            game_map = Map02(screen_width, screen_height)
        elif exit_building == "Stairs Down":
            game_map = Player1House(screen_width, screen_height)
        player1.r.x, player1.r.y = game_map.start_position  # Set player's position

    # Cap the frame rate
    clock.tick(60)

pg.quit()
