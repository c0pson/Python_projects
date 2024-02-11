import random

val = 1000
vec = []

for i in range(val):
    vec.append([f'{random.randrange(147, 201)}.{random.randrange(0, 10)} {random.randrange(30, 57)}.{random.randrange(0, 10)}'])
vec = [sublist for sublist in vec if sublist]
print(vec)

with open('zuza\\generator_inputu.txt', 'w') as out:
    for line in vec:
        for word in line:
            out.write(f'{str(word)}\n')
