import random
import time
import copy
import os

class Minesweeper:
    def __init__(self, size):
        self.size = size
        self.board = self.create_board()

    def create_board(self):
        self.board = [['X'] * self.size for _ in range(self.size)]
        self.bombs_placed = 0
        while self.bombs_placed < self.size:
            x = random.randrange(0, len(self.board))
            y = random.randrange(0, len(self.board[0]))
            if self.board[x][y] != 'B':
                self.board[x][y] = 'B'
                self.bombs_placed += 1
        return self.board

    def player_moves(self):
        self.list_of_options = [''] * self.size
        for i in range(self.size):
            self.list_of_options[i] = str(i + 1)
        self.x_cord = input('Row: ')
        while self.x_cord not in self.list_of_options:
            print(f'Invalid input, pls prov num from 1 to {self.size}')
            self.x_cord = input('Row: ')
        self.x_cord = int(self.x_cord)
        self.y_cord = input("Column: ")
        while self.y_cord not in self.list_of_options:
            print(f'Invalid input, please provide number from 1 to {self.size}')
            y_cord = input("Column: ")
        y_cord = int(y_cord)
        return self.x_cord, self.y_cord

    def print_board(self):
        for row in self.board:
            print(row)

if __name__ == "__main__":
    Minesweeper(10)
