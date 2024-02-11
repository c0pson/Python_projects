import random
import string
import time
import sys

def user_input():
    user_in = input("Enter text to display in matrix styled search: ")
    sys.stdout.write("\033c")
    return user_in

def shell_output_if_space(passed_string):
    when_to_break = random.choice(string.ascii_lowercase)
    for letter in string.ascii_lowercase:
        if when_to_break == letter:
            return 0
        sys.stdout.write("\033[1D")
        sys.stdout.write(" ")
        sys.stdout.write("\033[1G")
        sys.stdout.write(passed_string + letter)
        sys.stdout.flush()
        time.sleep(0.2)

def shell_output_if_incorrect(passed_string):
    sys.stdout.write("\033[1D")
    sys.stdout.write(" ")
    sys.stdout.write("\033[1G")
    # Display the next letter
    sys.stdout.write(passed_string)
    sys.stdout.flush()
    time.sleep(0.2)

def shell_output_if_correct(passed_string):
    sys.stdout.write("\033[1D")
    sys.stdout.write(" ")
    sys.stdout.write("\033[1G")
    sys.stdout.write(passed_string)
    sys.stdout.write('\n')
    time.sleep(0.2)

def main(sentence):
    result = [] * len(sentence)
    for i in range(len(sentence)):
        for letter in string.ascii_lowercase:
            if sentence[i] == " ":
                shell_output_if_space(''.join(result))
                result.append(" ")
                shell_output_if_correct(''.join(result))
                break
            elif letter is sentence[i]:
                result.append(letter)
                shell_output_if_correct(''.join(result))
                break
            else:        
                shell_output_if_incorrect(''.join(result) + letter)

if __name__ == "__main__":
    main(user_input())
