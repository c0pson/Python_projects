import os
import copy

def player_1_won():
    print("Player 1 has won the match!")
    #maybe rounds system

def player_2_won():
    print("Player 2 has won the match!")
    #maybe rounds system

def print_check_board(check_board):

    c_b_copy = copy.deepcopy(check_board)

    for i in range(len(c_b_copy)):
        for j in range(len(c_b_copy[i])):
            if c_b_copy[i][j] == 1:
                c_b_copy[i][j] = 'X'
            elif c_b_copy[i][j] == 2:
                c_b_copy[i][j] = 'O'
            else:
                c_b_copy[i][j] = ' '
    os.system('cls')

    print(f'\n\n| {c_b_copy[0][0]} || {c_b_copy[0][1]} || {c_b_copy[0][2]} || {c_b_copy[0][3]} || {c_b_copy[0][4]} |\n=========================')
    print(f'| {c_b_copy[1][0]} || {c_b_copy[1][1]} || {c_b_copy[1][2]} || {c_b_copy[1][3]} || {c_b_copy[1][4]} |\n=========================')
    print(f'| {c_b_copy[2][0]} || {c_b_copy[2][1]} || {c_b_copy[2][2]} || {c_b_copy[2][3]} || {c_b_copy[2][4]} |\n=========================')
    print(f'| {c_b_copy[3][0]} || {c_b_copy[3][1]} || {c_b_copy[3][2]} || {c_b_copy[3][3]} || {c_b_copy[3][4]} |\n=========================')
    print(f'| {c_b_copy[4][0]} || {c_b_copy[4][1]} || {c_b_copy[4][2]} || {c_b_copy[4][3]} || {c_b_copy[4][4]} |\n=========================')
    print('| 1 || 2 || 3 || 4 || 5 |')

def Player1(check_board):
    col = int(input("Provide column number: "))

    while check_board[0][col - 1] != 0:
        col = int(input("This column is full, provide correct number: "))

    for i in range(5):
        if check_board[4 - i][col - 1] == 0:
            check_board[4 - i][col - 1] = 1
            return check_board

def Player2(check_board):
    col = int(input("Provide column number: "))

    while check_board[0][col - 1] != 0:
        col = int(input("This column is full, provide correct number: "))

    for i in range(5):
        if check_board[4 - i][col - 1] == 0:
            check_board[4 - i][col - 1] = 2
            return check_board

def win_conditions(check_board):

#Player 1 conditions

#check for win in row
    
    for i in range(5):
        if check_board[i][0] == check_board[i][1] == check_board[i][2] == check_board[i][3] == 1 or check_board[i][1] == check_board[i][2] == check_board[i][3] == check_board[i][4] == 1:
            player_1_won()
            exit()

#check for win in column

    for i in range(5):
        if check_board[0][i] == check_board[1][i] == check_board[2][i] == check_board[3][i] == 1 or check_board[1][i] == check_board[2][i] == check_board[3][i] == check_board[4][i] == 1:
            player_1_won()
            exit()

#check for diagonal win

    # win_cond_01 = [[0, 0, 0, 0, 0],
    #                [0, 0, 0, 1, 0],
    #                [0, 0, 1, 0, 0],
    #                [0, 1, 0, 0, 0],
    #                [1, 0, 0, 0, 0]]
    
    # win_cond_02 = [[0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 1],
    #                [0, 0, 0, 1, 0],
    #                [0, 0, 1, 0, 0],
    #                [0, 1, 0, 0, 0]]

    for i in range(2):
        if check_board[4][i] == check_board[3][i + 1] == check_board[2][i + 2] == check_board[1][i + 3] == 1:
            player_1_won()
            exit()

    # win_cond_03 = [[0, 0, 0, 1, 0],
    #                [0, 0, 1, 0, 0],
    #                [0, 1, 0, 0, 0],
    #                [1, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0]]
    
    # win_cond_04 = [[0, 0, 0, 0, 1],
    #                [0, 0, 0, 1, 0],
    #                [0, 0, 1, 0, 0],
    #                [0, 1, 0, 0, 0],
    #                [0, 0, 0, 0, 0]]

        if check_board[3][i] == check_board[2][i + 1] == check_board[1][i + 2] == check_board[0][i + 3] == 1:
            player_1_won()
            exit()

    # win_cond_05 = [[0, 0, 0, 0, 0],
    #                [0, 1, 0, 0, 0],
    #                [0, 0, 1, 0, 0],
    #                [0, 0, 0, 1, 0],
    #                [0, 0, 0, 0, 1]]
    
    # win_cond_06 = [[0, 0, 0, 0, 0],
    #                [1, 0, 0, 0, 0],
    #                [0, 1, 0, 0, 0],
    #                [0, 0, 1, 0, 0],
    #                [0, 0, 0, 1, 0]]
    
        if check_board[0][i] == check_board[1][i + 1] == check_board[2][i + 2] == check_board[3][i + 3] == 1:
            player_1_won()
            exit()

    # win_cond_07 = [[0, 1, 0, 0, 0],
    #                [0, 0, 1, 0, 0],
    #                [0, 0, 0, 1, 0],
    #                [0, 0, 0, 0, 1],
    #                [0, 0, 0, 0, 0]]
    
    # win_cond_08 = [[1, 0, 0, 0, 0],
    #                [0, 1, 0, 0, 0],
    #                [0, 0, 1, 0, 0],
    #                [0, 0, 0, 1, 0],
    #                [0, 0, 0, 0, 0]]

        if check_board[1][i] == check_board[2][i + 1] == check_board[3][i + 2] == check_board[4][i + 3] == 1:
            player_1_won()
            exit()

#Player 2 conditions

#check for win in row
            
    for i in range(5):
        if check_board[i][0] == check_board[i][1] == check_board[i][2] == check_board[i][3] == 2 or check_board[i][1] == check_board[i][2] == check_board[i][3] == check_board[i][4] == 2:
            player_2_won()
            exit()

#check for win in column

    for i in range(5):
        if check_board[0][i] == check_board[1][i] == check_board[2][i] == check_board[3][i] == 2 or check_board[1][i] == check_board[2][i] == check_board[3][i] == check_board[4][i] == 2:
            player_2_won()
            exit()

#check for diagonal win

    # win_cond_01 = [[0, 0, 0, 0, 0],
    #                [0, 0, 0, 2, 0],
    #                [0, 0, 2, 0, 0],
    #                [0, 2, 0, 0, 0],
    #                [2, 0, 0, 0, 0]]
    
    # win_cond_02 = [[0, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 2],
    #                [0, 0, 0, 2, 0],
    #                [0, 0, 2, 0, 0],
    #                [0, 2, 0, 0, 0]]

    for i in range(2):
        if check_board[4][i] == check_board[3][i + 1] == check_board[2][i + 2] == check_board[1][i + 3] == 2:
            player_2_won()
            exit()

    # win_cond_03 = [[0, 0, 0, 2, 0],
    #                [0, 0, 2, 0, 0],
    #                [0, 2, 0, 0, 0],
    #                [2, 0, 0, 0, 0],
    #                [0, 0, 0, 0, 0]]
    
    # win_cond_04 = [[0, 0, 0, 0, 2],
    #                [0, 0, 0, 2, 0],
    #                [0, 0, 2, 0, 0],
    #                [0, 2, 0, 0, 0],
    #                [0, 0, 0, 0, 0]]

        if check_board[3][i] == check_board[2][i + 1] == check_board[1][i + 2] ==  check_board[0][i + 3] == 2:
            player_2_won()
            exit()

    # win_cond_05 = [[0, 0, 0, 0, 0],
    #                [0, 2, 0, 0, 0],
    #                [0, 0, 2, 0, 0],
    #                [0, 0, 0, 2, 0],
    #                [0, 0, 0, 0, 2]]
    
    # win_cond_06 = [[0, 0, 0, 0, 0],
    #                [2, 0, 0, 0, 0],
    #                [0, 2, 0, 0, 0],
    #                [0, 0, 2, 0, 0],
    #                [0, 0, 0, 2, 0]]
    
        if check_board[0][i] == check_board[1][i + 1] == check_board[2][i + 2] == check_board[3][i + 3] == 2:
            player_2_won()
            exit()

    # win_cond_07 = [[0, 2, 0, 0, 0],
    #                [0, 0, 2, 0, 0],
    #                [0, 0, 0, 2, 0],
    #                [0, 0, 0, 0, 2],
    #                [0, 0, 0, 0, 0]]
    
    # win_cond_08 = [[2, 0, 0, 0, 0],
    #                [0, 2, 0, 0, 0],
    #                [0, 0, 2, 0, 0],
    #                [0, 0, 0, 2, 0],
    #                [0, 0, 0, 0, 0]]

        if check_board[1][i] == check_board[2][i + 1] == check_board[3][i + 2] == check_board[4][i + 3] == 2:
            player_2_won()
            exit()

def check_draw(check_board):
    row_check_for_draw = [0] * 5
    counter = 0

    for row in check_board:
        if 0 in row:
            row_check_for_draw[counter] = 1
            counter += 1
        else:
            counter += 1

    if row_check_for_draw == [0 ,0 ,0 ,0 ,0]:
        print("Draw")
        exit()

def main():
    check_board = [[0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0]]

    print_check_board(check_board)

    while True:
        print("Player 1")
        Player1(check_board)
        print_check_board(check_board)
        win_conditions(check_board)
        check_draw(check_board)
        print("Player 2")
        Player2(check_board)
        print_check_board(check_board)
        win_conditions(check_board)
        check_draw(check_board)

if __name__ == "__main__":
    main()
