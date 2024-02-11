from itertools import product
from time import time

def generate_permutations():
    for perm_tuple in product(range(10), repeat=4):
        perm_str = ''.join(map(str, perm_tuple)).zfill(4)
        yield perm_str

generator = generate_permutations()

start_timer = time()
for _ in range(10000):
    print(next(generator))
print(f'Process finished in: {round(time() - start_timer, 2)} seconds')
