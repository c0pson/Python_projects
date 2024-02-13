from copy import deepcopy
import keyboard
import time
import os

def game_logic(key_pressed, map):
    len_of_block = 2
    map_copy = deepcopy(map)
    if key_pressed == 'a':
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == 2 and j >= len_of_block + 1:
                    for k in range(len_of_block):
                        map_copy[i][j - k] = 2
                        map_copy[i][j] = 0
    if key_pressed == 'd':
        for i in range(len(map)):
            for j in range((len(map[0]) - 1), -1, -1):
                if map[i][j] == 2 and map[i][j + len_of_block]:
                    for k in range(len_of_block):
                        map_copy[i][j + k] = 2
                        map_copy[i][j] = 0
    if key_pressed is None:
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == 2 and i < len(map) - 2:
                    map_copy[i][j] = 0
                    map_copy[i + 1][j] = 2
    map = deepcopy(map_copy)
    return map

# I have to change the whole handling and might change to pygame due to technical reasons

def print_map(map):
    os.system('cls')
    for line in map:
        print(' '.join(str(word) for word in line))

def main():
    map = [ [9, 0, 0, 0, 2, 2, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9] ]

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
            counter = 0
        counter += 1

if __name__ == "__main__":
    main()
