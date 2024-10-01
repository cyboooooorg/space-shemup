import pygame
from pygame.locals import *  # noqa: F403

# Initialize Pygame
pygame.init()
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Window")

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:  # noqa: F405
            pygame.quit()
            exit()
    pygame.display.update()
