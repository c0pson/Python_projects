import os
import copy
import time

def check_input(main_check, row, col):
    try:
        row = int(row)
        col = int(row)
    except ValueError:
        print("Provide integer number:")
        return False


    if row not in [1, 2, 3] or col not in [1, 2, 3]:
        os.system('cls')
        print("Provide numbers 1, 2, or 3 for both row and column.")
        time.sleep(1)
        os.system('cls')
        print_check_board(main_check)
        return False
    return True

def print_check_board(check_board):

    copy_of_check_board = copy.deepcopy(check_board)

    for i in range(len(copy_of_check_board)):
        for j in range(len(copy_of_check_board[i])):
            if copy_of_check_board[i][j] == 1:
                copy_of_check_board[i][j] = 'X'
            elif copy_of_check_board[i][j] == 2:
                copy_of_check_board[i][j] = 'O'
            else:
                copy_of_check_board[i][j] = ' '

    os.system('cls')

    print(f'{copy_of_check_board[0][0]} | {copy_of_check_board[0][1]} | {copy_of_check_board[0][2]}\n==#===#==')
    print(f'{copy_of_check_board[1][0]} | {copy_of_check_board[1][1]} | {copy_of_check_board[1][2]}\n==#===#==')
    print(f'{copy_of_check_board[2][0]} | {copy_of_check_board[2][1]} | {copy_of_check_board[2][2]}')

def check_if_empty(main_check, row, col):
    if main_check[row - 1][col - 1] == 1 or main_check[row - 1][col - 1] == 2:
        os.system('cls')
        print_check_board(main_check)
        print("Provide not occupied box")
        return False
    else:
        return True

def Player1(main_check):
    playerX = 1
    row = int(input("Provide row: "))
    col = int(input("provide column: "))

    while not check_input(main_check, row, col):
        row = int(input("Provide row: "))
        col = int(input("provide column: "))

    while not check_if_empty(main_check, row, col):
        Player1(main_check)

    main_check[row - 1][col - 1] = playerX
    print_check_board(main_check)

    if not check_win(main_check):
        check_if_draw(main_check)
        return main_check

def Player2(main_check):
    playerO = 2
    row = int(input("Provide row: "))
    col = int(input("provide column: "))

    while not check_input(main_check, row, col):
        row = int(input("Provide row: "))
        col = int(input("provide column: "))

    while not check_if_empty(main_check, row, col):
        Player2(main_check)

    main_check[row - 1][col - 1] = playerO
    print_check_board(main_check)

    if not check_win(main_check):
        check_if_draw(main_check)
        return main_check

def check_win(main_check):
    playerX = 1
    playerO = 2

#win conditions for rows

    win_condition_for_X = [1, 1, 1] 
    win_condition_for_o = [2, 2, 2]

    for row in main_check:
        if row == win_condition_for_X:
            print("X win")
            exit()
        elif row == win_condition_for_o:
            print("O win")
            exit()

#win conditions for columns
        
    for col in range(3):
        if main_check[0][col] == main_check[1][col] == main_check[2][col] == playerX:
            print("X win")
            exit()
        elif main_check[0][col] == main_check[1][col] == main_check[2][col] == playerO:
            print("O win")
            exit()

#win condition for diagonal

    if main_check[0][0] == main_check[1][1] == main_check[2][2] == playerX or main_check[0][2] == main_check[1][1] == main_check[2][0] == playerX:
        print("X win")
        exit()
    elif main_check[0][0] == main_check[1][1] == main_check[2][2] == playerO or main_check[0][2] == main_check[1][1] == main_check[2][0] == playerO:
        print("O win")
        exit()

def check_if_draw(main_check):
    for row in main_check:
        if 0 in row:
            return False
    print("Draw")
    exit()

def main():
    main_check = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
    os.system('cls')
    print_check_board(main_check)
    while not check_win(main_check):
        print("Player 1: ")
        Player1(main_check)
        print("Player 2: ")
        Player2(main_check)

if __name__ == "__main__":
    main()
