import pygame
import time
import math

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Display dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Exam Clock")

# Clock variables
clock_radius = 200
clock_center = (WIDTH // 2, HEIGHT // 2)
hour_hand_length = clock_radius * 0.5
minute_hand_length = clock_radius * 0.7
second_hand_length = clock_radius * 0.9
clock_font = pygame.font.SysFont(None, 64)
countdown_time = 300  # 5 minutes in seconds
start_time = 0
is_paused = False

# Function to convert degrees to radians
def degrees_to_radians(degrees):
    return degrees * math.pi / 180

# Function to calculate the endpoint of a line
def calculate_endpoint(center, length, angle):
    x = center[0] + length * math.cos(angle)
    y = center[1] - length * math.sin(angle)
    return int(x), int(y)

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_paused = not is_paused

    # Clear the screen
    SCREEN.fill(WHITE)

    # Countdown timer logic
    current_time = time.time()
    if not is_paused:
        if not start_time:
            start_time = current_time
        elapsed_time = current_time - start_time
        remaining_time = countdown_time - elapsed_time
        if remaining_time <= 0:
            # Time's up, do something (e.g., play a sound, show a message)
            print("Time's up!")
        else:
            # Calculate the angles for the clock hands
            total_seconds = remaining_time % 60
            total_minutes = (remaining_time // 60) % 60
            total_hours = (remaining_time // 3600) % 12
            second_angle = degrees_to_radians(total_seconds * 6)  # 360 degrees in 60 seconds
            minute_angle = degrees_to_radians(total_minutes * 6)  # 360 degrees in 60 minutes
            hour_angle = degrees_to_radians((total_hours * 30) + (total_minutes * 0.5))  # 360 degrees in 12 hours

            # Draw clock hands
            hour_hand_end = calculate_endpoint(clock_center, hour_hand_length, hour_angle)
            minute_hand_end = calculate_endpoint(clock_center, minute_hand_length, minute_angle)
            second_hand_end = calculate_endpoint(clock_center, second_hand_length, second_angle)
            pygame.draw.line(SCREEN, BLACK, clock_center, hour_hand_end, 8)
            pygame.draw.line(SCREEN, BLACK, clock_center, minute_hand_end, 4)
            pygame.draw.line(SCREEN, RED, clock_center, second_hand_end, 2)
    else:
        if start_time:
            elapsed_time = current_time - start_time
            start_time += elapsed_time

    # Update the display
    pygame.display.flip()

# Quit the application
pygame.quit()
