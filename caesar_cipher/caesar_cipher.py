def get_shift_from_user() -> int:
    alphabet_len = 26
    while True:
        user_input = input('Enter shift value (1 to 25): ')
        try:
            user_input = int(user_input)
            if 1 <= user_input < alphabet_len:
                return user_input
            else:
                print('Please provide a number in the range from 1 to 25.')
        except ValueError:
            print('Provide integer number!')

def key(alphabet: list[str], shift: int) -> list[str]:
    shifted_alphabet = [''] * len(alphabet)
    for i in range(len(alphabet)):
        shifted_alphabet[i] = alphabet[i-shift]
    return shifted_alphabet

def encode(text: str, key: list[str], alphabet: list[str]):
    encoded_text = [''] * len(text)
    counter = 0
    special_characters = ' .,?!;:-!@#$%^&*()=+_\\[]{};\'\"<>?/~`'
    for letter in text:
        if letter.lower() in special_characters:
            encoded_text[counter] = letter
        else:
            if letter.islower():
                encoded_text[counter] = key[alphabet.index(letter)]
            else:
                encoded_text[counter] = key[alphabet.index(letter.lower())].upper()
        counter += 1
    print(''.join(encoded_text))

def main() -> None:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    shift = get_shift_from_user()
    shifted_alphabet = key(alphabet, shift)
    encode("The quick brown fox jumps over the lazy dog.", shifted_alphabet, alphabet)

if __name__ == "__main__":
    main()
