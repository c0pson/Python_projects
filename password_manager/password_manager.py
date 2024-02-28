import customtkinter as ctk
from PIL import Image
from enum import Enum
import pyperclip

class Colors (str, Enum):
    BLUE_BACKGROUND = '#B5C0D0'
    GREEN ='#CCD3CA'
    YELLOW ='#F5E8DD'
    PINK ='#EED3D9'
    TEXT_COLOR = '#35374B'
    TRANSPARENT = 'transparent'

def login_proc(app, password_box):
    password = password_box.get()
    secret_password = '' # I will add some hashing or something like this
    if secret_password == password:
        for child in app.winfo_children():
            child.destroy()
        after_login(app)

def login_page(app, my_font):
    login_frame = ctk.CTkFrame(master=app, corner_radius=10, border_width=2,
                                fg_color=Colors.YELLOW, border_color=Colors.TEXT_COLOR)
    login_frame.pack(side='top', expand=True, padx=10, pady=10)

    password_label = ctk.CTkLabel(master=login_frame, fg_color=Colors.TRANSPARENT, text_color=Colors.TEXT_COLOR,
                                bg_color=Colors.TRANSPARENT, text='Password', font=my_font)
    password_label.pack(padx=5, pady=10)

    password_box = ctk.CTkEntry(master=login_frame, width=270, height=60, fg_color=Colors.GREEN,
                                corner_radius=10, font=my_font, show='*', text_color=Colors.TEXT_COLOR)
    password_box.pack(padx=15, pady=0)

    login_button = ctk.CTkButton(master=login_frame, width=120, height=50, fg_color=Colors.PINK, text_color=Colors.TEXT_COLOR,
                                corner_radius=10, text='Login', font=my_font, border_color=Colors.TEXT_COLOR, border_width=2,
                                hover_color='#cca9b0', command=lambda: login_proc(app, password_box))
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

def load_info(content_frame, current_label, my_font_x32, my_font_x21):
    for child in content_frame.winfo_children():
        child.destroy()
    title_label = ctk.CTkLabel(master=content_frame, corner_radius=5,
                            text=' '+''.join(current_label), font=my_font_x32, fg_color='#7D7C7C')
    title_label.pack(side='top', fill='x', padx=5, pady=5)

    url_frame = ctk.CTkFrame(master=content_frame, corner_radius=5)
    url_frame.pack(side='top', padx=5, pady=3, fill='x')

    url_text = ctk.CTkLabel(master=url_frame, text=' URL:  ', font=my_font_x32)
    url_text.pack(side='left', padx=2, pady=10)

    url_label = ctk.CTkEntry(master=url_frame, height=48, font=my_font_x32, state='disabled')
    url_label.pack(side='left', pady=10, fill='x', expand=True)

    edit_1_button = ctk.CTkButton(master=url_frame, corner_radius=5,
                                text='Edit', height=48, font=my_font_x21,
                                command=lambda: edit_label(url_label, edit_1_button))
    edit_1_button.pack(side='right', padx=8, pady=10)

    copy_1_button = ctk.CTkButton(master=url_frame, corner_radius=5,
                                text='Copy', height=48, font=my_font_x21,
                                command=lambda: copy_label(url_label))
    copy_1_button.pack(side='right', padx=16, pady=10)

    pass_frame = ctk.CTkFrame(master=content_frame, corner_radius=5)
    pass_frame.pack(side='top', padx=5, pady=3, fill='x')

    pass_frame_1 = ctk.CTkFrame(master=pass_frame, corner_radius=2)
    pass_frame_1.pack(side='top', padx=0, pady=0, fill='both')

    pass_text = ctk.CTkLabel(master=pass_frame_1, text=' Pass: ', font=my_font_x32)
    pass_text.pack(side='left', padx=2, pady=10)

    pass_label = ctk.CTkEntry(master=pass_frame_1, height=48, font=my_font_x32)
    pass_label.pack(side='left', pady=10, fill='x', expand=True)

    edit_2_button = ctk.CTkButton(master=pass_frame_1, corner_radius=5, text='Edit', height=48, font=my_font_x21)
    edit_2_button.pack(side='right', padx=8, pady=10)

    copy_2_button = ctk.CTkButton(master=pass_frame_1, corner_radius=5, text='Copy', height=48, font=my_font_x21)
    copy_2_button.pack(side='right', padx=16, pady=10)

    pass_frame_2 = ctk.CTkFrame(master=pass_frame, corner_radius=2)
    pass_frame_2.pack(side='top', padx=0, pady=0, fill='both')

    pass_str_text = ctk.CTkLabel(master=pass_frame_2, fg_color='transparent', text='Password strength')
    pass_str_text.pack(side='left', padx=20, pady=5)

    password_strength = ctk.CTkProgressBar(master=pass_frame_2)
    password_strength.set(0)
    password_strength.pack(side='right', fill='x', padx=20, pady=2, expand=True)

    buttons_frame = ctk.CTkFrame(master=content_frame, corner_radius=5)
    buttons_frame.pack(side='top', padx=5, pady=3, fill='both', expand=True)

def after_login(app):
    my_font_x32 = ctk.CTkFont(family='Hack Nerd Font Propo', size=32)
    my_font_x21 = ctk.CTkFont(family='Hack Nerd Font Propo', size=21)
    my_font_x16 = ctk.CTkFont(family='Hack Nerd Font Propo', size=16)

    button_index = []
    button_index_2 = []
    current_label = ['']

    def button_clicked(event, label):
        if current_label[0] != '':
            button_index[int(button_index_2.index(current_label[0]))].configure(fg_color='transparent')
        button_index[int(button_index_2.index(label.cget('text')))].configure(fg_color='gray')
        current_label[0] = label.cget('text')
        load_info(content_frame, current_label, my_font_x32, my_font_x21)

    def add():
        label_name = str(label_name_entry.get())
        label_name_entry.delete('0.0', 'end')
        if label_name == '' or label_name in button_index_2:
            return
        new_label=ctk.CTkLabel(master=password_index_frame, text=label_name, font=my_font_x21, corner_radius=5)
        new_label.bind(sequence='<Button-1>', command=lambda event: button_clicked(event, new_label))
        new_label.pack(side='top', fill='x', padx=3, pady=5)
        button_index.append(new_label)
        button_index_2.append(label_name)

    def remove():
        if current_label[0] != '':
            button_index[int(button_index_2.index(current_label[0]))].destroy()
            button_index.pop(int(button_index_2.index(current_label[0])))
            button_index_2.pop(int(button_index_2.index(current_label[0])))
        current_label[0] = ''

    main_frame = ctk.CTkFrame(master=app, corner_radius=0, fg_color=Colors.BLUE_BACKGROUND)
    main_frame.pack(side='left', expand=True, fill='both', padx=0, pady=0)

    index_frame = ctk.CTkFrame(master=main_frame, corner_radius=7, fg_color=Colors.BLUE_BACKGROUND)
    index_frame.pack(side='left', fill='both', padx=8, pady=8)

    password_index_frame = ctk.CTkScrollableFrame(master=index_frame, corner_radius=7,
                                                scrollbar_button_color='gray', fg_color=Colors.YELLOW)
    password_index_frame.pack(side='top', expand=True, fill='both', padx=0, pady=0)

    spacing_frame  = ctk.CTkFrame(master=index_frame, height=10, fg_color=Colors.TRANSPARENT)
    spacing_frame.pack()

    buttons_index_frame = ctk.CTkFrame(master=index_frame, corner_radius=7)
    buttons_index_frame.pack(side='bottom', fill='x', padx=0, pady=0)

    label_name_entry = ctk.CTkEntry(master=buttons_index_frame, font=my_font_x21, height=38)
    label_name_entry.pack(side='top', fill='x', padx=10, pady=8)

    add_button = ctk.CTkButton(master=buttons_index_frame, text='Add', font=my_font_x21, height=38, anchor='center', command=add)
    add_button.pack(side='top', fill='x', padx=10, pady=0)

    remove_button = ctk.CTkButton(master=buttons_index_frame, text='Remove', font=my_font_x21, height=38, anchor='center', command=remove)
    remove_button.pack(side='top', fill='x', padx=10, pady=8)

    content_frame = ctk.CTkFrame(master=main_frame, corner_radius=7)
    content_frame.pack(side='right', expand=True, fill='both', padx=8, pady=8)

def main():
    app = ctk.CTk()
    app.title('Password manager')
    x = app.winfo_screenwidth() // 2
    y = app.winfo_screenheight() // 2
    app.geometry(f'1080x720+{x-540}+{y-400}')
    my_font_x32 = ctk.CTkFont(family='Hack Nerd Font Propo', size=32)
    app_frame = ctk.CTkFrame(master=app, fg_color=Colors.BLUE_BACKGROUND, corner_radius=0)
    app_frame.pack(expand=True, padx=0, pady=0, fill='both')
    login_page(app_frame, my_font_x32)

    app.mainloop()

if __name__ == "__main__":
    main()
