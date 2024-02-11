import pygame
import renderResources as res
import time
import os

WHITE = (255, 255, 255)
ZEROPOSITION = 0, 0
DISPLAYX = 1280
DISPLAYY = 720
GROUNDSIZE = 128
FPS = 200
TARGETFPS = 60

pygame.init()
screen = pygame.display.set_mode((DISPLAYX, DISPLAYY))
clock = pygame.time.Clock()

font = pygame.font.Font(os.path.join("simpleGame/assets", "Minecraft.ttf"), 24)

def fpsCounter():
    fps = str(int(clock.get_fps()))
    fps_t = font.render(fps , 1, WHITE)
    screen.blit(fps_t,(5, 5))

def drawBackground(MOVE1, MOVE2, MOVE3, MOVE4, MOVE5):
    #first
    screen.blit(res.plx1, (MOVE1, 0))
    screen.blit(res.plx1, (DISPLAYX + MOVE1, 0))
    #second
    screen.blit(res.plx2, (MOVE2, 0))
    screen.blit(res.plx2, (DISPLAYX + MOVE2, 0))
    #third
    screen.blit(res.plx3, (MOVE3, 0))
    screen.blit(res.plx3, (DISPLAYX + MOVE3, 0))
    #fourth
    screen.blit(res.plx4, (MOVE4, 0))
    screen.blit(res.plx4, (DISPLAYX + MOVE4, 0))
    #fifth
    screen.blit(res.plx5, (MOVE5, 0))
    screen.blit(res.plx5, (DISPLAYX + MOVE5, 0))
    #ground
    screen.blit(res.ground, ((0 + MOVE5, DISPLAYY - GROUNDSIZE)))
    screen.blit(res.ground, ((DISPLAYX + MOVE5, DISPLAYY - GROUNDSIZE)))

def main():
    prevTime = 0
    MOVE1 = 0
    MOVE2 = 0
    MOVE3 = 0
    MOVE4 = 0
    MOVE5 = 0
    running = True
    while running:
        clock.tick(FPS)
        now = time.time()
        dt = now - prevTime
        prevTime = now
        drawBackground(MOVE1, MOVE2, MOVE3, MOVE4, MOVE5)
        fpsCounter()
        MOVE1 -= 1 * dt * TARGETFPS
        MOVE2 -= 2 * dt * TARGETFPS
        MOVE3 -= 3 * dt * TARGETFPS
        MOVE4 -= 4 * dt * TARGETFPS
        MOVE5 -= 5 * dt * TARGETFPS
        if MOVE1 < -1280:
            MOVE1 = 0
        if MOVE2 < -1280:
            MOVE2 = 0
        if MOVE3 < -1280:
            MOVE3 = 0
        if MOVE4 < -1280:
            MOVE4 = 0
        if MOVE5 < -1280:
            MOVE5 = 0
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

main()
pygame.quit()
