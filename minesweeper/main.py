import random
import time
import copy
import os

def choose_difficulty():
    is_int = False
    while not is_int:
        size = input("Choose size of an board: ")
        try:
            size = int(size)
            if size < 40 and size > 3:
                is_int = True
            else:
                print("Provide only integer number")
        except ValueError:
            print("Provide only integer number")
    return size

def  print_starting_board(size):
    starting_board = [['X'] * size for _ in range(size)]
    print_board(starting_board)

def print_end_board(board):
    board_to_print = copy.deepcopy(board)
    for i in range(len(board_to_print)):
        for j in range(len(board_to_print[0])):
            if board_to_print[i][j] == 'X':
                board_to_print[i][j] = '\u25A0'
            if board_to_print[i][j] == 'B':
                board_to_print[i][j] = '\u25CB'
            if board_to_print[i][j] == 'M':
                board_to_print[i][j] = '\u2691'
            if board_to_print[i][j] == 'm':
                board_to_print[i][j] = '\u22BB'
    os.system('cls')
    max_row_width = len(str(len(board_to_print)))  
    row_numbers = ''
    for i in range(1, len(board_to_print[0]) + 1):
        row_numbers += f"{i:2d}"
        if i < len(board_to_print[0]):
            row_numbers += " "
    print(f' \U0001F4A3 |{row_numbers}' + ' |')
    horizontal_line = '----+' + '-' * len(row_numbers) + '-+'
    print(horizontal_line)
    for i, row in enumerate(board_to_print, start=1):
        row_str = f" {i:>{max_row_width}} | {'  '.join(row)} |"
        print(row_str)
    print(horizontal_line)

def print_board(board):
    board_to_print = copy.deepcopy(board)
    for i in range(len(board_to_print)):
        for j in range(len(board_to_print[0])):
            if board_to_print[i][j] == 'B':
                board_to_print[i][j] = 'X'
            if board_to_print[i][j] == 'X':
                board_to_print[i][j] = '\u25A0'
            if board_to_print[i][j] == 'm' or board_to_print[i][j] == 'M':
                board_to_print[i][j] = '\u2691'
    os.system('cls')
    os.system('cls')
    max_row_width = len(str(len(board_to_print)))  
    row_numbers = ''
    for i in range(1, len(board_to_print[0]) + 1):
        row_numbers += f"{i:2d}"
        if i < len(board_to_print[0]):
            row_numbers += " "
    print(f' \U0001F4A3 |{row_numbers}' + ' |')
    horizontal_line = '----+' + '-' * len(row_numbers) + '-+'
    print(horizontal_line)
    if len(board) > 9:
        for i, row in enumerate(board_to_print, start=1):
            row_str = f" {i:>{max_row_width}} | {'  '.join(row)} |"
            print(row_str)
    else:
        for i, row in enumerate(board_to_print, start=1):
            row_str = f"  {i:>{max_row_width}} | {'  '.join(row)} |"
            print(row_str)
    print(horizontal_line)

def create_board(size, x_cord, y_cord):
    num_bombs = size
    board = [['X'] * size for _ in range(size)]
    bombs_placed = 0
    while bombs_placed < num_bombs:
        x = random.randrange(0, len(board))
        y = random.randrange(0, len(board[0]))
        if (x, y) != (x_cord - 1, y_cord - 1) and board[x][y] != 'B':
            board[x][y] = 'B'
            bombs_placed += 1
        bombs_placed -= remove_bombs_nearby(board, x_cord - 1, y_cord - 1)
    return board

def remove_bombs_nearby(board, x_cord, y_cord):
    counter = 0
    for i in range(max(0, x_cord - 1), min(len(board), x_cord + 2)):
        for j in range(max(0, y_cord - 1), min(len(board[0]), y_cord + 2)):
            if board[i][j] == 'B':
                board[i][j] = 'X'
                counter += 1
    return counter

def choose_mode(board, board_size):
    mods = ['Select area', 'Pin bombs']
    mode = input("Select mode (0: select area | 1: pin bombs): ")
    while mode != '0' and mode != '1':
        mode = input("Select mode (0: select area | 1: pin bombs): ")
    mode = int(mode)
    print(f'Selected mode is {mods[mode]}')
    if mode == 0:
        x_cord, y_cord = player_moves(board_size)
        check_for_bombs(board, x_cord, y_cord)
        print_board(board)
    else:
        x_cord, y_cord = player_moves(board_size)
        mark_bomb(board, x_cord, y_cord)
        print_board(board)

def player_moves(board_size):
    list_of_possible_options = [0] * board_size
    for i in range(board_size):
        list_of_possible_options[i] = str(i + 1)
    x_cord = input("Row: ")
    while x_cord not in list_of_possible_options:
        print(f'Invalid input, please provide number from 1 to {board_size}')
        x_cord = input("Row: ")
    x_cord = int(x_cord)
    y_cord = input("Column: ")
    while y_cord not in list_of_possible_options:
        print(f'Invalid input, please provide number from 1 to {board_size}')
        y_cord = input("Column: ")
    y_cord = int(y_cord)
    return x_cord, y_cord

def mark_bomb(board, x_cord, y_cord):
    if board[x_cord - 1][y_cord - 1] == 'B':
        board[x_cord - 1][y_cord - 1] = 'M'
    elif board[x_cord - 1][x_cord - 1] == 'X':
        board[x_cord - 1][y_cord - 1] = 'm'
    else:
        print('U cant mark bomb in here!')
        time.sleep(1)

def check_for_bombs(board, x_cord, y_cord):
    if board[x_cord - 1][y_cord - 1] == 'B' or board[x_cord - 1][y_cord - 1] == 'M':
        board[x_cord - 1][y_cord - 1] = '\u25CB'
        print_end_board(board)
        exit('Game Over')
    else:
        search_around(board, x_cord - 1, y_cord -  1)

def search_around(board, x_cord, y_cord):
    counter = 0
    for i in range(max(0, x_cord - 1), min(len(board), x_cord + 2)):
        for j in range(max(0, y_cord - 1), min(len(board[0]), y_cord + 2)):
            if board[i][j] == 'B' or board[i][j] == 'M':
                counter += 1
    if counter > 0:
        board[x_cord][y_cord] = str(counter)
    else:
        board[x_cord][y_cord] = '\u25A1' 
        for i in range(max(0, x_cord - 1), min(len(board), x_cord + 2)):
            for j in range(max(0, y_cord - 1), min(len(board[0]), y_cord + 2)):
                if board[i][j] == 'X' or board[i][j] == 'm':
                    search_around(board, i, j)

def check_win(board, board_size):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'B':
                return False
    return True

def end_game(board, board_size, score_max):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'm':
                score_max = score_max - (score_max // (board_size * board_size))
    if check_win(board, board_size):
        print_end_board(board)
        exit(f'U won with score {score_max}')
    return score_max

def main():
    board_size = choose_difficulty()
    score_max = 999
    print_starting_board(board_size)
    x_cord, y_cord = player_moves(board_size)
    board = create_board(board_size, x_cord, y_cord)
    check_for_bombs(board, x_cord, y_cord)
    print_board(board)
    while True:
        choose_mode(board, board_size)
        score_max = end_game(board, board_size, score_max)

if __name__ == "__main__":
    main()
