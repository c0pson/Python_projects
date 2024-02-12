import pygame

def game_logic():
    ...

def main():
    SCREEN_SIZE = (1280, 720)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE))
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('white')
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

main()
