import random

def random_matrix(size):
    possible_characters = [0,0,0,0,0,1]
    with open('game_of_life\\map.txt', 'w') as file:
        for i in range(size):
            for j in range(size + (size // 2)):
                x = random.choice(possible_characters)
                file.write(str(x))
            file.write('\n')
    file.close()

def main():
    size = int(input('Enter size of matrix: '))
    random_matrix(size)

main()
