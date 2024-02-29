import customtkinter as ctk
from enum import Enum
import pyperclip

class Colors (str, Enum):
    BLUE_BACKGROUND = '#B5C0D0'
    GREEN ='#CCD3CA'
    YELLOW ='#F5E8DD'
    PINK ='#EED3D9'
    DARK_PINK = '#cca9b0'
    GRAPHITE = '#35374B'
    RED = '#D04848'
    TRANSPARENT = 'transparent'

def destroy_old_page(page):
    for child in page.winfo_children():
        child.destroy()

def login_proc(app, password_box, wrong_pass_label, wrong_pass_frame):
    password = password_box.get()
    secret_password = 'secret' # I will add some hashing or something like this
    if secret_password == password:
        for child in app.winfo_children():
            child.destroy()
        after_login(app)
    else:
        password_box.delete('0', 'end')
        wrong_pass_frame.configure(fg_color=Colors.RED)
        wrong_pass_frame.configure(border_width=3)
        wrong_pass_frame.configure(border_color=Colors.GRAPHITE)
        wrong_pass_label.configure(text_color=Colors.GRAPHITE)

def login_page(app, my_font, my_font_2):
    login_frame = ctk.CTkFrame(master=app, corner_radius=10, border_width=2,
                                fg_color=Colors.YELLOW, border_color=Colors.GRAPHITE)
    login_frame.pack(side='top', expand=True, padx=10, pady=10)

    password_label = ctk.CTkLabel(master=login_frame, fg_color=Colors.TRANSPARENT, font=my_font,
                                bg_color=Colors.TRANSPARENT, text='Password', text_color=Colors.GRAPHITE)
    password_label.pack(padx=5, pady=10)

    password_box = ctk.CTkEntry(master=login_frame, width=270, height=60, fg_color=Colors.GREEN,
                                corner_radius=10, font=my_font, show='*', text_color=Colors.GRAPHITE)
    password_box.pack(padx=15, pady=0)

    wrong_pass_frame = ctk.CTkFrame(master=app, fg_color=Colors.BLUE_BACKGROUND, corner_radius=10)
    wrong_pass_frame.pack(side='bottom', pady=20)

    wrong_pass_label = ctk.CTkLabel(master=wrong_pass_frame, text='WRONG PASSWORD',
                                    text_color=Colors.BLUE_BACKGROUND, font=my_font_2)
    wrong_pass_label.pack(padx=40, pady=10)

    login_button = ctk.CTkButton(master=login_frame, width=120, height=50, fg_color=Colors.PINK, text_color=Colors.GRAPHITE,
                                corner_radius=10, text='Login', font=my_font, border_color=Colors.GRAPHITE, border_width=2,
                                hover_color=Colors.DARK_PINK, command=lambda: login_proc(app, password_box, wrong_pass_label, wrong_pass_frame))
    login_button.pack(padx=10, pady=15)

def edit_label(label, edit_button):
    if edit_button.cget('text') == 'Edit':
        label.configure(state='normal')
        edit_button.configure(text='Save')
    else:
        label.configure(state='disabled')
        edit_button.configure(text='Edit')

def copy_label(label):
    pyperclip.copy(str(label.get()))

def get_label_info(name) -> list[str] | None:
    path = 'C:\\Users\\piotr\\Documents\\Files\\python\\password_manager\\storage.txt'
    with open(path, 'r') as file:
        found = False
        for line in file:
            if found:
                return line.strip().split(', ')
            if name in line:
                found = True

def username_label_con(content_frame, my_font_x21, info):
    frame = ctk.CTkFrame(master=content_frame, corner_radius=5, fg_color=Colors.BLUE_BACKGROUND, border_color=Colors.GRAPHITE, border_width=3)
    frame.pack(side='top', padx=10, pady=10, fill='x')
    text = ctk.CTkLabel(master=frame, text='Name:', font=my_font_x21, text_color=Colors.GRAPHITE)
    text.pack(side='left', padx=8, pady=10)
    label = ctk.CTkEntry(master=frame, height=48, font=my_font_x21, fg_color=Colors.GREEN, border_color=Colors.GRAPHITE, border_width=3, text_color=Colors.GRAPHITE)
    label.insert('0', info)
    label.configure(state='disabled')
    label.pack(side='left', padx=8, pady=10, fill='x', expand=True)
    edit_button = ctk.CTkButton(master=frame, corner_radius=5, text='Edit', height=48, fg_color=Colors.PINK,
                                hover_color=Colors.DARK_PINK, font=my_font_x21, command=lambda: edit_label(label, edit_button),
                                border_width=3, border_color=Colors.GRAPHITE, text_color=Colors.GRAPHITE)
    edit_button.pack(side='right', padx=8, pady=10)
    copy_button = ctk.CTkButton(master=frame, corner_radius=5, text='Copy', fg_color=Colors.PINK,
                                hover_color=Colors.DARK_PINK, height=48, font=my_font_x21, command=lambda: copy_label(label),
                                border_width=3, border_color=Colors.GRAPHITE, text_color=Colors.GRAPHITE)
    copy_button.pack(side='right', padx=8, pady=10)

def url_label_con(content_frame, my_font_x21, info):
    frame = ctk.CTkFrame(master=content_frame, corner_radius=5, fg_color=Colors.BLUE_BACKGROUND, border_color=Colors.GRAPHITE, border_width=3)
    frame.pack(side='top', padx=10, pady=0, fill='x')
    text = ctk.CTkLabel(master=frame, text='Link:', font=my_font_x21, text_color=Colors.GRAPHITE)
    text.pack(side='left', padx=8, pady=10)
    label = ctk.CTkEntry(master=frame, height=48, font=my_font_x21, fg_color=Colors.GREEN, border_color=Colors.GRAPHITE, border_width=3, text_color=Colors.GRAPHITE)
    label.insert('0', info)
    label.configure(state='disabled')
    label.pack(side='left', padx=8, pady=10, fill='x', expand=True)
    edit_button = ctk.CTkButton(master=frame, corner_radius=5, text='Edit', height=48, fg_color=Colors.PINK,
                                hover_color=Colors.DARK_PINK, font=my_font_x21, command=lambda: edit_label(label, edit_button),
                                border_width=3, border_color=Colors.GRAPHITE, text_color=Colors.GRAPHITE)
    edit_button.pack(side='right', padx=8, pady=10)
    copy_button = ctk.CTkButton(master=frame, corner_radius=5, text='Copy', fg_color=Colors.PINK,
                                hover_color=Colors.DARK_PINK, height=48, font=my_font_x21, command=lambda: copy_label(label),
                                border_width=3, border_color=Colors.GRAPHITE, text_color=Colors.GRAPHITE)
    copy_button.pack(side='right', padx=8, pady=10)

def password_label_con(content_frame, my_font_x21, info):
    frame = ctk.CTkFrame(master=content_frame, corner_radius=5, fg_color=Colors.BLUE_BACKGROUND, border_color=Colors.GRAPHITE, border_width=3)
    frame.pack(side='top', padx=10, pady=10, fill='x')
    text = ctk.CTkLabel(master=frame, text='Pass:', font=my_font_x21, text_color=Colors.GRAPHITE)
    text.pack(side='left', padx=8, pady=10)
    label = ctk.CTkEntry(master=frame, height=48, font=my_font_x21, fg_color=Colors.GREEN, border_color=Colors.GRAPHITE, border_width=3, text_color=Colors.GRAPHITE)
    label.insert('0', info)
    label.configure(state='disabled')
    label.pack(side='left', padx=8, pady=10, fill='x', expand=True)
    edit_button = ctk.CTkButton(master=frame, corner_radius=5, text='Edit', height=48, fg_color=Colors.PINK,
                                hover_color=Colors.DARK_PINK, font=my_font_x21, command=lambda: edit_label(label, edit_button),
                                border_width=3, border_color=Colors.GRAPHITE, text_color=Colors.GRAPHITE)
    edit_button.pack(side='right', padx=8, pady=10)
    copy_button = ctk.CTkButton(master=frame, corner_radius=5, text='Copy', fg_color=Colors.PINK,
                                hover_color=Colors.DARK_PINK, height=48, font=my_font_x21, command=lambda: copy_label(label),
                                border_width=3, border_color=Colors.GRAPHITE, text_color=Colors.GRAPHITE)
    copy_button.pack(side='right', padx=8, pady=10)

def load_labels_from_file(button_index_2, label_name_entry, password_index_frame, my_font_x21, button_index, current_label, content_frame):
    path = 'C:\\Users\\piotr\\Documents\\Files\\python\\password_manager\\storage.txt'
    with open(path,'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if i % 2 == 0:
                add(line.strip('\n'), label_name_entry, button_index_2, password_index_frame, my_font_x21, button_index, current_label, content_frame, 0)
        file.close()

def append_file(label_name):
    path = 'C:\\Users\\piotr\\Documents\\Files\\python\\password_manager\\storage.txt'
    with open(path, 'a') as file:
        file.write(f'{label_name}\n\n')
    file.close()

def remove_from_file(line_numbers):
    path = 'C:\\Users\\piotr\\Documents\\Files\\python\\password_manager\\storage.txt'
    with open(path, 'r') as file:
        lines = file.readlines()

    # Remove the specified line numbers
    remaining_lines = [line for i, line in enumerate(lines, start=1) if i not in line_numbers]

    # Write the remaining lines back to the file
    with open(path, 'w') as file:
        file.writelines(remaining_lines)

def load_info(content_frame, my_font_x21, current_label, button_index_2):
    for child in content_frame.winfo_children():
        child.destroy()
    info: list[str] | None = get_label_info(current_label[0])
    if info and info != ['']:
        username_label_con(content_frame, my_font_x21, info[0])
        url_label_con(content_frame, my_font_x21, info[1])
        password_label_con(content_frame, my_font_x21, info[2])
    else:
        username_label_con(content_frame, my_font_x21, '')
        url_label_con(content_frame, my_font_x21, '')
        password_label_con(content_frame, my_font_x21, '')

def add(label_name, label_name_entry, button_index_2, password_index_frame, my_font_x21, button_index, current_label, content_frame, to_append_file):
    label_name_entry.delete('0', 'end')
    if label_name == '' or label_name in button_index_2:
        return
    new_label=ctk.CTkButton(master=password_index_frame, text=label_name, font=my_font_x21, corner_radius=5, fg_color=Colors.PINK, width=50,
                            border_color=Colors.GRAPHITE, border_width=2, hover_color=Colors.DARK_PINK, text_color=Colors.GRAPHITE,
                            command=lambda: button_clicked(new_label, current_label, button_index, button_index_2, content_frame, my_font_x21))
    new_label.pack(expand=True, fill='both', padx=1, pady=1)
    button_index.append(new_label)
    button_index_2.append(label_name)
    if to_append_file:
        append_file(button_index_2[-1])

def remove(current_label, button_index, button_index_2, content_frame):
    if current_label[0] != '':
        destroy_old_page(content_frame)
        button_index[int(button_index_2.index(current_label[0]))].destroy()
        remove_from_file({int(button_index_2.index(current_label[0])*2+1), int(button_index_2.index(current_label[0])*2+2)})
        button_index.pop(int(button_index_2.index(current_label[0])))
        button_index_2.pop(int(button_index_2.index(current_label[0])))
    current_label[0] = ''


def button_clicked(label, current_label, button_index, button_index_2, content_frame, my_font_x21):
    if current_label[0] != '':
        button_index[int(button_index_2.index(current_label[0]))].configure(fg_color=Colors.PINK)
    button_index[int(button_index_2.index(label.cget('text')))].configure(fg_color=Colors.DARK_PINK)
    current_label[0] = label.cget('text')
    load_info(content_frame, my_font_x21, current_label, button_index_2)

def on_validate(d, i, P, s, S, v, V, W):
    return len(P) <= 14

def after_login(app):
    my_font_x21 = ctk.CTkFont(family='Hack Nerd Font Propo', size=21)
    button_index = []
    button_index_2 = []
    current_label = ['']

    main_frame = ctk.CTkFrame(master=app, corner_radius=0, fg_color=Colors.BLUE_BACKGROUND)
    main_frame.pack(side='left', expand=True, fill='both', padx=0, pady=0)

    index_frame = ctk.CTkFrame(master=main_frame, corner_radius=7, fg_color=Colors.BLUE_BACKGROUND)
    index_frame.pack(side='left', fill='both', padx=8, pady=8)

    frame_for_border = ctk.CTkFrame(master=index_frame, corner_radius=7, border_color=Colors.GRAPHITE,
                                    fg_color=Colors.YELLOW, border_width=3)
    frame_for_border.pack(side='top', expand=True, fill='both', padx=0, pady=0)

    password_index_frame = ctk.CTkScrollableFrame(master=frame_for_border, corner_radius=7, scrollbar_button_hover_color=Colors.DARK_PINK,
                                                scrollbar_button_color=Colors.PINK, fg_color=Colors.YELLOW)
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

    add_button = ctk.CTkButton(master=buttons_index_frame, text='Add', font=my_font_x21, height=38,
                                command=lambda: add(str(label_name_entry.get()), label_name_entry, button_index_2, password_index_frame, my_font_x21, button_index, current_label,content_frame, 1),
                                border_color=Colors.GRAPHITE, border_width=2, fg_color=Colors.PINK, hover_color=Colors.DARK_PINK, text_color=Colors.GRAPHITE)
    add_button.pack(side='top', fill='x', padx=10, pady=0)

    content_frame = ctk.CTkFrame(master=main_frame, corner_radius=7, fg_color=Colors.YELLOW,
                                border_color=Colors.GRAPHITE, border_width=3)
    content_frame.pack(side='right', expand=True, fill='both', padx=8, pady=8)

    remove_button = ctk.CTkButton(master=buttons_index_frame, text='Remove',
                                font=my_font_x21, height=38, command=lambda: remove(current_label, button_index, button_index_2, content_frame),
                                border_color=Colors.GRAPHITE, border_width=2,
                                fg_color=Colors.PINK, hover_color=Colors.DARK_PINK,
                                text_color=Colors.GRAPHITE)
    remove_button.pack(side='top', fill='x', padx=10, pady=10)

    load_labels_from_file(button_index_2, label_name_entry, password_index_frame, my_font_x21, button_index, current_label, content_frame)

def main():
    app = ctk.CTk()
    app.title('Password manager')
    app.iconbitmap('password_manager\\resources\\icon.ico')
    x = app.winfo_screenwidth() // 2
    y = app.winfo_screenheight() // 2
    my_font_x16 = ctk.CTkFont(family='Hack Nerd Font Propo', size=16)
    app.geometry(f'1080x720+{x-540}+{y-400}')
    my_font_x32 = ctk.CTkFont(family='Hack Nerd Font Propo', size=32)
    app_frame = ctk.CTkFrame(master=app, fg_color=Colors.BLUE_BACKGROUND, corner_radius=0)
    app_frame.pack(expand=True, padx=0, pady=0, fill='both')
    login_page(app_frame, my_font_x32, my_font_x16)

    app.mainloop()

if __name__ == "__main__":
    main()
