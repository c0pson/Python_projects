import pygame

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont('Brittanic', 60)
clock = pygame.time.Clock()
FPS = 60
PLAYER_COLOR = (38, 80, 115)
BALL_COLOR = (45, 149, 150)
BACKGROUND_COLOR = (154, 208, 194)

class Projectiles:
    # maybe i'll be able to make projectile following the ball 
    amount = 0
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        Projectiles.amount += 1

    def draw_projectile_following_ball(self):
        ...

class Player:
    def __init__(self, pos_x, pos_y, width, height, speed, color, points):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.points = points

        self.player_rect = pygame.Rect(pos_x, pos_y, width, height)
        self.player = pygame.draw.rect(screen, self.color, self.player_rect)

    def display(self):
        self.player = pygame.draw.rect(screen, self.color, self.player_rect)
        score_text = font.render(str(self.points), False, (0,0,0))
        if self.pos_x > WIDTH // 2:
            screen.blit(score_text, (3 * (WIDTH // 4), HEIGHT - 60))
        else:
            screen.blit(score_text, (WIDTH // 4 - 60, HEIGHT - 60))

    def update(self, direction):
        if self.pos_y == HEIGHT - self.height and direction == 1:
            direction = 0
        if self.pos_y == 0 and direction == -1:
            direction = 0
        self.pos_y = self.pos_y + self.speed * direction
        self.player_rect = (self.pos_x, self.pos_y, self.width, self.height)

    def get_coords(self):
        return self.pos_x, self.pos_y
    
    def score(self):
        self.points += 1
        self.pos_y = HEIGHT // 2 - 100

    def reset_position(self, x, y):
        self.pos_x = x
        self.pos_y = y

class Ball:
    def __init__(self, pos_x, pos_y, size, speed, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size = size
        self.speed = speed
        self.color = color
        self.move_x = -1
        self.move_y = -1

    def display(self):
        if self.pos_y >= HEIGHT - self.size:
            self.move_y = -1
        if self.pos_y <= 0 + self.size:
            self.move_y = 1
        self.ball = pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.size)

    def hit(self):
        self.move_x = self.move_x * -1

    def move(self):
        self.pos_x = self.pos_x + self.move_x * self.speed
        self.pos_y = self.pos_y + self.move_y * self.speed

    def get_coords(self):
        return self.pos_x, self.pos_y

    def reset_position(self):
        self.pos_y = HEIGHT // 2 - self.size
        self.pos_x = WIDTH // 2 - self.size

def main():
    running = True
    player_1 = Player(20, HEIGHT // 2 - 100, 20, 100, 5, PLAYER_COLOR, 0)
    player_2 = Player(WIDTH - 40, HEIGHT // 2 - 100, 20, 100, 5, PLAYER_COLOR, 0)
    ball = Ball(WIDTH//2-20, HEIGHT//2-20, 20, 5, BALL_COLOR)
    player_1_direction = 0
    player_2_direction = 0
    counter = 0
    while running:
        screen.fill(BACKGROUND_COLOR)
        separator_rect = pygame.Rect(WIDTH // 2 - 2, 0, 4, HEIGHT)
        pygame.draw.rect(screen, "black", separator_rect)
        for i in range(HEIGHT // 20):
            separator_rect_2 = pygame.Rect(WIDTH // 2 - 2, (i * (HEIGHT // 10)) - (HEIGHT // 40), 4, HEIGHT // 20)
            pygame.draw.rect(screen, BACKGROUND_COLOR, separator_rect_2)
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
        # update position
        player_1.update(player_1_direction)
        player_2.update(player_2_direction)
        ball.move()
        # update coords
        player_1_x, player_1_y = player_1.get_coords()
        player_2_x, player_2_y = player_2.get_coords()
        ball_x, ball_y = ball.get_coords()
        #collision check
        if ball_x == player_1_x + 40 and ball_y >= player_1_y and ball_y <= player_1_y + 120:
            ball.hit()
        if ball_x == player_2_x - 20 and ball_y >= player_2_y and ball_y <= player_2_y + 120:
            ball.hit()
        # points system
        if ball_x >= WIDTH - 10:
            player_1.reset_position(20, HEIGHT // 2 - 100)
            player_2.reset_position(WIDTH - 40, HEIGHT // 2 - 100)
            ball.reset_position()
            player_2.score()
            counter += 1
        if ball_x <= 10:
            player_1.reset_position(20, HEIGHT // 2 - 100)
            player_2.reset_position(WIDTH - 40, HEIGHT // 2 - 100)
            ball.reset_position()
            player_1.score()
            counter += 1
        player_1.display()
        player_2.display()
        ball.display()
        clock.tick(FPS)
        pygame.display.update()

if __name__ == "__main__":
    main()

