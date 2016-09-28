import pygame
import Particle
import time
import math


class Game:

    particleList = list()

    def __init__(self):
        self.screen = pygame.display.set_mode((700, 700))
        self.screen.fill((0, 0, 0))
        self.running = True
        self.run()

    def drawParticle(self):
        color = (255, 255, 255)
        # posx, posy = pygame.mouse.get_pos()
        posx, posy = 350, 350
        pygame.draw.circle(self.screen, color, (posx, posy), 10)
        pygame.display.update()

    def updateSpeed(self, partCoords, mousex, mousey, speedList):

        speed = .3
        if len(partCoords) == 0 and len(speedList) == 0:
            for particle in self.particleList:
                partCoords.append((particle.xpos, particle.ypos))

                dx = mousex - particle.xpos
                dy = mousey - particle.ypos
                dz = math.sqrt(dx**2 + dy**2)

                speedx = dx/dz * speed
                speedy = dy/dz * speed

                # if speedx > 0:
                #     speedx += .05
                # else:
                #     speedx -= .05
                #
                # if speedy > 0:
                #     speedy += .05
                # else:
                #     speedy -= .05

                speedList.append((speedx, speedy))
        else:
            for index, speed in enumerate(speedList):
                tempsx = speed[0]
                tempsy = speed[1]
                if tempsx > 0:
                    tempsx += .002
                else:
                    tempsx -= .002

                if tempsy > 0:
                    tempsy += .002
                else:
                    tempsy -= .002
                speedList[index] = (tempsx, tempsy)

    def followMouse(self):
        mousex, mousey = pygame.mouse.get_pos()
        partCoords = list()
        speedList = list()
        numPartsAtPoint = -1

        while numPartsAtPoint != len(partCoords):
            self.updateSpeed(partCoords, mousex, mousey, speedList)
            numPartsAtPoint = 0
            self.screen.fill((0, 0, 0))
            for index, (particle, speed) in enumerate(zip(partCoords, speedList)):
                tempx = particle[0]
                tempy = particle[1]

                if mousex != int(particle[0]):
                    tempx += speed[0]
                if mousey != int(particle[1]):
                    tempy += speed[1]

                Particle.Particle(self.screen, int(tempx), int(tempy))
                temptuple = (tempx, tempy)
                partCoords[index] = temptuple
                self.particleList[index].xpos = tempx
                self.particleList[index].ypos = tempy

                if abs(mousex - tempx) < 1 and abs(mousey - tempy) < 1:
                    numPartsAtPoint += 1
            pygame.display.update()

        print "finished"

    def run(self):
        clock = pygame.time.Clock()
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 50)
        # Particle.Particle(self.screen)
        self.particleList.append(Particle.Particle(self.screen))
        self.particleList.append(Particle.Particle(self.screen, 400, 400))
        self.particleList.append(Particle.Particle(self.screen, 100, 250))
        self.particleList.append(Particle.Particle(self.screen, 73, 153))
        self.particleList.append(Particle.Particle(self.screen, 500, 423))

        while self.running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.followMouse()
                    # Particle.Particle(self.screen)
        print len(self.particleList)
        pygame.display.quit()
        pygame.quit()

