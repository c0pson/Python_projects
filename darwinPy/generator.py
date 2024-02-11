import random
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
filename = "chromosomes.txt"
full_path = os.path.join(script_directory, filename)

f = open(full_path, "w")

for i in range(1000):
    randomLenght = random.randrange(2, 12)
    for j in range(randomLenght):
        randomChromosome = random.randrange(0, 100)
        f.write(str(randomChromosome) + " ")
    f.write("\n")
