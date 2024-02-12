def map_generator(size):
    map = [[0] * size for _ in range(size)]
    for line in map:
        print(' '.join(str(word) for word in line))

def main():
    map_generator(10)

if __name__ == "__main__":
    main()
