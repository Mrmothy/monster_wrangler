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

#Start game loop
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

#End game loop
pygame.quit()