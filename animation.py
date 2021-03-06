import pygame, sys
from pygame.locals import *
from time import sleep

from model.Grid import Grid
from model.Fighter import Fighter
from model.Archer import Archer
from model.Skill import Skill
from controller.ControlEntity import ControlEntity

pygame.init()


FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAY = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Cat game')
black = pygame.image.load('sprites/black.png')
blackx = 10
blacky = 10
fond = pygame.image.load("sprites/back.png")
fond = pygame.transform.scale(fond, (640, 480))
telep1 = pygame.image.load("sprites/telep1.png")
telep2 = pygame.image.load("sprites/telep2.png")
telep3 = pygame.image.load("sprites/telep3.png")
telep4 = pygame.image.load("sprites/telep4.png")
kame1 = pygame.image.load("sprites/kame1.png") 
kame2 = pygame.image.load("sprites/kame2.png")
kame3 = pygame.image.load("sprites/kame3.png")
kame4 = pygame.image.load("sprites/kame4.png")
kame5 = pygame.image.load("sprites/kame5.png")
pygame.key.set_repeat(100)

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
            pygame.mixer.music.load('sprites/it.mp3')
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
            black = pygame.image.load('sprites/black.png')
            DISPLAY.blit(black, (blackx, blacky))
            pygame.display.update()
            fpsClock.tick(FPS)
        elif event.type == KEYDOWN and event.key == K_k:
            pygame.mixer.music.load('sprites/kamesound.mp3')
            pygame.mixer.music.play(0)
            black = kame1
            DISPLAY.blit(black, (blackx, blacky))
            pygame.display.update()
            fpsClock.tick(FPS)
            sleep(2)
            black = kame2
            DISPLAY.blit(black, (blackx, blacky))
            pygame.display.update()
            fpsClock.tick(FPS)
            sleep(3)
            black = kame3
            DISPLAY.blit(black, (blackx, blacky))
            pygame.display.update()
            fpsClock.tick(FPS)
            sleep(2)
            DISPLAY.blit(black, (blackx, blacky))
            pygame.display.update()
            fpsClock.tick(FPS)
            black = kame4
            DISPLAY.blit(black, (blackx, blacky))
            pygame.display.update()
            fpsClock.tick(FPS)
            fond.blit(kame5, (120,20))
            pygame.display.update()
            fond.blit(kame5, (120,20))
            pygame.display.update()
            
            
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
        DISPLAY.blit(fond, (0, 0))
        DISPLAY.blit(black, (blackx, blacky))
        pygame.display.update()
        fpsClock.tick(FPS)
