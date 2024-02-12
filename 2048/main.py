from copy import deepcopy
from os import system
import random

def print_board(board):
    system('cls')
    # for line in board:
    #     print(' '.join(map(str, line)))

    for line in board:
        print(' '.join("{:<4}".format(word) for word in line))

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
            return user_input

def connect_up(board):
    for i in range(3):
        for j in range(4):
            if board[i][j] == board[i + 1][j]:
                board[i][j] = int(board[i][j]) * 2
                board[i + 1][j] = 0

def connect_left(board):
    for j in range(3):
        for i in range(4):
            if board[i][j] == board[i][j + 1]:
                board[i][j] = int(board[i][j]) * 2
                board[i][j + 1] = 0

def connect_down(board):
    for i in range(2, -1, -1):
        for j in range(4):
            if board[i + 1][j] == board[i][j]:
                board[i + 1][j] = int(board[i + 1][j]) * 2
                board[i][j] = 0

def connect_right(board):
    for j in range(2, -1, -1):
        for i in range(4):
            if board[i][j] == board[i][j + 1]:
                board[i][j + 1] = int(board[i][j + 1]) * 2 
                board[i][j] = 0

def up(board):
    for i in range(4):
        for _ in range(4):
            if board[0][i] == 0:
                for j in range(3):
                    board[j][i] = board[j + 1][i]
                board[3][i] = 0
            if board[1][i] == 0:
                for j in range(1, 3):
                    board[j][i] = board[j + 1][i]
                board[3][i] = 0
            if board[2][i] == 0:
                board[2][i] = board[3][i]
                board[3][i] = 0
            

def left(board):
    for j in range(4):
        for _ in range(4):
            if board[j][0] == 0:
                for i in range(3):
                    board[j][i] = board[j][i + 1]
                board[j][3] = 0
            if board[j][1] == 0:
                for i in range(1, 3):
                    board[j][i] = board[j][i + 1]
                board[j][3] = 0
            if board[j][2] == 0:
                board[j][2] = board[j][3]
                board[j][3] = 0

def down(board):
    for i in range(4):
        for _ in range(4):
            if board[3][i] == 0:
                for j in range(3, 0, -1):
                    board[j][i] = board[j - 1][i]
                board[0][i] = 0
            if board[2][i] == 0:
                for j in range(2, 0, -1):
                    board[j][i] = board[j - 1][i]
                board[0][i] = 0
            if board[2][i] == 0:
                board[1][i] = board[0][i]
                board[0][i] = 0

def right(board):
    for j in range(4):
        for _ in range(4):
            if board[j][3] == 0:
                for i in range(3, 0, -1):
                    board[j][i] = board[j][i - 1]
                board[j][0] = 0
            if board[j][2] == 0:
                for i in range(2, 0, -1):
                    board[j][i] = board[j][i - 1]
                board[j][0] = 0
            if board[j][1] == 0:
                board[j][1] = board[j][0]
                board[j][0] = 0

def game_root(board, user_input):
    copy_of_board = deepcopy(board)
    copy_of_board_2 = deepcopy(board)
    if user_input == 'w':
        up(copy_of_board)
        connect_up(copy_of_board_2)
        if copy_of_board == board and copy_of_board_2 == board:
            print("This move is illegal")
            return
        up(board)
        connect_up(board)
        up(board)
    if user_input == 'a':
        left(copy_of_board)
        connect_left(copy_of_board_2)
        if copy_of_board == board and copy_of_board_2 == board:
            print("This move is illegal")
            return
        left(board)
        connect_left(board)
        left(board)
    if user_input == 's':
        down(copy_of_board)
        connect_down(copy_of_board_2)
        if copy_of_board == board and copy_of_board_2 == board:
            print("This move is illegal")
            return
        down(board)
        connect_down(board)
        down(board)
    if user_input == 'd':
        right(copy_of_board)
        connect_right(copy_of_board_2)
        if copy_of_board == board and copy_of_board_2 == board:
            print("This move is illegal")
            return
        right(board)
        connect_right(board)
        right(board)
    append_board(board)
    check_win(board)
    print_board(board)

def check_win(board):
    counter = 0
    if 2048 in board:
        exit('U have won!!!')
    else:
        copy_1 = deepcopy(board)
        copy_2 = deepcopy(board)
        up(copy_1)
        connect_up(copy_2)
        if copy_1 != board or copy_2 != board:
            counter += 1
        copy_1 = deepcopy(board)
        copy_2 = deepcopy(board)
        left(copy_1)
        connect_left(copy_2)
        if copy_1 != board or copy_2 != board:
            counter += 1
        copy_1 = deepcopy(board)
        copy_2 = deepcopy(board)
        down(copy_1)
        connect_down(copy_2)
        if copy_1 != board or copy_2 != board:
            counter += 1
        copy_1 = deepcopy(board)
        copy_2 = deepcopy(board)
        right(copy_1)
        connect_right(copy_2)
        if copy_1 != board or copy_2 != board:
            counter += 1
        if counter < 1:
            print_board(board)
            exit('Game over')

def append_board(board):
    elements_to_choose = [2, 2, 2, 2, 2, 2, 2, 2, 4]
    correct = False
    while not correct:
        x = random.randrange(0, 4)
        y = random.randrange(0, 4)
        if board[x][y] == 0:
            board[x][y] = random.choice(elements_to_choose)
            correct = True

def main():
    board = starting_board()
    while True:
        game_root(board, move())

if __name__ == "__main__":
    main()
