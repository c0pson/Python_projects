import random

random_ints = [random.randint(1, 6721) for _ in range(999)]
# print(random_ints)

def search_for_smallest_in_list(list_of_int):
    biggest_val = list_of_int[0]
    for i in range(len(list_of_int) - 1):
        if biggest_val < list_of_int[i + 1]:
            biggest_val = list_of_int[i + 1]
        else:
            continue
    print(biggest_val)

search_for_smallest_in_list(random_ints)
