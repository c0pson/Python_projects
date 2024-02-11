import pygame
import os

#i will figure it out how to optimise it

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ZEROPOSITION = 0, 0
DISPLAYX = 1280
DISPLAYY = 720
GROUNDSIZE = 128
GROUNDSIZE = 64
MOVE = 0

pygame.init()
screen = pygame.display.set_mode((DISPLAYX, DISPLAYY))
clock = pygame.time.Clock()
running = True

font = pygame.font.Font(os.path.join("simpleGame/assets", "Minecraft.ttf"), 24)

plx1 = pygame.image.load(os.path.join("simpleGame/assets", "plx-1.png")).convert()
plx2 = pygame.image.load(os.path.join("simpleGame/assets", "plx-2.png")).convert_alpha()
plx3 = pygame.image.load(os.path.join("simpleGame/assets", "plx-3.png")).convert_alpha()
plx4 = pygame.image.load(os.path.join("simpleGame/assets", "plx-4.png")).convert_alpha()
plx5 = pygame.image.load(os.path.join("simpleGame/assets", "plx-5.png")).convert_alpha()
ground = pygame.image.load(os.path.join("simpleGame/assets", "ground.png")).convert_alpha()

plx1 = pygame.transform.scale(plx1, (DISPLAYX, DISPLAYY))
plx2 = pygame.transform.scale(plx2, (DISPLAYX, DISPLAYY))
plx3 = pygame.transform.scale(plx3, (DISPLAYX, DISPLAYY))
plx4 = pygame.transform.scale(plx4, (DISPLAYX, DISPLAYY))
plx5 = pygame.transform.scale(plx5, (DISPLAYX, DISPLAYY))
ground = pygame.transform.scale(ground, (DISPLAYX, GROUNDSIZE))

def drawBackground():
    #first
    screen.blit(plx1, (MOVE * 2, 0))
    screen.blit(plx1, (DISPLAYX + MOVE * 2, 0))
    #second
    screen.blit(plx2, (MOVE * 2, 0))
    screen.blit(plx2, (DISPLAYX + MOVE * 2, 0))
    #third
    screen.blit(plx3, (MOVE * 2, 0))
    screen.blit(plx3, (DISPLAYX + MOVE * 2, 0))
    #fourth
    screen.blit(plx4, (MOVE * 2, 0))
    screen.blit(plx4, (DISPLAYX + MOVE * 2, 0))
    #fifth
    screen.blit(plx5, (MOVE * 2, 0))
    screen.blit(plx5, (DISPLAYX + MOVE * 2, 0))
    #ground
    screen.blit(ground, ((0 + MOVE * 2, DISPLAYY - GROUNDSIZE)))
    screen.blit(ground, ((DISPLAYX + MOVE *2, DISPLAYY - GROUNDSIZE)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    drawBackground()
    MOVE -= 1
    if MOVE < - DISPLAYX / 2:
        MOVE = 0
    pygame.display.update()
    clock.tick(60)

pygame.quit()
