import pygame 

class Clock:
    def __init__(self, time):
        # in millisecond 
        self.time_limit = time
        self.time_remaining = time*1000
        self.start_time = pygame.time.get_ticks()

    def tick(self):
        elapsed_time = pygame.time.get_ticks() -self.start_time
        time_remaining = max(self.time_limit * 1000 - elapsed_time, 0)