import pygame 


class Mode:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

    def run(self):
        #update and draw the game 
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
