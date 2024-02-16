import pygame

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 30

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

    def update(self, direction):
        self.pos_y = self.pos_y + self.speed * direction
        self.player_rect = (self.pos_x, self.pos_y, self.width, self.height)

class Ball:
    ...

def main():
    running = True
    player_1 = Player(20, HEIGHT//2-100, 20, 100, 10, 'green')
    player_2 = Player(WIDTH - 40, HEIGHT//2-100, 20, 100, 10, 'red')
    player_1_direction = 0
    player_2_direction = 0
    while running:
        screen.fill('gray')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_2_direction = -1
                if event.key == pygame.K_DOWN:
                    player_2_direction = 1
                if event.key == pygame.K_w:
                    player_1_direction = -1
                if event.key == pygame.K_s:
                    player_1_direction = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_2_direction = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player_1_direction = 0

        player_1.update(player_1_direction)
        player_2.update(player_2_direction)

        player_1.display()
        player_2.display()

        clock.tick(FPS)
        pygame.display.update()
main()
