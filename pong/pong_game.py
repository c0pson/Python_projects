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
        if self.pos_y == HEIGHT - self.height and direction == 1:
            direction = 0
        if self.pos_y == 0 and direction == -1:
            direction = 0
        self.pos_y = self.pos_y + self.speed * direction
        self.player_rect = (self.pos_x, self.pos_y, self.width, self.height)

class Ball:
    def __init__(self, pos_x, pos_y, size, speed, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size = size
        self.speed = speed
        self.color = color

        self.move_x = 1
        self.move_y = 1

    def display(self):
        if self.pos_y == HEIGHT - self.size:
            self.move_y = -1
        if self.pos_y == 0 + self.size:
            self.move_y = 1
        if self.pos_x == WIDTH - self.size:
            self.move_x = -1
        if self.pos_x == 0 + self.size:
            self.move_x = 1 # there will be points system

    def hit(self):
        ...

        self.ball = pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.size)

    def move(self):
        self.pos_x = self.pos_x + self.move_x * self.speed
        self.pos_y = self.pos_y + self.move_y * self.speed


def main():
    running = True
    player_1 = Player(20, HEIGHT // 2 - 100, 20, 100, 10, 'green')
    player_2 = Player(WIDTH - 40, HEIGHT // 2 - 100, 20, 100, 10, 'red')
    ball = Ball(WIDTH//2-20, HEIGHT//2-20, 20, 10, 'blue')
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
    # not intuitive - to change
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_2_direction = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player_1_direction = 0

        player_1.update(player_1_direction)
        player_2.update(player_2_direction)
        ball.move()

        player_1.display()
        player_2.display()
        ball.display()

        clock.tick(FPS)
        pygame.display.update()

if __name__ == "__main__":
    main()
