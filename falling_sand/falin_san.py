import pygame

# pygame screen

def print_matrix(matrix):
    for row in matrix:
        print(row)

def init_pygame():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))  # noqa: F841
    pygame.display.set_caption("Falling sand")
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


        screen.fill((96,96,96))

        pygame.display.flip()

# pygame screen
# =============
# matrix setup

def setup_matrix():
    matrix = [[0]*16 for _ in range(16)]
    for row in matrix:
        print(row)

    return matrix

# matrix setup
# ===============
# physics of sand

def falling_sand(matrix, column):
    flag = 0
    was_left = 0
    for i in range(len(matrix)):
        if matrix[-i-1][column] == 0:
            print(True)
            flag += 1
            if matrix[-i - 1][column - 1] == 0 and matrix[-i][column  - 1] == 0 and flag == 2 and was_left == 0:
                print('Falling to left')
                flag = 1
                was_left = 1

            elif  matrix[-i - 1][column + 1] == 0 and matrix[-i][column + 1] == 0 and flag == 2 and was_left == 1:
                print('Falling to right')
                flag = 0
                was_left = 0

            else:
                print('Not falling')
        else:
            print(False)
    
    print_matrix(matrix)

# physics of sand
# ===============

matrix = setup_matrix()
falling_sand(matrix, column=1)
init_pygame()
