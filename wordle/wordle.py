import customtkinter as ctk
import pyautogui
import random
import os

def enter_click_handle(guess_list, word):
    print(guess_list)
    for i in range(5):
        if guess_list[i] == word[i]:
            print(f'Letter {i+1} is correct')

    if '' not in guess_list:
        ...

#main logic

def check_row(event, entry_box, row_nb):
    check_length(event, entry_box)
    if row_nb != 1:
        return 'break'

def get_letter(event, cell, guess_list, entry_box):
    acceptable_input = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    entry_text = entry_box.get()
    if entry_text not in acceptable_input:
        entry_box.delete('0', 'end')
        return
    guess_list[cell-1] = entry_text
    entry_text = entry_text.upper()
    entry_box.delete('0', 'end')
    entry_box.insert(0, entry_text)
    print(guess_list)

def check_length(event, entry_box):
    if len(entry_box.get()) > 0 and event.keysym != 'Tab' and event.keysym != 'Return': # 'Return' is somehow 'Enter'
        entry_box.delete('0', 'end')
    if event.keysym == 'Return':
        pyautogui.press('Tab')

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
        words_list.close()
    for letter in word:
        word_as_list.append(letter)
    print(word_as_list)
    return word_as_list

def entry_frame_handle(app, my_font, cell, guess_list, row_nb, attempt_nb):
    entry = ctk.CTkEntry(master=app, font=my_font, width=60, height=60)
    entry.configure(insertontime=0)
    entry.grid(row=row_nb-1, column=cell-1, padx=5, pady=5, sticky='nsew')
    entry.bind(sequence='<KeyPress>', command=lambda event: check_row(event, entry, row_nb, attempt_nb))
    entry.bind(sequence='<KeyRelease>', command=lambda event: get_letter(event, cell, guess_list, entry))

def setup_line(frame, my_font, guess_list, row, attempt_nb):
    entry_frame_handle(frame, my_font, 1, guess_list, row, attempt_nb)
    entry_frame_handle(frame, my_font, 2, guess_list, row, attempt_nb)
    entry_frame_handle(frame, my_font, 3, guess_list, row, attempt_nb)
    entry_frame_handle(frame, my_font, 4, guess_list, row, attempt_nb)
    entry_frame_handle(frame, my_font, 5, guess_list, row, attempt_nb)

def main_frame(app, my_font, guess_list, attempt_nb):
    frame_for_words = ctk.CTkFrame(master=app, corner_radius=10)
    frame_for_words.pack(side='top', fill='both', expand=True, padx=5, pady=5)

    centring_frame = ctk.CTkFrame(master=frame_for_words, corner_radius=10, fg_color='transparent')
    centring_frame.pack(side='top', expand=True, padx=5, pady=5)

    setup_line(centring_frame, my_font, guess_list, 1, attempt_nb)
    setup_line(centring_frame, my_font, guess_list, 2, attempt_nb)
    setup_line(centring_frame, my_font, guess_list, 3, attempt_nb)
    setup_line(centring_frame, my_font, guess_list, 4, attempt_nb)
    setup_line(centring_frame, my_font, guess_list, 5, attempt_nb)
    setup_line(centring_frame, my_font, guess_list, 6, attempt_nb)

    frame_for_words.grid_rowconfigure(0, weight=1)
    frame_for_words.grid_rowconfigure(7, weight=1)
    frame_for_words.grid_columnconfigure(0, weight=1)
    frame_for_words.grid_columnconfigure(6, weight=1)

def button_frame(app, my_font, guess_list, word):
    frame_for_buttons = ctk.CTkFrame(master=app, width=360, corner_radius=10)
    frame_for_buttons.pack(side='top', fill='both', expand=True, padx=5, pady=5)

    enter_button = ctk.CTkButton(master=frame_for_buttons, text='Enter', font=my_font, width=100, height=72, command=lambda: enter_click_handle(guess_list, word))
    enter_button.pack(expand=True)

def main():
    attempt_nb = 1
    words = load_directory()
    word = get_random_word(words)
    guess_list = [''] * 5
    print(word)

    WIDTH, HEIGHT = 420, 680
    app = ctk.CTk()
    app.geometry(f'{WIDTH}x{HEIGHT}')
    app.title('WORDLE')
    my_font = ctk.CTkFont(family='Hack Nerd Font Regular', size=44)

    main_frame(app, my_font, guess_list, attempt_nb)

    button_frame(app, my_font, guess_list, word)

    app.mainloop()

if __name__ == "__main__":
    main()
