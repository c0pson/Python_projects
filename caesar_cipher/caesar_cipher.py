import os

def get_mode_from_user() -> int:
    message = '''
Encryption/Decryption in python using Caesar cipher
[1 -> encrypt]
[2 -> decrypt from key]
[3 -> brute force decrypt]
[4 -> decrypt using frequency analysis]
:'''
    while True:
        user_inp = input(message)
        try:
            user_inp = int(user_inp)
            if user_inp == 1:
                return user_inp
            if user_inp == 2:
                return user_inp
            if user_inp == 3:
                return user_inp
            if user_inp == 4:
                return user_inp
            print('Provide only number associated with modes provided above')
        except ValueError:
            print('Provide only number associated with modes provided above')

def mode_1(alphabet) -> None:
    shift = get_shift_from_user()
    shifted_alphabet = key(alphabet, shift)
    text = get_text_from_user()
    encoded_text = encode(text, shifted_alphabet, alphabet)
    save_text(''.join(encoded_text))

def mode_2(alphabet) -> None:
    shift = get_shift_from_user()
    text = get_text_from_user()
    shifted_alphabet = key(alphabet, shift)
    decoded_text = decode_from_key(text, shifted_alphabet, alphabet)
    save_text(''.join(decoded_text))

def mode_3(alphabet) -> None:
    text = get_text_from_user()
    brute_force_texts = decode_brute_force(text, alphabet)
    save_text(''.join(brute_force_texts))

def mode_4(alphabet) -> None:
    text = get_text_from_user()
    frequency_analysis = method_for_long_texts(text, alphabet)
    save_text(''.join(frequency_analysis))

def get_shift_from_user() -> int:
    alphabet_len = 26
    while True:
        user_input = input('Enter shift value (1 to 25): ')
        try:
            user_input = int(user_input)
            if 0 <= user_input < alphabet_len:
                return user_input
            else:
                print('Please provide a number in the range from 1 to 25.')
        except ValueError:
            print('Provide integer number!')

def get_text_from_user() -> str:
    path_to_text = os.path.dirname(__file__)
    path_to_text = os.path.join(path_to_text, 'text.txt')
    with open(path_to_text, 'r') as file:
        user_input = file.read()
    file.close()
    return user_input

def save_text(text) -> None:
    path_to_file = os.path.dirname(__file__)
    path_to_file = os.path.join(path_to_file, 'output.txt')
    with open(path_to_file, 'w') as file:
        file.write(text)
    file.close()

def key(alphabet: list[str], shift: int) -> list[str]:
    shifted_alphabet = [''] * len(alphabet)
    for i in range(len(alphabet)):
        shifted_alphabet[i-shift] = alphabet[i]
    return shifted_alphabet

def encode(text: str, key: list[str], alphabet: list[str]) -> list[str]:
    encoded_text = [''] * len(text)
    counter = 0
    for letter in text:
        if letter.lower() not in alphabet:
            encoded_text[counter] = letter
        else:
            if letter.islower():
                encoded_text[counter] = key[alphabet.index(letter)]
            else:
                encoded_text[counter] = key[alphabet.index(letter.lower())].upper()
        counter += 1
    return encoded_text

def decode_from_key(text: str, key: list[str], alphabet: list[str]) -> list[str]:
    decoded_text = [''] * len(text)
    counter = 0
    for letter in text:
        if letter.lower() not in alphabet:
            decoded_text[counter] = letter
        else:
            if letter.islower():
                decoded_text[counter] = alphabet[key.index(letter)]
            else:
                decoded_text[counter] = alphabet[key.index(letter.lower())].upper()
        counter += 1
    return decoded_text

def brute_force(text, alphabet, spacing) -> list[str]:
    decoded_text = [''] * len(text)
    brute_force_tries = [''] * len(alphabet)
    for i in range(len(alphabet)):
            counter = 0
            shifted_alphabet = key(alphabet, i)
            for letter in text:
                if letter.lower() not in alphabet:
                    decoded_text[counter] = letter
                else:
                    if letter.islower():
                        decoded_text[counter] = alphabet[shifted_alphabet.index(letter)]
                    else:
                        decoded_text[counter] = alphabet[shifted_alphabet.index(letter.lower())].upper()
                counter += 1
            brute_force_tries[i] = f'Shift by {i}: \n\n' + ''.join(decoded_text) + f'\n\n{spacing} \n'
            decoded_text = [''] * len(text)
    return brute_force_tries

def decode_brute_force(text: str, alphabet: list[str]) -> list[str]:
    spacing = '=======' * 20
    if len(text) > 50:
        decoded_text = brute_force(text[0:51], alphabet, spacing)
        for item in decoded_text:
            print(item)
        shift = get_shift_from_user()
        shifted_alphabet = key(alphabet, shift)
        decoded_text = decode_from_key(text, shifted_alphabet, alphabet)
    else:
        decoded_text = brute_force(text, alphabet, spacing)
    return decoded_text

def method_for_long_texts(text, alphabet):
    letter_e_index = 5
    amount_of_letters_in_text = {
        'e': 0, 't': 0, 'o': 0, 'a': 0, 'i': 0, 'n': 0, 'h': 0, 's': 0, 'r': 0, 'd': 0,
        'l': 0, 'u': 0, 'm': 0, 'w': 0, 'c': 0, 'y': 0, 'f': 0, 'g': 0, 'p': 0, 'b': 0,
        'v': 0, 'k': 0, 'x': 0, 'j': 0, 'q': 0, 'z': 0 }
    for letter in text:
        letter = letter.lower()
        if letter in alphabet:
            amount_of_letters_in_text[letter] = amount_of_letters_in_text[letter] + 1
    amount_of_letters_in_text = dict(sorted(amount_of_letters_in_text.items(), key=lambda item: item[1], reverse=True))
    for i in range(26):
        if list(amount_of_letters_in_text.keys())[0] == alphabet[i]:
            shift = i + 1 - letter_e_index
    shifted_alphabet = key(alphabet, shift)
    decoded_text = decode_from_key(text, shifted_alphabet, alphabet)
    return decoded_text

def main() -> None:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    mode = get_mode_from_user()
    if mode == 1:
        mode_1(alphabet)
    elif mode == 2:
        mode_2(alphabet)
    elif mode == 3:
        mode_3(alphabet)
    elif mode == 4:
        mode_4(alphabet)

if __name__ == "__main__":
    main()
