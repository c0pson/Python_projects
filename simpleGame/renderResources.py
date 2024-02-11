import pygame
import os

DISPLAYX = 1280
DISPLAYY = 720
GROUNDSIZE = 128

pygame.init()
pygame.display.set_mode((DISPLAYX, DISPLAYY))
pygame.image.get_extended()

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

#mage

mage1 = pygame.image.load(os.path.join("simpleGame/assets/mage", "1.png")).convert_alpha()
mage2 = pygame.image.load(os.path.join("simpleGame/assets/mage", "2.png")).convert_alpha()
mage3 = pygame.image.load(os.path.join("simpleGame/assets/mage", "3.png")).convert_alpha()
mage4 = pygame.image.load(os.path.join("simpleGame/assets/mage", "4.png")).convert_alpha()
mage5 = pygame.image.load(os.path.join("simpleGame/assets/mage", "5.png")).convert_alpha()
mage6 = pygame.image.load(os.path.join("simpleGame/assets/mage", "6.png")).convert_alpha()
mage7 = pygame.image.load(os.path.join("simpleGame/assets/mage", "7.png")).convert_alpha()
mage8 = pygame.image.load(os.path.join("simpleGame/assets/mage", "8.png")).convert_alpha()

mage1 = pygame.transform.scale(mage1, (112, 96))
mage2 = pygame.transform.scale(mage2, (112, 96))
mage3 = pygame.transform.scale(mage3, (112, 96))
mage4 = pygame.transform.scale(mage4, (112, 96))
mage5 = pygame.transform.scale(mage5, (112, 96))
mage6 = pygame.transform.scale(mage6, (112, 96))
mage7 = pygame.transform.scale(mage7, (112, 96))
mage8 = pygame.transform.scale(mage8, (112, 96))

gigMage = pygame.image.load(os.path.join("simpleGame/assets/", "mage.gif"))
