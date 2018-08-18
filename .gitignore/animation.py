import pygame, sys
from pygame.locals import *

pygame.init()


FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAY = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Cat game')
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
white = (255, 255, 255)


while True: # the main game loop
    DISPLAY.fill(white)
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_RIGHT:
            catx += 10
        elif event.type == KEYDOWN and event.key == K_LEFT:
            catx -= 10
        elif event.type == KEYDOWN and event.key == K_UP:
            caty -= 10
        elif event.type == KEYDOWN and event.key == K_DOWN:
            caty += 10
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
        DISPLAY.blit(catImg, (catx, caty))
        pygame.display.update()
        fpsClock.tick(FPS)
    
        

