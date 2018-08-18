import pygame, sys
from pygame.locals import *
from time import sleep


pygame.init()


FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAY = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Cat game')
black = pygame.image.load('black.png')
blackx = 10
blacky = 10
fond = pygame.image.load("back.png")
fond = pygame.transform.scale(fond, (640, 480))
telep1 = pygame.image.load("telep1.png")
telep2 = pygame.image.load("telep2.png")
telep3 = pygame.image.load("telep3.png")
telep4 = pygame.image.load("telep4.png")




while True: # the main game loop
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_RIGHT:
            blackx += 10
        elif event.type == KEYDOWN and event.key == K_LEFT:
            blackx -= 10
        elif event.type == KEYDOWN and event.key == K_UP:
            blacky -= 10
        elif event.type == KEYDOWN and event.key == K_DOWN:
            blacky += 10
        elif event.type == KEYDOWN and event.key == K_SPACE:
            black = telep1
            DISPLAY.blit(black, (blackx, blacky))
            pygame.display.update()
            fpsClock.tick(FPS)
            sleep(1)
            black = telep2
            DISPLAY.blit(black, (blackx, blacky))
            pygame.display.update()
            fpsClock.tick(FPS)
            pygame.mixer.music.load('it.mp3')
            pygame.mixer.music.play(0)
            black = telep3
            DISPLAY.blit(black, (blackx, blacky))
            pygame.display.update()
            fpsClock.tick(FPS)
            black = telep4
            DISPLAY.blit(black, (blackx, blacky))
            pygame.display.update()
            fpsClock.tick(FPS)
            blackx += 100
            DISPLAY.blit(black, (blackx, blacky))
            pygame.display.update()
            fpsClock.tick(FPS)
            black = pygame.image.load('black.png')
            DISPLAY.blit(black, (blackx, blacky))
            pygame.display.update()
            fpsClock.tick(FPS)
            
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
        DISPLAY.blit(fond, (0, 0))
        DISPLAY.blit(black, (blackx, blacky))
        pygame.display.update()
        fpsClock.tick(FPS)
    
        

