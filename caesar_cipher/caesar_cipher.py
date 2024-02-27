def get_shift_from_user() -> int:
    user_input = ''
    while user_input == '':
        user_input = input('Enter shift value: ')
        try:
            user_input = int(user_input)
        except ValueError:
            user_input = ''
    return user_input

def key(alphabet: list[str], shift: int) -> list[str]:
    shifted_alphabet = [''] * len(alphabet)
    for i in range(len(alphabet)):
        shifted_alphabet[i] = alphabet[i-shift]
    return shifted_alphabet

def main() -> None:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    shift = get_shift_from_user()
    shifted_alphabet = key(alphabet, shift)
    print(shifted_alphabet)

if __name__ == "__main__":
    main()
