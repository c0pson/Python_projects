import random

def print_board(board):
    for line in board:
        print(line)

def starting_board():
    board = [[0] * 4 for _ in range(4)]
    elements_to_choose = [2, 2 , 2 , 2 , 2 , 2 , 2, 4]
    starting_element = random.choice(elements_to_choose)
    x_cord = random.randrange(len(board))
    y_cord = random.randrange(len(board[0]))
    board[x_cord][y_cord] = starting_element
    print_board(board)

def main():
    starting_board()

main()
