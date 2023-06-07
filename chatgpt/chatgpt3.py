import pygame
import sys

# Initialize Pygame
pygame.init()

# Get the user's screen size
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Screen")

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Game logic and drawing code here

    # Update the screen
    pygame.display.flip()
