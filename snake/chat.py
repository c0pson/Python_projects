import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the clock to control the frame rate
clock = pygame.time.Clock()

# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((width // 2), (height // 2))]
        self.direction = random.choice([(0, -10), (0, 10), (-10, 0), (10, 0)])
        self.color = (0, 255, 0)  # Green

    def move(self):
        cur = self.positions[0]
        x, y = self.direction
        new = (((cur[0] + x) % width), (cur[1] + y) % height)
        self.positions = [new] + self.positions[:-1]

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.direction = (0, -10)
                elif event.key == pygame.K_DOWN:
                    self.direction = (0, 10)
                elif event.key == pygame.K_LEFT:
                    self.direction = (-10, 0)
                elif event.key == pygame.K_RIGHT:
                    self.direction = (10, 0)

# Main function
def main():
    snake = Snake()

    while True:
        snake.handle_keys()
        snake.move()

        # Draw the screen
        screen.fill(black)
        for position in snake.positions:
            pygame.draw.rect(screen, snake.color, (position[0], position[1], 10, 10))

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(10)  # You can adjust the frame rate as needed

if __name__ == "__main__":
    main()
