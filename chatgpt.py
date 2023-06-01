import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
window_size = (400, 300)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Timer")

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the font
font = pygame.font.Font(None, 64)

# Set up the timer variables
clock = pygame.time.Clock()
time_limit = 60  # Time limit in seconds
time_remaining = time_limit * 1000  # Convert time limit to milliseconds

# Start the timer
start_time = pygame.time.get_ticks()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the window
    window.fill(WHITE)

    # Calculate the time remaining
    elapsed_time = pygame.time.get_ticks() - start_time
    time_remaining = max(time_limit * 1000 - elapsed_time, 0)

    # Convert the time remaining to seconds
    seconds = time_remaining // 1000

    # Render the time on the screen
    time_text = font.render(str(seconds), True, BLACK)
    text_rect = time_text.get_rect(center=(window_size[0] // 2, window_size[1] // 2))
    window.blit(time_text, text_rect)

    # Update the display
    pygame.display.flip()

    # Check if the time limit has been reached
    if time_remaining <= 0:
        break

    # Limit the frame rate
    clock.tick(60)

# Display "Time's up!" after the timer ends
time_up_text = font.render("Time's up!", True, BLACK)
time_up_rect = time_up_text.get_rect(center=(window_size[0] // 2, window_size[1] // 2))
window.fill(WHITE)
window.blit(time_up_text, time_up_rect)
pygame.display.flip()

# Wait for a few seconds before quitting
pygame.time.wait(3000)

# Quit Pygame
pygame.quit()
