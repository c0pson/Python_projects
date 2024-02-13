from copy import deepcopy
import keyboard

def game_logic(key_pressed):
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
    if key_pressed == 'a':
        ...
    elif key_pressed == 'd':
        ...
    elif key_pressed is None:
        map_copy = deepcopy(map)
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == 2:
                    map_copy[i][j] = 0
                    map_copy[i+1][j] = 2
        map = map_copy
        for line in map:
            print(line)
        print('\n')

def main():
    running = True
    counter = 0
    while running:
        if keyboard.is_pressed('a'):
            game_logic('a')
        elif keyboard.is_pressed('d'):
            game_logic('d')
        else:
            if counter % 6500:
                ...
            else:
                print('test')
        if keyboard.is_pressed('q'):
            running = False
        counter += 1

if __name__ == "__main__":
    main()
