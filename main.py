import pygame 
import sys
from settings import *

pygame.init()



class Game:
    def __init__(self):
        self.running = True 
        
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption(WINDOW_NAME)
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
 
            self.screen.fill('black')
            # self.level.run() #
            pygame.display.update()
            self.clock.tick(FPS)



if __name__ == '__main__':
    game = Game()
    game.run()