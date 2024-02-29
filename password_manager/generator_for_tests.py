def print_continuous_pattern(num_patterns):
    for i in range(1, num_patterns + 1):
        print("Label", i)
        print(f'name {i}\nlink {i}\npassword {i}')

num_patterns = 25
print_continuous_pattern(num_patterns)
