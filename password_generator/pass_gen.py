from string import ascii_letters, digits, punctuation
import pyperclip
import argparse
import random

def main():
    params = argparse.ArgumentParser()
    params.add_argument("--len", type = int)

    args = params.parse_args()
    length = args.len

    if not length:
        length = 20

    exceptions = [",", "`", "~"]
    password = "".join(random.choice("".join(set(ascii_letters + digits + punctuation) - set(exceptions))) for _ in range(length))
    pyperclip.copy(password)
    print("Password copied to clipboard")

if __name__ == "__main__":
    main()
