import customtkinter as ctk
import random
import os

def get_letter(event, cell, guess_list, entry_box):
    entry_text = entry_box.get()
    guess_list[cell-1] = entry_text
    entry_text = entry_text.upper()
    entry_box.delete('0', 'end')
    entry_box.insert(0, entry_text)

def check_length(event, entry_box):
    if len(entry_box.get()) > 0 and event.keysym != 'Tab':
        entry_box.delete('0', 'end')

def load_directory():
    working_directory = os.path.dirname(__file__)
    word_list = os.path.join(working_directory, 'words.txt')
    return word_list

def get_random_word(words):
    list_of_words = []
    word_as_list = []
    with open(words, 'r') as words_list:
        for word in words_list:
            list_of_words.append(word.strip('\n'))
    word = random.choice(list_of_words)
    for letter in word:
        word_as_list.append(letter)
    return word_as_list

def entry_frame_handle(app, my_font, cell, guess_list):
    entry = ctk.CTkEntry(master=app, font=my_font)
    entry.grid(row=0, column=cell-1)
    entry.bind(sequence='<KeyPress>', command=lambda event: check_length(event, entry))
    entry.bind(sequence='<KeyRelease>', command=lambda event: get_letter(event, cell, guess_list, entry))

def main():
    words = load_directory()
    word = get_random_word(words)
    guess_list = [''] * 5
    print(word)

    WIDTH, HEIGHT = 1080, 720
    app = ctk.CTk()
    app.geometry(f'{WIDTH}x{HEIGHT}')
    app.title('WORDLE')
    my_font = ctk.CTkFont(family='Hack Nerd Font Regular', size=34)

    entry_frame_handle(app, my_font, 1, guess_list)
    entry_frame_handle(app, my_font, 2, guess_list)
    entry_frame_handle(app, my_font, 3, guess_list)
    entry_frame_handle(app, my_font, 4, guess_list)
    entry_frame_handle(app, my_font, 5, guess_list)

    app.mainloop()

if __name__ == "__main__":
    main()
