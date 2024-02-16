import pygame

pygame.init()

SCREEN_SIZE = (1280, 720)
screen = pygame.display.set_mode(SCREEN_SIZE)


class Player:
    def __init__(self, pos_x, pos_y, width, height, speed, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

        self.player_rect = pygame.Rect(pos_x, pos_y, width, height)
        self.player = pygame.draw.rect(screen, self.color, self.player_rect)

    def display(self):
        self.player = pygame.draw.rect(screen, self.color, self.player_rect)

    def update(self):
        ...

class Ball:
    ...

def main():
    running = True

    player_1 = Player(20, 0, 10, 100, 10, 'green')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('gray')

        player_1.display()

        pygame.display.flip()

main()
