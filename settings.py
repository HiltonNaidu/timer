import pygame
import sys 
import utility 
pygame.init()

#settings 
screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h

# clock settings 
FPS = 60

# window name 
WINDOW_NAME = "Timer Program"

# getting operating system 
systems = {
    "darwin": "macos",
    "win32": "windows",
    "linux" and "linux2": "linux"
}
OS = systems[sys.platform]


# getting darnk mode settings 
if utility.check_appearance():
    COLOUR_MODE = "dark"
else:
    COLOUR_MODE = "light"

