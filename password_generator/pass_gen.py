from string import ascii_letters, digits, punctuation
import pyperclip
import argparse
import random

def main():
    params = argparse.ArgumentParser()
    params.add_argument("--len", type = int)

    args = params.parse_args()
    lenght = args.len

    if not lenght:
        lenght = 20

    exceptations = [",", "`", "~"]
    password = "".join(random.choice("".join(set(ascii_letters + digits + punctuation) - set(exceptations))) for _ in range(lenght))
    pyperclip.copy(password)
    print("Password copied to clipboard")

if __name__ == "__main__":
    main()
