from string import ascii_letters, digits, punctuation
from cryptography.fernet import Fernet
from datetime import datetime
import customtkinter as ctk
from subprocess import call
from enum import Enum
import pyperclip
import hashlib
import secrets
import random
import time
import sys
import os

class Colors (str, Enum):
    BLUE_BACKGROUND = '#B5C0D0'
    GREEN ='#CCD3CA'
    YELLOW ='#F5E8DD'
    PINK ='#EED3D9'
    DARK_PINK = '#cca9b0'
    GRAPHITE = '#35374B'
    RED = '#D04848'
    TRANSPARENT = 'transparent'

def check_req():
    if not os.path.exists(resource_path('storage')):
        os.makedirs(resource_path('storage'))
    if not os.path.exists(resource_path('storage\\storage.txt')):
        storage = open(resource_path('storage\\storage.txt'), 'w+')
        storage.close()
    if not os.path.exists(resource_path('storage\\storage.txt.enc')):
        enc_storage = open(resource_path('storage\\storage.txt.enc'), 'w+')
        enc_storage.close()
    if not os.path.exists(resource_path('storage\\logs.txt')):
        log_files = open(resource_path('storage\\logs.txt'), 'w+')
        log_files.close()

def logs(info):
    length = 0
    with open(resource_path('storage\\logs.txt'), 'r') as file:
        length = len(file.readlines()) + 1
    if length < 10:
        length = str(f' {length}')
    with open(resource_path('storage\\logs.txt'), 'a') as file:
        now = time.time()
        date = datetime.fromtimestamp(now)
        log_message = f'Log {length}: {date.strftime('%d %B %Y %H:%M:%S')} | {info}\n'
        file.write(log_message)

def load_keys():
    file = open(resource_path('storage\\keys.txt'), 'r')
    file.close()
    with open(resource_path('storage\\keys.txt'), 'r') as file:
        key = file.readline()
    return key

def generate_key():
    key = Fernet.generate_key()
    with open(resource_path('storage\\keys.txt'), 'w') as file:
        file.write(key.decode())
    return key

def confirm_password(label, app, my_font, my_font_2, login_success):
    logs(f'Set up new password | id: {os.getpid()}')
    password = label.get()
    with open(resource_path('storage\\marker.marker'), 'w') as file:
        file.write(f'{password}')
    encrypt_marker_file(resource_path('storage\\marker.marker'))
    destroy_old_page(app)
    login_page(app, my_font_2, my_font, [1], login_success)

def encrypt_marker_file(file_path):
    key = generate_key()
    cipher = Fernet(key)
    with open(file_path, 'rb') as file:
        data = file.read()
    encrypted_data = cipher.encrypt(data)
    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

def set_password(app, app_frame, my_font, my_font_2, login_success):
    my_font_x27 = ctk.CTkFont(family='Hack Nerd Font Propo', size=27)
    flag = [0]

    def show_password(entry_label, flag):
        if flag[0] == 0:
            entry_label.configure(show='')
            flag[0] = 1
        else:
            entry_label.configure(show='*')
            flag[0] = 0

    app_frame = ctk.CTkFrame(master=app, corner_radius=10, fg_color=Colors.YELLOW, border_color=Colors.GRAPHITE, border_width=3)
    app_frame.pack(expand=True, padx=0, pady=0)

    label = ctk.CTkLabel(master=app_frame, text='Insert password:', font=my_font_x27, text_color=Colors.GRAPHITE)
    label.pack(side='top', expand=True, fill='x', padx=23, pady=20)

    entry_label = ctk.CTkEntry(master=app_frame, width=44, font=my_font_x27, fg_color=Colors.GREEN, text_color=Colors.GRAPHITE, show='*', border_width=2, border_color=Colors.GRAPHITE)
    entry_label.pack(side='top', expand=True, fill='x', padx=23, pady=0)

    frame_for_buttons = ctk.CTkFrame(master=app_frame, height=20, fg_color=Colors.YELLOW)
    frame_for_buttons.pack(side='bottom', expand=True, padx=23, pady=20, fill='x')

    button = ctk.CTkCheckBox(master=frame_for_buttons, command=lambda: show_password(entry_label, flag),
                            fg_color=Colors.PINK, hover=False, checkmark_color=Colors.DARK_PINK, text='Show password',
                            text_color=Colors.GRAPHITE, border_color=Colors.GRAPHITE, border_width=2, font=my_font)
    button.pack(side='left', expand=True, fill='x')

    ok_button = ctk.CTkButton(master=frame_for_buttons, command=lambda: confirm_password(entry_label, app, my_font, my_font_2, login_success),
                            fg_color=Colors.PINK, text='OK', width=60, hover_color=Colors.DARK_PINK,
                            text_color=Colors.GRAPHITE, border_color=Colors.GRAPHITE, border_width=2, font=my_font)
    ok_button.pack(side='left', fill='y')

def destroy_old_page(page):
    for child in page.winfo_children():
        child.destroy()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2  # type: ignore
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def read_file():
    with open(resource_path('storage\\marker.marker'), 'rb') as file:
        data = file.read()
        return data.decode()

def login_proc(app, password_box, was_first_time, login_success, my_font):
    def decrypt_password(encrypted_password):
        key = load_keys().encode()
        fernet = Fernet(key)
        decrypted_password = fernet.decrypt(encrypted_password)
        return decrypted_password.decode()

    encrypted_password = read_file()
    password_str = decrypt_password(encrypted_password)

    def hash_password(password, salt=None):
        if salt is None:
            salt = secrets.token_hex(16)
        hash_obj = hashlib.sha256()
        hash_obj.update((password + salt).encode())
        return hash_obj.hexdigest(), salt

    def verify_password(password, stored_hashed_password, stored_salt):
        hashed_input_password, _ = hash_password(password, stored_salt)
        return hashed_input_password == stored_hashed_password

    stored_hashed_password, stored_salt = hash_password(password_str)

    if verify_password(password_box.get(), stored_hashed_password, stored_salt):
        logs(f'Logged in | id: {os.getpid()}')
        destroy_old_page(app)
        after_login(app, was_first_time, login_success)
    else:
        logs(f'Wrong password was entered: {password_box.get()} | id: {os.getpid()}')
        display_error(app, my_font, 'Wrong Password')

def login_page(app, my_font, my_font_2, was_first_time, login_success):
    flag = [0]
    def show_password(entry_label, flag):
        if flag[0] == 0:
            entry_label.configure(show='')
            flag[0] = 1
        else:
            entry_label.configure(show='*')
            flag[0] = 0
    login_frame = ctk.CTkFrame(master=app, corner_radius=10, border_width=2,
                                fg_color=Colors.YELLOW, border_color=Colors.GRAPHITE)
    login_frame.pack(side='top', expand=True, padx=10, pady=10)

    password_label = ctk.CTkLabel(master=login_frame, fg_color=Colors.TRANSPARENT, font=my_font,
                                bg_color=Colors.TRANSPARENT, text='Password', text_color=Colors.GRAPHITE)
    password_label.pack(padx=5, pady=10)

    password_box = ctk.CTkEntry(master=login_frame, width=270, height=60, fg_color=Colors.GREEN,
                                corner_radius=10, font=my_font, show='*', text_color=Colors.GRAPHITE)
    password_box.pack(padx=15, pady=0)

    button = ctk.CTkCheckBox(master=login_frame, command=lambda: show_password(password_box, flag),
                            fg_color=Colors.PINK, hover=False, checkmark_color=Colors.DARK_PINK, text='Show password',
                            text_color=Colors.GRAPHITE, border_color=Colors.GRAPHITE, border_width=3, font=my_font_2)
    button.pack(side='top', expand=True, fill='x', padx=15, pady=10)

    login_button = ctk.CTkButton(master=login_frame, width=120, height=50, fg_color=Colors.PINK, text_color=Colors.GRAPHITE, text='Login',
                                corner_radius=10, font=my_font, border_color=Colors.GRAPHITE, border_width=2, hover_color=Colors.DARK_PINK,
                                command=lambda: login_proc(app, password_box, was_first_time, login_success, my_font_2))
    login_button.pack(padx=10, pady=15)

def edit_label(label, edit_button, current_label, button_index_2 , text):
    if edit_button.cget('text') == 'Edit':
        label.configure(state='normal')
        edit_button.configure(text='Save')
    else:
        label.configure(state='disabled')
        edit_button.configure(text='Edit')
        if text.cget('text') == 'Name:':
            logs(f'Edited named in {current_label[0]} | id: {os.getpid()}')
            save_info_in_file(int(button_index_2.index(current_label[0])*4+2), label.get())
        if text.cget('text') == 'Link:':
            logs(f'Edited link in {current_label[0]} | id: {os.getpid()}')
            save_info_in_file(int(button_index_2.index(current_label[0])*4+3), label.get())
        if text.cget('text') == 'Pass:':
            logs(f'Edited password in {current_label[0]} | id: {os.getpid()}')
            save_info_in_file(int(button_index_2.index(current_label[0])*4+4), label.get())

def encrypt_file(file_path, cipher):
    with open(file_path, 'rb') as file:
        data = file.read()
    encrypted_data = cipher.encrypt(data)
    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    with open(file_path, 'w+') as file:
        file.truncate(0)
    logs(f'Encrypted data | id: {os.getpid()}')

def decrypt_pass(file_path, cipher):
    with open(file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data

def decrypt_file(file_path, cipher):
    with open(file_path + '.enc', 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    logs(f'Decrypted storage | id: {os.getpid()}')

def copy_label(label):
    pyperclip.copy(str(label.get()))

def get_label_info(name) -> list[str] | None:
    path = resource_path('storage\\storage.txt')
    with open(path, 'r') as file:
        found = False
        next_lines = []
        for index, line in enumerate(file, start=1):
            if found:
                next_lines.append(line.strip())
                if len(next_lines) == 3:
                    return next_lines
            if name in line:
                found = True
            if index % 4 == 0:
                found = False
                next_lines = []

def username_label_con(content_frame, my_font_x21, info, current_label, button_index_2):
    frame = ctk.CTkFrame(master=content_frame, corner_radius=5, fg_color=Colors.BLUE_BACKGROUND,
                        border_color=Colors.GRAPHITE, border_width=3)
    frame.pack(side='top', padx=10, pady=0, fill='x')
    text = ctk.CTkLabel(master=frame, text='Name:', font=my_font_x21, text_color=Colors.GRAPHITE)
    text.pack(side='left', padx=8, pady=10)
    label = ctk.CTkEntry(master=frame, height=48, font=my_font_x21, fg_color=Colors.GREEN,
                        border_color=Colors.GRAPHITE, border_width=3, text_color=Colors.GRAPHITE)
    label.insert('0', info)
    label.configure(state='disabled')
    label.pack(side='left', padx=8, pady=10, fill='x', expand=True)
    edit_button = ctk.CTkButton(master=frame, corner_radius=5, text='Edit', height=48, fg_color=Colors.PINK,
                                hover_color=Colors.DARK_PINK, font=my_font_x21, border_width=3,
                                command=lambda: edit_label(label, edit_button, current_label, button_index_2, text),
                                border_color=Colors.GRAPHITE, text_color=Colors.GRAPHITE)
    edit_button.pack(side='right', padx=8, pady=10)
    copy_button = ctk.CTkButton(master=frame, corner_radius=5, text='Copy', fg_color=Colors.PINK,
                                hover_color=Colors.DARK_PINK, height=48, font=my_font_x21, command=lambda: copy_label(label),
                                border_width=3, border_color=Colors.GRAPHITE, text_color=Colors.GRAPHITE)
    copy_button.pack(side='right', padx=8, pady=10)

def url_label_con(content_frame, my_font_x21, info, current_label, button_index_2):
    frame = ctk.CTkFrame(master=content_frame, corner_radius=5, fg_color=Colors.BLUE_BACKGROUND, border_color=Colors.GRAPHITE, border_width=3)
    frame.pack(side='top', padx=10, pady=10, fill='x')
    text = ctk.CTkLabel(master=frame, text='Link:', font=my_font_x21, text_color=Colors.GRAPHITE)
    text.pack(side='left', padx=8, pady=10)
    label = ctk.CTkEntry(master=frame, height=48, font=my_font_x21, fg_color=Colors.GREEN, border_color=Colors.GRAPHITE,
                        border_width=3, text_color=Colors.GRAPHITE)
    label.insert('0', info)
    label.configure(state='disabled')
    label.pack(side='left', padx=8, pady=10, fill='x', expand=True)
    edit_button = ctk.CTkButton(master=frame, corner_radius=5, text='Edit', height=48, fg_color=Colors.PINK, font=my_font_x21,
                                hover_color=Colors.DARK_PINK, command=lambda: edit_label(label, edit_button, current_label, button_index_2, text),
                                border_width=3, border_color=Colors.GRAPHITE, text_color=Colors.GRAPHITE)
    edit_button.pack(side='right', padx=8, pady=10)
    copy_button = ctk.CTkButton(master=frame, corner_radius=5, text='Open', fg_color=Colors.PINK,
                                hover_color=Colors.DARK_PINK, height=48, font=my_font_x21, command=lambda: open_in_browser(label.get()),
                                border_width=3, border_color=Colors.GRAPHITE, text_color=Colors.GRAPHITE)
    copy_button.pack(side='right', padx=8, pady=10)

def open_in_browser(link):
    call(['C:\\Program Files\\Mozilla Firefox\\Firefox.exe', '-new-tab', link])
    logs(f'Opened link {link} | id: {os.getpid()}')

def strength_set(password, label, bar):
    password_strength = 0
    special_characters_counter = 0
    numbers_counter = 0
    lower_letters_counter = 0
    upper_characters_counter = 0
    strength = 0
    in_common = 0
    first = 0.0
    second = 0.0
    third = 0.0
    fourth = 0.0
    alphabet_l = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
    alphabet_u = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    previous_char = ['']
    for character in password:
        if previous_char[0] == character:
            strength += 1
        else:
            pass
        if character in alphabet_l:
            lower_letters_counter += 1
        elif character in alphabet_u:
            upper_characters_counter += 1
        elif character in numbers:
            numbers_counter+= 1
        else:
            special_characters_counter += 1
        previous_char[0] = character
    with open(resource_path('resources\\most_common_pass.txt'), 'r') as file:
        if len(password) < 10:
            for line in file:
                if line in password:
                    in_common = 0.5
                    break
    if special_characters_counter != 0:
        first = ((numbers_counter+lower_letters_counter+upper_characters_counter)/special_characters_counter)
    if numbers_counter != 0:
        second = ((special_characters_counter + lower_letters_counter + upper_characters_counter) / numbers_counter)
    if lower_letters_counter != 0:
        third = ((special_characters_counter + numbers_counter + upper_characters_counter) / lower_letters_counter)
    if upper_characters_counter != 0:
        fourth = ((special_characters_counter + numbers_counter + lower_letters_counter) / upper_characters_counter)
    password_strength = (((first*1.5) + (second*1.5) + (third*1.5) + (fourth*1.5)) * len(password))
    password_strength *= ((special_characters_counter+special_characters_counter+lower_letters_counter+upper_characters_counter) / 100)
    if in_common == 0:
        in_common = 1
    if len(password) >= 16:
        password_strength *= 2.3
    elif len(password) >= 8:
        password_strength *= 2.3
    if strength > len(password) and password_strength < 0.5:
        password_strength -= strength * 0.04
    final = ((password_strength * in_common)) / 100
    bar.set(final)
    if password != '':
        if final <= 0.1:
            label.configure(text='Awful password ')
        if final > 0.1:
            label.configure(text=' Weak password ')
        if final > 0.4:
            label.configure(text=' Good password ')
        if final > 0.6:
            label.configure(text='Strong password')
        if final > 0.9:
            label.configure(text='Solid password ')
    else:
        label.configure(text='  No password  ')

def password_label_con(content_frame, my_font_x21, info, current_label, button_index_2):
    frame = ctk.CTkFrame(master=content_frame, corner_radius=5, fg_color=Colors.BLUE_BACKGROUND, border_color=Colors.GRAPHITE, border_width=3)
    frame.pack(side='top', padx=10, pady=10, fill='x')
    text = ctk.CTkLabel(master=frame, text='Pass:', font=my_font_x21, text_color=Colors.GRAPHITE)
    text.pack(side='left', padx=8, pady=10)
    label = ctk.CTkEntry(master=frame, height=48, font=my_font_x21, fg_color=Colors.GREEN, border_color=Colors.GRAPHITE, border_width=3, text_color=Colors.GRAPHITE)
    label.insert('0', info)
    label.configure(state='disabled')
    label.pack(side='left', padx=8, pady=10, fill='x', expand=True)
    edit_button = ctk.CTkButton(master=frame, corner_radius=5, text='Edit', height=48, fg_color=Colors.PINK,
                                hover_color=Colors.DARK_PINK, font=my_font_x21, command=lambda: edit_label(label, edit_button, current_label, button_index_2, text),
                                border_width=3, border_color=Colors.GRAPHITE, text_color=Colors.GRAPHITE)
    edit_button.pack(side='right', padx=8, pady=10)
    copy_button = ctk.CTkButton(master=frame, corner_radius=5, text='Copy', fg_color=Colors.PINK,
                                hover_color=Colors.DARK_PINK, height=48, font=my_font_x21, command=lambda: copy_label(label),
                                border_width=3, border_color=Colors.GRAPHITE, text_color=Colors.GRAPHITE)
    copy_button.pack(side='right', padx=8, pady=10)
    frame_1 = ctk.CTkFrame(master=content_frame, corner_radius=5, fg_color=Colors.BLUE_BACKGROUND, border_color=Colors.GRAPHITE, border_width=3)
    frame_1.pack(side='top', padx=10, pady=0, fill='x')
    text_1 = ctk.CTkLabel(master=frame_1, text='Strength:', font=my_font_x21, text_color=Colors.GRAPHITE)
    text_1.pack(side='left', padx=10, pady=10)
    strength_bar = ctk.CTkProgressBar(master=frame_1, fg_color=Colors.GREEN, border_color=Colors.GRAPHITE, border_width=2, progress_color=Colors.PINK, height=20)
    strength_bar.pack(side='left', padx=8, pady=10, fill='x', expand=True)
    frame_2 = ctk.CTkFrame(master=frame_1, border_width=3, border_color=Colors.GRAPHITE, fg_color=Colors.PINK, corner_radius=5)
    frame_2.pack(side='left', fill='x', padx=8, pady=10)
    strength_text = ctk.CTkLabel(master=frame_2, text='No password', text_color=Colors.GRAPHITE, font=my_font_x21)
    strength_text.pack(side='top', padx=8, pady=8)
    strength_set(label.get(), strength_text ,strength_bar)
    label.bind("<KeyRelease>", lambda bar: strength_set(label.get(), strength_text, bar = strength_bar))

def generate_password(value, label):
    label.configure(state='normal')
    label.delete('0', 'end')
    exceptions = [",", "`", "~"]
    password = "".join(random.choice("".join(set(ascii_letters + digits + punctuation) - set(exceptions))) for _ in range(int(value)))
    label.insert('end', f'{password}')
    label.configure(state='disabled')
    pyperclip.copy(password)

def update_length(label, length):
    space = ''
    if length < 10:
        space = ' '
    label.configure(text=f'  {space}{int(length)} ')

def generate_password_con(content_frame, my_font_x21):
    frame = ctk.CTkFrame(master=content_frame, corner_radius=5, fg_color=Colors.BLUE_BACKGROUND, border_color=Colors.GRAPHITE, border_width=3)
    frame.pack(side='top', padx=10, pady=10, fill='x')
    frame_1 = ctk.CTkFrame(master=frame, fg_color=Colors.BLUE_BACKGROUND)
    frame_1.pack(side='bottom', padx=8, pady=10, fill='x')
    length_info_frame = ctk.CTkFrame(master=frame_1, corner_radius=5, fg_color=Colors.PINK, height=48, border_width=3, border_color=Colors.GRAPHITE)
    length_info_frame.pack(side='right', padx=0, pady=0, fill='x')
    space = ctk.CTkLabel(master=frame_1, text='        ')
    space.pack(side='right')
    length_label = ctk.CTkLabel(master=length_info_frame, font=my_font_x21, text_color=Colors.GRAPHITE)
    length_label.pack(padx=4, pady=4)
    slider = ctk.CTkSlider(master=frame_1, from_=1, to=25, number_of_steps=24, border_width=2, progress_color=Colors.PINK, height=22,
                            border_color=Colors.GRAPHITE, fg_color=Colors.GREEN, hover=False, button_color=Colors.GRAPHITE,
                            command=lambda label: update_length(length_label, slider.get()))
    slider.pack(side='right', expand=True, padx=0, pady=0, fill='x')
    slider.set(18)
    length_label.configure(text=f'  {int(slider.get())} ')
    space_2 = ctk.CTkLabel(master=frame_1, text='        ')
    space_2.pack(side='right')
    frame_2 = ctk.CTkFrame(master=frame, fg_color=Colors.BLUE_BACKGROUND)
    frame_2.pack(side='bottom', padx=8, pady=10, fill='x', expand=True)
    text = ctk.CTkLabel(master=frame_2, text='Generator: ', font=my_font_x21, text_color=Colors.GRAPHITE)
    text.pack(side='left', fill='x')
    generated_password = ctk.CTkEntry(master=frame_2, height=48, font=my_font_x21, fg_color=Colors.GREEN,
                                        border_color=Colors.GRAPHITE, border_width=3, text_color=Colors.GRAPHITE)
    generated_password.configure(state='disabled')
    generated_password.pack(side='left', padx=0, pady=0, fill='x', expand=True)
    space_1 = ctk.CTkLabel(master=frame_2, text='     ')
    space_1.pack(side='left', fill='x')
    generate_button = ctk.CTkButton(master=frame_2, corner_radius=5, text='Generate', height=48, fg_color=Colors.PINK,
                                hover_color=Colors.DARK_PINK, font=my_font_x21, command=lambda: generate_password(slider.get(), generated_password),
                                border_width=3, border_color=Colors.GRAPHITE, text_color=Colors.GRAPHITE)
    generate_button.pack(side='left', padx=0, pady=0, fill='x')

def load_labels_from_file(button_index_2, label_name_entry, password_index_frame, my_font_x21, button_index, current_label, content_frame):
    path = resource_path('storage\\storage.txt')
    with open(path,'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if i % 4 == 0:
                add(line.strip('\n'), label_name_entry, button_index_2, password_index_frame, my_font_x21, button_index, current_label, content_frame, 0)
    current_label[0] = ''

def append_file(data):
    path = resource_path('storage\\storage.txt')
    with open(path, 'a') as file:
        file.write(f'{data}{'\n'*4}')

def remove_from_file(line_numbers):
    path = resource_path('storage\\storage.txt')
    with open(path, 'r') as file:
        lines = file.readlines()
    remaining_lines = [line for i, line in enumerate(lines, start=1) if i not in line_numbers]
    with open(path, 'w') as file:
        file.writelines(remaining_lines)

def save_info_in_file(line_number, data):
    path = resource_path('storage\\storage.txt')
    with open(path, 'r') as file:
        lines = file.readlines()
        lines[line_number - 1] = data + '\n'
    with open(path, 'w') as file:
        file.writelines(lines)

def load_info(content_frame, my_font_x21, current_label, button_index_2):
    for child in content_frame.winfo_children():
        child.destroy()
    info: list[str] | None = get_label_info(current_label[0])
    if info and info != ['']:
        url_label_con(content_frame, my_font_x21, info[1], current_label, button_index_2)
        username_label_con(content_frame, my_font_x21, info[0], current_label, button_index_2)
        password_label_con(content_frame, my_font_x21, info[2], current_label, button_index_2)
        generate_password_con(content_frame, my_font_x21)
    else:
        url_label_con(content_frame, my_font_x21, '', current_label, button_index_2)
        username_label_con(content_frame, my_font_x21, '', current_label, button_index_2)
        password_label_con(content_frame, my_font_x21, '', current_label, button_index_2)
        generate_password_con(content_frame, my_font_x21)

def add(label_name, label_name_entry, button_index_2, password_index_frame, my_font_x21, button_index, current_label, content_frame, to_append_file):
    if label_name == '' or label_name in button_index_2:
        return
    new_label=ctk.CTkButton(master=password_index_frame, text=label_name, font=my_font_x21, corner_radius=5, fg_color=Colors.PINK, width=50,
                            border_color=Colors.GRAPHITE, border_width=2, hover_color=Colors.DARK_PINK, text_color=Colors.GRAPHITE,
                            command=lambda: button_clicked(new_label, current_label, button_index, button_index_2, content_frame, my_font_x21))
    new_label.pack(expand=True, fill='both', padx=1, pady=1)
    button_index.append(new_label)
    button_index_2.append(label_name)
    if to_append_file:
        label_name_entry.delete('0', 'end')
        logs(f'Added new password {label_name} | id: {os.getpid()}')
        append_file(button_index_2[-1])
        destroy_old_page(password_index_frame)
        button_index = []
        button_index_2 = []
        load_labels_from_file(button_index_2, label_name_entry, password_index_frame, my_font_x21, button_index, current_label, content_frame)
        button_index[-1].invoke()
        password_index_frame.focus()

def remove(current_label, button_index, button_index_2, content_frame, password_index_frame, my_font_x21, search, label_name_entry, app):
    logs(f'Removed password {current_label[0]} | id: {os.getpid()}')
    line_num = int(button_index_2.index(current_label[0])*4+1)
    if current_label[0] != '':
        destroy_old_page(content_frame)
        button_index[int(button_index_2.index(current_label[0]))].destroy()
        remove_from_file({line_num, line_num+1, line_num+2, line_num+3})
        button_index.pop(int(button_index_2.index(current_label[0])))
        button_index_2.pop(int(button_index_2.index(current_label[0])))
    current_label[0] = ''
    search_for_label(button_index, button_index_2, password_index_frame, search, my_font_x21, content_frame, current_label, label_name_entry, app)

def button_clicked(label, current_label, button_index, button_index_2, content_frame, my_font_x21):
    if current_label[0] != '':
        button_index[int(button_index_2.index(current_label[0]))].configure(fg_color=Colors.PINK)
    button_index[int(button_index_2.index(label.cget('text')))].configure(fg_color=Colors.DARK_PINK)
    current_label[0] = label.cget('text')
    load_info(content_frame, my_font_x21, current_label, button_index_2)

def on_validate(d, i, P, s, S, v, V, W):
    return len(P) <= 14

def add_from_search(password_index_frame, label_name, my_font_x21, button_index, button_index_2, content_frame, current_label):
    destroy_old_page(content_frame)
    new_label=ctk.CTkButton(master=password_index_frame, text=label_name, font=my_font_x21, corner_radius=5, fg_color=Colors.PINK, width=50,
                            border_color=Colors.GRAPHITE, border_width=2, hover_color=Colors.DARK_PINK, text_color=Colors.GRAPHITE,
                            command=lambda: button_clicked(new_label, current_label, button_index, button_index_2, content_frame, my_font_x21))
    new_label.pack(expand=True, fill='both', padx=1, pady=1)
    button_index.append(new_label)
    button_index_2.append(label_name)

def display_error(app, my_font, my_text):
    message = []
    half_width = app.winfo_width() // 2
    half_height = app.winfo_height() // 2
    try:
        message[1].destroy()
    except IndexError:
        pass
    color = Colors.YELLOW
    space = 0
    if my_text == 'Wrong Password':
        color = Colors.BLUE_BACKGROUND
        space = 75
    frame_for_error = ctk.CTkFrame(master=app, fg_color=Colors.RED, border_color=Colors.GRAPHITE, border_width=3, width=200, height=(half_height // 10), bg_color=color)
    label = ctk.CTkLabel(master=frame_for_error, text=my_text, font=my_font, text_color=Colors.GRAPHITE)
    frame_for_error.place(x=half_width-space, y=half_height // 12)
    label.pack(padx=10, pady=10)
    message.append(frame_for_error)
    app.after(1500, lambda: frame_for_error.destroy())

def search_for_label(button_index, button_index_2, password_index_frame, search, my_font_x21, content_frame, current_label, label_name_entry, app):
    founded_items = []
    items_to_show = []
    items_to_show_2 = []
    if search != '':
        for i, item in enumerate(button_index_2):
            if search in item:
                founded_items.append(item)
        destroy_old_page(password_index_frame)
        counter = 0
        for i, item in enumerate(button_index_2):
            if len(founded_items) > counter:
                if founded_items[counter] == button_index_2[i]:
                    items_to_show.append(button_index[i])
                    items_to_show_2.append(button_index_2[i])
                    counter += 1
        if founded_items != []:
            button_index = []
            button_index_2 = []
            current_label[0] = ''
            for item in founded_items:
                add_from_search(password_index_frame, item, my_font_x21, button_index, button_index_2, content_frame, current_label)
            founded_items = []
            items_to_show = []
            items_to_show_2 = []
            current_label[0] = ''
        else:
            destroy_old_page(content_frame)
            display_error(app, my_font_x21, 'Not found!')
    else:
        destroy_old_page(password_index_frame)
        button_index = []
        button_index_2 = []
        load_labels_from_file(button_index_2, label_name_entry, password_index_frame, my_font_x21, button_index, current_label, content_frame)
        password_index_frame.focus()

def after_login(app, was_first_time, login_success):
    my_font_x21 = ctk.CTkFont(family='Hack Nerd Font Propo', size=21)
    button_index = []
    button_index_2 = []
    current_label = ['']  

    main_frame = ctk.CTkFrame(master=app, corner_radius=0, fg_color=Colors.BLUE_BACKGROUND)
    main_frame.pack(side='left', expand=True, fill='both', padx=0, pady=0)

    index_frame = ctk.CTkFrame(master=main_frame, corner_radius=7, fg_color=Colors.BLUE_BACKGROUND)
    index_frame.pack(side='left', fill='both', padx=8, pady=8)

    search_frame = ctk.CTkFrame(master=index_frame, corner_radius=7, border_color=Colors.GRAPHITE,
                                border_width=3, fg_color=Colors.YELLOW)
    search_frame.pack(side='top', fill='both', padx=0, pady=0)

    search_frame_2 = ctk.CTkFrame(master=search_frame, fg_color=Colors.YELLOW, corner_radius=7)
    search_frame_2.pack(side='top', fill='both', padx=10, pady=8)

    search_text = ctk.CTkLabel(master=search_frame_2, fg_color=Colors.YELLOW, text='Search:', font=my_font_x21, text_color=Colors.GRAPHITE)
    search_text.pack(side='top', padx=0, pady=0)

    search_label = ctk.CTkEntry(master=search_frame_2, font=my_font_x21, height=38, fg_color=Colors.GREEN,
                                    border_color=Colors.GRAPHITE, text_color=Colors.GRAPHITE)
    search_label.pack(side='top', fill='x', padx=0, pady=0, expand=True)

    frame_for_border = ctk.CTkFrame(master=index_frame, corner_radius=7, border_color=Colors.GRAPHITE,
                                    fg_color=Colors.YELLOW, border_width=3)
    frame_for_border.pack(side='top', expand=True, fill='both', padx=0, pady=8)

    password_index_frame = ctk.CTkScrollableFrame(master=frame_for_border, corner_radius=7, scrollbar_button_hover_color=Colors.DARK_PINK,
                                                scrollbar_button_color=Colors.DARK_PINK, fg_color=Colors.YELLOW)
    password_index_frame.pack(side='top', expand=True, fill='both', padx=4, pady=4)

    spacing_frame  = ctk.CTkFrame(master=index_frame, height=10, fg_color=Colors.TRANSPARENT)
    spacing_frame.pack()

    buttons_index_frame = ctk.CTkFrame(master=index_frame, corner_radius=7, border_color=Colors.GRAPHITE,
                                        border_width=3, fg_color=Colors.YELLOW)
    buttons_index_frame.pack(side='bottom', fill='x', padx=0, pady=0)

    validate_cmd = buttons_index_frame.register(on_validate)
    label_name_entry = ctk.CTkEntry(master=buttons_index_frame, font=my_font_x21, height=38, fg_color=Colors.GREEN,
                                    border_color=Colors.GRAPHITE, text_color=Colors.GRAPHITE, validate="key",
                                    validatecommand=(validate_cmd, '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'))
    label_name_entry.pack(side='top', fill='x', padx=10, pady=10)

    search_label.bind("<KeyRelease>", command=lambda search: search_for_label(button_index, button_index_2, password_index_frame, search_label.get(), my_font_x21, content_frame, current_label, label_name_entry, app))

    add_button = ctk.CTkButton(master=buttons_index_frame, text='Add', font=my_font_x21, height=38,
                                command=lambda: add(str(label_name_entry.get()), label_name_entry, button_index_2, password_index_frame, my_font_x21, button_index, current_label, content_frame, 1),
                                border_color=Colors.GRAPHITE, border_width=2, fg_color=Colors.PINK, hover_color=Colors.DARK_PINK, text_color=Colors.GRAPHITE)
    add_button.pack(side='top', fill='x', padx=10, pady=0)

    content_frame = ctk.CTkFrame(master=main_frame, corner_radius=7, fg_color=Colors.YELLOW,
                                border_color=Colors.GRAPHITE, border_width=3)
    content_frame.pack(side='right', expand=True, fill='both', padx=8, pady=8)

    remove_button = ctk.CTkButton(master=buttons_index_frame, text='Remove',
                                font=my_font_x21, height=38, command=lambda: remove(current_label, button_index, button_index_2, content_frame, password_index_frame, my_font_x21, search_label.get(), label_name_entry, app),
                                border_color=Colors.GRAPHITE, border_width=2,
                                fg_color=Colors.PINK, hover_color=Colors.DARK_PINK,
                                text_color=Colors.GRAPHITE)
    remove_button.pack(side='top', fill='x', padx=10, pady=10)

    if was_first_time[0] != 1:
        key = load_keys().encode()
        cipher = Fernet(key)
        decrypt_file(resource_path('storage\\storage.txt'), cipher)
    
    load_labels_from_file(button_index_2, label_name_entry, password_index_frame, my_font_x21, button_index, current_label, content_frame)
    login_success[0] = 1

def main():
    logs(f'App opened | id: {os.getpid()}')
    login_success = [0]
    check_req()
    app = ctk.CTk()
    app.title('Password manager')
    app.iconbitmap(resource_path('resources\\icon.ico'))
    x = app.winfo_screenwidth() // 2
    y = app.winfo_screenheight() // 2
    my_font_x16 = ctk.CTkFont(family='Hack Nerd Font Propo', size=16)
    my_font_x32 = ctk.CTkFont(family='Hack Nerd Font Propo', size=32)
    app.geometry(f'1080x720+{x-540}+{y-400}')
    app.minsize(width=900, height=540)
    app_frame = ctk.CTkFrame(master=app, fg_color=Colors.BLUE_BACKGROUND, corner_radius=0)
    app_frame.pack(expand=True, padx=0, pady=0, fill='both')
    if not os.path.exists(resource_path('storage\\marker.marker')):
        set_password(app_frame, app_frame, my_font_x16, my_font_x32, login_success)
    else:
        login_page(app_frame, my_font_x32, my_font_x16, [0], login_success)
    app.mainloop()
    if login_success[0] == 1:
        encrypt_file(resource_path('storage\\storage.txt'), Fernet(load_keys().encode()))
    logs(f'Closed app | id: {os.getpid()}')

if __name__ == "__main__":
    main()
