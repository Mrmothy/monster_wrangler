import pygame, random
from os.path import join


#Initialize Pygame
pygame.init()

#Set display window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Monster Wrangler")


#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#TODO Define Classes
class Game():
    """A class to control gameplay"""
    def __init__(self) -> None:
        """Initialize the game object"""
        pass

    def update(self):
        """Update our game object"""
        pass

    def draw(self):
        """Draw the hud and other to the display"""
        pass

    def check_collisions(self):
        """Check for collisions between players and monsters"""
        pass

    def start_new_round(self):
        """Populate board with new monsters"""
        pass

    def chose_new_target(self):
        """Choose a new target monster for the player"""
        pass

    def pause_game(self):
        """Pause the game"""
        pass

    def rest_game(self):
        """Rest the game"""
        pass

class Player(pygame.sprite.Sprite):
    """A player class that the user can control"""
    def __init__(self):
        """Initialize the player"""
        pass

    def update(self):
        """Update the player"""
        pass

    def warp(self):
        """Warp the player to safe zone"""
        pass

    def resets_player(self):
        """Rests the player to starting position"""
        pass

class Monster(pygame.sprite.Sprite):
    """A class to create enemy monster objects"""
    def __init__(self):
        """Initialize the monster"""
        pass

    def update(self):
        """Update the monster"""
        pass


#*Start game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    #Fill display
    display_surface.fill((0, 0, 0))

    #Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)

#*End game loop
pygame.quit()