import pygame

pygame.init()
RESOLUTION = (720, 720)
screen = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()
running = True
FPS = 60
dt = 0
white = (255, 255, 255)

PIXEL = 45

pos_x = 75
pos_y = 74

def draw_snake():
    global pos_x, pos_y

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_w]:
        pos_y -= PIXEL
    if keys[pygame.K_s]:
        pos_y += PIXEL
    if keys[pygame.K_a]:
        pos_x -= PIXEL
    if keys[pygame.K_d]:
        pos_x += PIXEL
    pygame.draw.rect(screen, white, (pos_x, pos_y, PIXEL, PIXEL))

def draw_food():
    ...

def check_colision():
    ...

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    draw_snake()
    pygame.display.flip()
    clock.tick(FPS)
    dt = clock.tick(FPS)/1000
pygame.quit()
