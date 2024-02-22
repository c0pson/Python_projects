import random

def generate_long_list():
    list = [0] * 10000
    for i in range(10000):
        factor = random.randrange(0, 3)
        list[i] = i * i + factor
    print(list)
    return list

def binary_search(sorted_array, target):
    counter = 0
    while len(sorted_array) > 0:
        middle_of_array = len(sorted_array) // 2

        if sorted_array[middle_of_array] > target:
            sorted_array = sorted_array[:middle_of_array]
            counter += 1

        elif sorted_array[middle_of_array] < target:
            sorted_array = sorted_array[middle_of_array+1:]
            counter += 1

        else:
            print(f'{target} found in {counter} steps.\n')
            return middle_of_array

    print(f'Target {target} not found')
    return -1

def main():
    sorted_list = generate_long_list()
    target = int(input("Enter number to search for: "))
    binary_search(sorted_list, target)

if __name__ == '__main__':
    main()
