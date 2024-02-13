from copy import deepcopy
import keyboard
import time
import os

def game_logic(key_pressed, map):
    if key_pressed == 'a':
        map_copy = deepcopy(map)
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == 2:
                    map_copy[i][j-1] = 2
                    map_copy[i][j] = 0
    if key_pressed == 'd':
        map_copy = deepcopy(map)
        for i in range(len(map)):
            for j in range(len(map[0])-1,-1,-1):
                if map[i][j] == 2:
                    map_copy[i][j+1] = 2
                    map_copy[i][j] = 0
    if key_pressed is None:
        map_copy = deepcopy(map)
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == 2:
                    map_copy[i][j] = 0
                    map_copy[i + 1][j] = 2
    map = deepcopy(map_copy)
    return map

def print_map(map):
    os.system('cls')
    for line in map:
        print(line)

def main():
    map = [ [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 2, 2, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 1, 1, 0, 0, 0], 
            [0, 0, 1, 1, 1, 1, 0, 0, 0] ]

    running = True
    counter = 0
    key_pressed = None
    while running:
        if keyboard.is_pressed('a'):
            key_pressed = 'a'
            time.sleep(0.1)
        if keyboard.is_pressed('d'):
            key_pressed = 'd'
            time.sleep(0.1)
        if not counter % 7000:
            map = game_logic(key_pressed, map)
            key_pressed = None
            print_map(map)
        counter += 1

if __name__ == "__main__":
    main()
