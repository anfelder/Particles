import pygame


class Particle:

    xpos = None
    ypos = None

    def __init__(self, surface, posx=350, posy=350, color=(255, 255, 255)):
        self.view = pygame.draw.circle(surface, color, (posx, posy), 5, 0)
        self.xpos = posx
        self.ypos = posy
        pygame.display.update()
