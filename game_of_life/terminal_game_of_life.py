from copy import deepcopy
import time
import os

# Any live cell with fewer than two live neighbors dies, as if by underpopulated.
#
# matrix = [[0,0,0,0],
#           [0,1,1,0],
#           [0,0,0,0],
#           [0,0,0,0]] -- all of them will be dead
#
# Any live cell with two or three live neighbors lives on to the next generation.
#
# matrix = [[0,0,0,0],
#           [0,1,1,0],
#           [1,0,0,1],
#           [0,1,1,0]] -- it will stay forever due to this and other rules
#
# Any live cell with more than three live neighbors dies, as if by overpopulation.
#
# matrix = [[0,0,0,0],
#           [1,0,1,0],
#           [0,1,0,0],
#           [1,0,1,0]] -- middle one will be dead due to this rule, all other will also disappear due to first rule
#
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
#
# matrix = [[0,0,0,0],
#           [0,1,1,0],
#           [0,1,0,0],
#           [0,0,0,0]] -- it will create a square
#
#================================================================================

def draw_map(map):
    map_copy = deepcopy(map)
    for i in range(len(map_copy)):
        for j in range(len(map_copy)):
            if map_copy[i][j] == 1:
                map_copy[i][j] = '\u25A0'
            else:
                map_copy[i][j] = ' '
    for line in map_copy:
        print(' '.join(str(word) for word in line))

def count_neighbors(map, x, y):
    counter = 0
    height = len(map)
    width = len(map[0])  # Fix here: Use len(map[0]) to get the width
    relative_indices = [
        (-1,-1),(-1, 0),(-1, 1),
        ( 0,-1),        ( 0, 1),
        ( 1,-1),( 1, 0),( 1, 1)
    ]
    for dx, dy in relative_indices:
        neighbor_x, neighbor_y = x + dx, y + dy
        if 0 <= neighbor_x < width and 0 <= neighbor_y < height:
            if map[neighbor_y][neighbor_x] == 1:  # Fix here: Correct indexing
                counter += 1
    return counter

def game_logic(map, map_new):
    for i in range(len(map)):
        for j in range(len(map[0])):
            living_neighbors = count_neighbors(map, j, i)
            if map[i][j] == 0:
                if living_neighbors == 3:
                    map_new[i][j] = 1
                else:
                    map_new[i][j] = 0
            else:
                if living_neighbors < 2 or living_neighbors > 3:
                    map_new[i][j] = 0
                else:
                    map_new[i][j] = 1
    for i in range(len(map)):
        for j in range(len(map[0])):
            map[i][j] = map_new[i][j]
    draw_map(map)
    return map

def map_generator(size):
    map = [[0] * size for _ in range(size)]
    return map

def map_drawing_mode():
    ...

def main():
    os.system('cls')
    size = 40
    map = map_generator(size)
    empty_map = map_generator(size)
    print('Generation: 0')
    draw_map(map)
    time.sleep(0.5)
    for i in range(10):
        os.system('cls')
        print(f'Generation: {i + 1}')
        map = game_logic(map, empty_map)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
