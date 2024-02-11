import random

def print_board(board):
    for line in board:
        print(' '.join(map(str, line)))

def starting_board():
    board = [[0] * 4 for _ in range(4)]
    elements_to_choose = [2, 2, 2, 2, 2, 2, 2, 4]
    starting_element = random.choice(elements_to_choose)
    x_cord = random.randrange(4)
    y_cord = random.randrange(4)
    board[x_cord][y_cord] = int(starting_element)
    print_board(board)
    return board

def move():
    input_list = ['w','a','s','d']
    user_input = 'x'
    correct_input = False
    while not correct_input:
        if user_input not in input_list:
            user_input = input('Enter direction w(up), s(down), a(left), d(right): ')
        else:
            correct_input = True
            print(user_input)
            return user_input

def up(board):
    for i in range(4):
        for _ in range(4):
            if board[0][i] == 0:
                board[0][i] = board[1][i]
                board[1][i] = board[2][i]
                board[2][i] = board[3][i]
                board[3][i] = 0

def left(board):
    ...

def down(board):
    ...

def right(board):
    ...

def game_root(board, user_input):
    if user_input == 'w':
        up(board)
        print_board(board)
    if user_input == 'a':
        left(board)
    if user_input == 's':
        down(board)
    if user_input == 'd':
        right(board)

def main():
    board = starting_board()
    for _ in range(1):
        game_root(board, move())

main()
