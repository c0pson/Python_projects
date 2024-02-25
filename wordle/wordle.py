import customtkinter as ctk
import pyautogui
import random
import os

def press_tab(cell):
    if cell == 5:
        return
    pyautogui.press('tab')

def handle_delete():
    pyautogui.hotkey('shift', 'tab')

def enter_click_handle(guess_list, word, attempt_nb, entry_boxes_to_color):
    word_from_list = ''.join(guess_list)
    list_of_words = load_all_words(load_directory())
    if '' in guess_list:
        print('Ayo wtf')
    if word_from_list in list_of_words and '' not in guess_list:
        attempt_nb[0] += 1
        row_index = attempt_nb[0] - 2
        for i in range(5):
            index_in_row = row_index * 5 + i
            if guess_list[i] == word[i]:
                entry_boxes_to_color[index_in_row].configure(fg_color='green')
            elif guess_list[i] in word:
                entry_boxes_to_color[index_in_row].configure(fg_color='blue')
        guess_list.clear()
        guess_list.extend([''] * 5)

def check_row(event, entry_box, row_nb, attempt_nb, cell):
    check_length(event, entry_box, cell)
    if row_nb != attempt_nb[0]:
        return 'break'

def get_letter(event, cell, guess_list, entry_box):
    acceptable_input = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    entry_text = entry_box.get()
    if entry_text not in acceptable_input:
        entry_box.delete('0', 'end')
        return
    guess_list[cell-1] = entry_text
    entry_text = entry_text.upper()
    entry_box.delete('0', 'end')
    entry_box.insert(0, entry_text)
    entry_box.update()
    press_tab(cell)

def check_length(event, entry_box, cell):
    entry_box.configure(state='readonly')
    if len(entry_box.get()) > 0 and event.keysym != 'Tab' and event.keysym != 'Return': # 'Return' is somehow 'Enter'
        entry_box.delete('0', 'end')
    if event.keysym == 'Return':
        pyautogui.press('Tab')
    if event.keysym == 'BackSpace' and cell != 1:
        handle_delete()
    entry_box.configure(state='normal')

def load_directory():
    working_directory = os.path.dirname(__file__)
    word_list = os.path.join(working_directory, 'words.txt')
    return word_list

def load_all_words(words):
    list_of_words = []
    with open(words, 'r') as words_list:
        for word in words_list:
            list_of_words.append(word.strip('\n'))
        words_list.close()
    return list_of_words

def get_random_word(words):
    list_of_words = []
    word_as_list = []
    list_of_words = load_all_words(words)
    word = random.choice(list_of_words)
    for letter in word:
        word_as_list.append(letter)
    print(word_as_list)
    return word_as_list

def entry_frame_handle(app, my_font, cell, guess_list, row_nb, attempt_nb):
    entry = ctk.CTkEntry(master=app, font=my_font, width=60, height=60)
    entry.configure(insertontime=0)
    entry.grid(row=row_nb-1, column=cell-1, padx=5, pady=5, sticky='nsew')
    entry.bind(sequence='<KeyPress>', command=lambda event: check_row(event, entry, row_nb, attempt_nb, cell))
    entry.bind(sequence='<KeyRelease>', command=lambda event: get_letter(event, cell, guess_list, entry))
    return entry

def setup_line(frame, my_font, guess_list, row, attempt_nb):
    entries = []
    for cell in range(1, 6):
        entry = entry_frame_handle(frame, my_font, cell, guess_list, row, attempt_nb)
        entries.append(entry)
    return entries

def main_frame(app, my_font, guess_list, attempt_nb, word):
    frame_for_words = ctk.CTkFrame(master=app, corner_radius=10)
    frame_for_words.pack(side='top', fill='both', expand=True, padx=5, pady=5)

    centring_frame = ctk.CTkFrame(master=frame_for_words, corner_radius=10, fg_color='transparent')
    centring_frame.pack(side='top', expand=True, padx=5, pady=5)

    entry_boxes = []
    for row in range(1, 7):
        row_entry_boxes = setup_line(centring_frame, my_font, guess_list, row, attempt_nb)
        entry_boxes.extend(row_entry_boxes)

    frame_for_words.grid_rowconfigure(0, weight=1)
    frame_for_words.grid_rowconfigure(7, weight=1)
    frame_for_words.grid_columnconfigure(0, weight=1)
    frame_for_words.grid_columnconfigure(6, weight=1)

    button_frame(app, my_font, guess_list, word, attempt_nb, entry_boxes)

def button_frame(app, my_font, guess_list, word, attempt_nb, entry_boxes):
    frame_for_buttons = ctk.CTkFrame(master=app, width=360, corner_radius=10)
    frame_for_buttons.pack(side='top', fill='both', expand=True, padx=5, pady=5)

    enter_button = ctk.CTkButton(master=frame_for_buttons, text='Enter', font=my_font, width=100, height=72, command=lambda: enter_click_handle(guess_list, word, attempt_nb, entry_boxes))
    enter_button.pack(expand=True)

def main():
    attempt_nb = [1]
    words = load_directory()
    word = get_random_word(words)
    guess_list = [''] * 5
    print(word)

    WIDTH, HEIGHT = 420, 680
    app = ctk.CTk()
    app.geometry(f'{WIDTH}x{HEIGHT}')
    app.title('WORDLE')
    my_font = ctk.CTkFont(family='Hack Nerd Font Regular', size=44)

    main_frame(app, my_font, guess_list, attempt_nb, word)

    app.mainloop()

if __name__ == "__main__":
    main()