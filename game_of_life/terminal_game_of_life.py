from copy import deepcopy
import random
import time
import os

# Any live cell with fewer than two live neighbors dies, as if by underpopulated.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by overpopulation.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

def draw_map(map, generation):
    os.system('cls')
    map_copy = deepcopy(map)
    for i in range(len(map_copy)):
        for j in range(len(map_copy[0])):
            if map_copy[i][j] == 1:
                map_copy[i][j] = '\u25A0'
            else:
                map_copy[i][j] = ' '
    if (len(map) + 1) % 2:
        print('+' + '---' * (len(map)) + '-+')
    else:
        print('+' + '---' * (len(map)) + '+')
    for line in map_copy:
        print('| ' + ' '.join(str(word) for word in line) + ' |')
    if (len(map) + 1) % 2:
        print('+' + '---' * (len(map)) + '-+')
    else:
        print('+' + '---' * (len(map)) + '+')
    print(f'Generation: {generation}')

def count_neighbors(map, x, y):
    counter = 0
    height = len(map)
    width = len(map[0])
    relative_indices = [
        (-1,-1),(-1, 0),(-1, 1),
        ( 0,-1),        ( 0, 1),
        ( 1,-1),( 1, 0),( 1, 1)
    ]
    for dx, dy in relative_indices:
        neighbor_x, neighbor_y = x + dx, y + dy
        if 0 <= neighbor_x < width and 0 <= neighbor_y < height:
            if map[neighbor_y][neighbor_x] == 1:
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
    return map

def choose_map_mode():
    possible_choices = [0,1]
    mode = 2
    while mode not in possible_choices:
        mode = int(input('Select map mode -> 0 (random map), 1 (Load from file): '))
    return mode

def empty_map_generator(size):
    map = [[0] * (size + (size // 2)) for _ in range(size)]
    return map

def random_map_generator():
    size = int(input('Enter size of map: '))
    while size < 10 and size > 45:
        size = int(input('Enter size of map: '))
    map = [[0] * (size + (size // 2)) for _ in range(size)]
    rng = [0,0,0,0,0,0,0,0,1]
    for i in range(len(map)):
        for j in range(len(map[0])):
            block = random.choice(rng)
            map[i][j] = block
    return map, size

def map_loader():
    map = []
    map_path = input('Enter path to your map: ')
    with open(map_path, 'r') as file:
        for line in file:
            row = [int(x) for x in line.strip()]
            map.append(row)
    return map

def main():
    generation = 0
    if not choose_map_mode():
        map, size = random_map_generator()
    else:
        map = map_loader()
        size = len(map)
    empty_map = empty_map_generator(size)
    while True:
        generation += 1
        map = game_logic(map, empty_map)
        draw_map(map, generation)
        time.sleep(0.2)

if __name__ == "__main__":
    main()
