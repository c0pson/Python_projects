from time import time

start = time()

for i in range(100):
    print(i)

print(f'Process finished in {round(time() - start, 2)}seconds')
